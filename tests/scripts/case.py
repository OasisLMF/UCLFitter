"""Module to add a test case to the software"""

import json
import pathlib
import shutil
import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Type, Optional

import pandas as pd


@dataclass
class InputDataFiles:
    """Class representing input datafiles for the test case."""

    account: str = "account.csv"
    analysis_settings: str = "analysis_settings.json"
    location: str = "location.csv"
    configuration: str = "oasislmf.json"

    base_path: str = "."

    def get_path(self, field_name: str) -> pathlib.Path:
        """Get the full path for a specific input data file."""
        if not hasattr(self, field_name):
            raise ValueError(f"Field '{field_name}' does not exist in InputDataFiles.")

        path = pathlib.Path(self.base_path) / getattr(self, field_name)
        if not path.exists():
            raise FileNotFoundError(f"File '{path}' does not exist.")

        return path


@dataclass
class InputData(ABC):
    """Class representing input data for the test case."""

    data_files: InputDataFiles

    account: pd.DataFrame = field(init=False)
    analysis_settings: dict = field(init=False)
    location: pd.DataFrame = field(init=False)
    configuration: dict = field(init=False)

    def __post_init__(self):
        self.account = pd.read_csv(self.data_files.get_path("account"))

        with open(
            self.data_files.get_path("analysis_settings"), "r", encoding="utf-8"
        ) as f:
            self.analysis_settings = json.load(f)

        self.location = pd.read_csv(self.data_files.get_path("location"))

        with open(
            self.data_files.get_path("configuration"), "r", encoding="utf-8"
        ) as f:
            self.configuration = json.load(f)

    def write_files(self):
        """Write the modified input data back to their respective files."""
        self.account.to_csv(self.data_files.get_path("account"), index=False)

        with open(
            self.data_files.get_path("analysis_settings"), "w", encoding="utf-8"
        ) as f:
            json.dump(self.analysis_settings, f, ensure_ascii=False, indent=4)

        self.location.to_csv(self.data_files.get_path("location"), index=False)

        with open(
            self.data_files.get_path("configuration"), "w", encoding="utf-8"
        ) as f:
            json.dump(self.configuration, f, ensure_ascii=False, indent=4)

    @abstractmethod
    def edit_account(self):
        """Edit the account data as needed for the test case."""

    @abstractmethod
    def edit_analysis_settings(self):
        """Edit the analysis settings as needed for the test case."""

    @abstractmethod
    def edit_location(self):
        """Edit the location data as needed for the test case."""

    @abstractmethod
    def edit_configuration(self):
        """Edit the configuration data as needed for the test case."""


