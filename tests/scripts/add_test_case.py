"""Module to add a test case to the software"""

import json
import os
import pathlib
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

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


@dataclass
class TestCase:
    """Class representing a test case for the software."""

    name: str
    description: str
    input_data: InputData
    expected_output: dict = field(default_factory=dict)

    def run_test(self):
        """Run the test case and return True if it passes, False otherwise."""
        # Placeholder for actual test execution logic
        print(f"Running test case: {self.name}")
        # Simulate test logic here

        os.system("./run.sh")


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


def main():
    """Main function to demonstrate adding a test case."""

    test_case = load_test_case("Base Test")
    test_case.run_test()


if __name__ == "__main__":
    main()