def ensure_accounts_for_locations(
    account_df: pd.DataFrame, location_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Ensure account dataframe has at least one row for each AccNumber in location.
    Copy details from existing rows when creating new account entries.

    Args:
        account_df: The account DataFrame
        location_df: The location DataFrame containing AccNumber references

    Returns:
        pd.DataFrame: Updated account DataFrame with all required AccNumbers

    Raises:
        ValueError: If account dataframe is empty and no template row is available
    """
    # Get unique AccNumbers from location dataframe
    location_acc_numbers = set(location_df["AccNumber"].unique())

    # Get existing AccNumbers from account dataframe
    existing_acc_numbers = (
        set(account_df["AccNumber"].unique())
        if "AccNumber" in account_df.columns
        else set()
    )

    # Find AccNumbers that are missing from account
    missing_acc_numbers = location_acc_numbers - existing_acc_numbers

    if not missing_acc_numbers:
        print("All AccNumbers from location already exist in account dataframe")
        return account_df

    print(f"Adding {len(missing_acc_numbers)} missing account entries")

    # Get a template row from existing account data (use first row as template)
    if len(account_df) > 0:
        template_row = account_df.iloc[0].copy()
    else:
        raise ValueError("Account dataframe is empty and no template row is available.")

    # Create new rows for missing AccNumbers
    new_rows = []
    for acc_number in sorted(missing_acc_numbers):
        new_row = template_row.copy()
        new_row["AccNumber"] = acc_number
        # Update account name to reflect the new AccNumber
        if "AccName" in new_row:
            new_row["AccName"] = f"Account_{acc_number}"
        new_rows.append(new_row)

    # Create DataFrame from new rows and concatenate with existing account data
    if new_rows:
        new_account_df = pd.DataFrame(new_rows)
        updated_account_df = pd.concat([account_df, new_account_df], ignore_index=True)

        # Sort by AccNumber for better organization
        updated_account_df = updated_account_df.sort_values("AccNumber").reset_index(
            drop=True
        )

        print(f"Account dataframe now has {len(updated_account_df)} rows")
        return updated_account_df

    return account_df


class DefaultInputData(InputData):
    """Default implementation of InputData with no edits."""

    def edit_account(self):
        pass

    def edit_analysis_settings(self):
        pass

    def edit_location(self):
        pass

    def edit_configuration(self):
        pass


class Policy2(InputData):
    """Implementation of InputData for damage-dependent test cases."""

    def edit_account(self, damage_slab: list = None, payout: list = None):
        """
        Ensure account dataframe has at least one row for each AccNumber in location,
        then create damage slabs with trigger ranges and payouts.

        Args:
            damage_slab: List of floats representing damage slab sizes (will be normalized to sum to 1)
            payout: List of int/float representing payouts for each slab (same length as damage_slab)
        """
        # Default damage slabs and payouts if not provided
        if damage_slab is None:
            raise ValueError("damage_slab must be provided")
        if payout is None:
            raise ValueError("payout must be provided")

        # Validate inputs
        if len(damage_slab) != len(payout):
            raise ValueError("damage_slab and payout must have the same length")

        if not damage_slab or not payout:
            raise ValueError("damage_slab and payout cannot be empty")

        # Ensure we have accounts for all locations first
        self.account = ensure_accounts_for_locations(self.account, self.location)

        # Normalize damage_slab to sum to 1
        total_slab = sum(damage_slab)
        if total_slab == 0:
            raise ValueError("damage_slab cannot sum to zero")

        normalized_slab = [slab / total_slab for slab in damage_slab]

        print(
            f"Creating damage slabs: {len(normalized_slab)} slabs for {len(self.account)} base accounts"
        )
        print(f"Normalized slabs: {[f'{slab:.3f}' for slab in normalized_slab]}")
        print(f"Payouts: {payout}")

        # Store the original account data
        original_accounts = self.account.copy()

        # Create new rows for each damage slab
        new_account_rows = []

        for _, account_row in original_accounts.iterrows():
            print(f"Processing AccNumber: {account_row['AccNumber']}")
            # Calculate trigger ranges for this account
            cumulative = 0.0

            for i, (slab_size, slab_payout) in enumerate(zip(normalized_slab, payout)):
                # Create a copy of the account row for this slab
                new_row = account_row.copy()

                # Set trigger ranges
                trigger_start = cumulative
                trigger_end = cumulative + slab_size

                # Add the new columns
                new_row["TriggerBuildingStart"] = trigger_start
                new_row["TriggerBuildingEnd"] = trigger_end
                new_row["PayOutBuildingStart"] = slab_payout
                new_row["PayOutBuildingEnd"] = ""
                new_row["DeductibleBuilding"] = ""
                new_row["StepTriggerType"] = 1
                new_row["TriggerType"] = 2
                new_row["StepFunctionName"] = 28 if trigger_end == 1 else 27
                new_row["PayOutType"] = 1 if trigger_end == 1 else 2
                new_row["PayoutLimitBuilding"] = 1e3
                new_row["StepNumber"] = i % 3 + 1
                new_row["PolPeril"] = "QTS"

                # Update account name to include slab info
                if "AccName" in new_row:
                    base_name = new_row["AccName"]
                    new_row["AccName"] = f"{base_name}_Slab_{i+1}"

                new_account_rows.append(new_row)
                cumulative = trigger_end

        # Replace the account dataframe with the new slab-based structure
        if new_account_rows:
            self.account = pd.DataFrame(new_account_rows).reset_index(drop=True)

            # Sort by AccNumber and then by TriggerBuildingStart for organization
            self.account = self.account.sort_values(
                ["AccNumber", "TriggerBuildingStart"]
            ).reset_index(drop=True)

            print(f"Created {len(self.account)} account rows with damage slabs")
            print(
                f"Expected: {len(normalized_slab)} slabs × {len(original_accounts)} accounts = {len(normalized_slab) * len(original_accounts)} rows"
            )
        else:
            print("No account rows were created")

    def edit_analysis_settings(self):
        # Example edit: Change analysis type to damage-dependent
        pass

    def edit_location(self):
        # Each location has its own account number
        self.location["AccNumber"] = self.location["LocNumber"]

    def edit_configuration(self):
        # Example edit: Update configuration for damage-dependent analysis
        pass


@dataclass
class TestCase:
    """Class representing a test case for the software."""

    name: str
    description: str
    input_data: InputData
    expected_output: dict = field(default_factory=dict)

    def run_test(
        self,
        verbose: bool = False,
        dry_run: bool = False,
        output_dir: Optional[str] = None,
    ) -> bool:
        """
        Run the test case using the enhanced run.sh script.

        Args:
            verbose: Enable verbose output
            dry_run: Show what would be executed without running
            output_dir: Custom output directory for results

        Returns:
            bool: True if test passes, False otherwise
        """
        print(f"Running test case: {self.name}")
        print(f"Description: {self.description}")

        # Get the absolute path to the test data
        test_dir = pathlib.Path(self.input_data.data_files.base_path).resolve()
        config_file = self.input_data.data_files.configuration

        # Get the absolute path to run.sh
        script_dir = pathlib.Path(__file__).parent
        run_script = script_dir / "run.sh"

        if not run_script.exists():
            print(f"Error: run.sh script not found at {run_script}")
            return False

        # Build command arguments
        cmd = [str(run_script)]

        # Add options
        if verbose:
            cmd.append("--verbose")
        if dry_run:
            cmd.append("--dry-run")
        if output_dir:
            cmd.extend(["--output", output_dir])

        # Add test directory (relative to tests/ folder)
        # Convert absolute path to relative path from tests/ directory
        tests_root = script_dir.parent  # /path/to/tests
        try:
            relative_test_dir = test_dir.relative_to(tests_root)
            cmd.append(str(relative_test_dir))
        except ValueError:
            # If not relative to tests/, use absolute path
            cmd.append(str(test_dir))

        # Add config file
        cmd.append(config_file)

        print(f"Executing: {' '.join(cmd)}")

        try:
            # Run the command
            result = subprocess.run(
                cmd, capture_output=True, text=True, cwd=script_dir, check=False
            )

            # Print output
            if result.stdout:
                print("STDOUT:")
                print(result.stdout)

            if result.stderr:
                print("STDERR:")
                print(result.stderr)

            # Check if successful
            if result.returncode == 0:
                print(f"✅ Test case '{self.name}' completed successfully!")
                return True
            else:
                print(
                    f"❌ Test case '{self.name}' failed with exit code {result.returncode}"
                )
                return False

        except FileNotFoundError:
            print(f"Error: Could not execute {run_script}")
            return False


def load_test_case(
    test_name: str, test_list=pathlib.Path("../test_list.json")
) -> TestCase:
    """Load a test case by name from a JSON file."""
    if not test_list.exists():
        raise FileNotFoundError(f"Test list file '{test_list}' does not exist.")

    with open(test_list, "r", encoding="utf-8") as f:
        tests = json.load(f)

    for test in tests:
        if test["name"] == test_name:
            data_files = InputDataFiles(base_path=test.get("base_path", "."))
            input_data = DefaultInputData(data_files=data_files)
            return TestCase(
                name=test["name"],
                description=test.get("description", ""),
                input_data=input_data,
                expected_output=test.get("expected_output", {}),
            )

    raise ValueError(f"Test case '{test_name}' not found in '{test_list}'.")


def create_new_test_case(
    name: str,
    description: str,
    input_data_class: Type[InputData],
    base_test_path: str = "../test_java",
    tests_root: str = "..",
    overwrite: bool = False,
) -> TestCase:
    """
    Create a new test case with the specified InputData class and create a new folder.

    Args:
        name: Name of the test case
        description: Description of the test case
        input_data_class: Concrete InputData class to use for this test case
        base_test_path: Path to the base test case to copy files from
        tests_root: Root directory where test folders are created
        overwrite: Whether to overwrite existing test cases

    Returns:
        TestCase: The created test case

    Raises:
        FileNotFoundError: If base test path doesn't exist
        ValueError: If the test folder already exists
    """
    # Sanitize the test name for folder creation
    folder_name = name.lower().replace(" ", "_").replace("-", "_")
    test_folder_path = pathlib.Path(tests_root) / f"test_{folder_name}"
    base_test_path = pathlib.Path(base_test_path)

    # Check if base test exists
    if not base_test_path.exists():
        raise FileNotFoundError(f"Base test path '{base_test_path}' does not exist.")

    # Check if test folder already exists
    if test_folder_path.exists():
        if not overwrite:
            raise ValueError(f"Test folder '{test_folder_path}' already exists.")

        print(
            f"Warning: Test folder '{test_folder_path}' already exists and will be overwritten."
        )
        shutil.rmtree(test_folder_path)

    # Create the new test folder
    test_folder_path.mkdir(parents=True, exist_ok=False)
    print(f"Created test folder: {test_folder_path}")

    # Copy base files to the new test folder
    files_to_copy = [
        "account.csv",
        "location.csv",
        "analysis_settings.json",
        "oasislmf.json",
    ]

    for file_name in files_to_copy:
        source_file = base_test_path / file_name
        if source_file.exists():
            dest_file = test_folder_path / file_name
            shutil.copy2(source_file, dest_file)
            print(f"Copied {file_name} to {test_folder_path}")
        else:
            print(f"Warning: {file_name} not found in base test, skipping...")

    # Create InputDataFiles pointing to the new folder
    data_files = InputDataFiles(base_path=str(test_folder_path))

    # Create the InputData instance using the specified class
    input_data = input_data_class(data_files=data_files)

    # Apply the specific edits for this InputData class
    input_data.edit_location()

    # For Policy2, we can pass custom damage slabs and payouts
    if hasattr(input_data, "edit_account") and input_data_class == Policy2:
        # Example with custom damage slabs and payouts
        custom_damage_slab = [0.3, 0.4, 0.3]  # 30%, 40%, 30%
        custom_payout = [7.5e6, 19e6, 30e6]  # Progressive payouts
        input_data.edit_account(damage_slab=custom_damage_slab, payout=custom_payout)
    else:
        input_data.edit_account()

    input_data.edit_analysis_settings()
    input_data.edit_configuration()

    # Write the modified files
    input_data.write_files()
    print(f"Applied {input_data_class.__name__} modifications and saved files")

    # Create and return the TestCase
    test_case = TestCase(name=name, description=description, input_data=input_data)

    # Update the test list JSON file
    _update_test_list(name, str(test_folder_path), description)

    return test_case


def _update_test_list(
    name: str,
    folder_path: str,
    description: str,
    test_list_path: str = "../test_list.json",
):
    """
    Update the test_list.json file with the new test case.

    Args:
        name: Name of the test case
        folder_path: Path to the test folder
        description: Description of the test case
        test_list_path: Path to the test list JSON file
    """
    test_list_file = pathlib.Path(test_list_path)

    # Load existing tests or create empty list
    if test_list_file.exists():
        with open(test_list_file, "r", encoding="utf-8") as f:
            tests = json.load(f)
    else:
        tests = []

    # Add the new test case
    new_test = {"name": name, "base_path": folder_path, "description": description}

    # Check if test already exists
    for test in tests:
        if test["name"] == name:
            print(f"Warning: Test '{name}' already exists in test list, updating...")
            test.update(new_test)
            break
    else:
        tests.append(new_test)

    # Write back to file
    with open(test_list_file, "w", encoding="utf-8") as f:
        json.dump(tests, f, ensure_ascii=False, indent=4)

    print(f"Updated test list: {test_list_file}")


def main():
    """Main function to demonstrate creating and running test cases."""

    # Example 1: Load and run an existing test case
    # print("=== Loading and running existing test case ===")
    # try:
    #     base_test = load_test_case("Base Test")
    #     success = base_test.run_test(verbose=True)
    #     print(f"Base test {'PASSED' if success else 'FAILED'}")
    # except Exception as e:
    #     print(f"Error with base test: {e}")

    # Example 2: Create a new test case with Policy2 modifications
    print("\n=== Creating new test case ===")
    try:
        new_test = create_new_test_case(
            name="Policy Test 2",
            description="Test case with damage-dependent policies v2",
            input_data_class=Policy2,
            base_test_path="../test_java",
            overwrite=True,
        )
        print(f"Successfully created test case: {new_test.name}")

        # Run the new test with different options
        print("\n--- Running new test with verbose output ---")
        success = new_test.run_test(verbose=True)
        print(f"New test {'PASSED' if success else 'FAILED'}")

    except (FileNotFoundError, ValueError) as e:
        print(f"Error creating test case: {e}")

    # # Example 3: Run with dry-run mode
    # print("\n=== Dry run example ===")
    # try:
    #     test_case = load_test_case("Base Test")
    #     print("Running in dry-run mode (shows what would be executed):")
    #     test_case.run_test(dry_run=True, verbose=True)
    # except Exception as e:
    #     print(f"Error with dry run: {e}")


if __name__ == "__main__":
    main()
