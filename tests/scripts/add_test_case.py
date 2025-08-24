"""Module to add a test case to the software"""

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

    base_path: pathlib.Path = field(default_factory=pathlib.Path)

    def get_path(self, field_name: str) -> pathlib.Path:
        """Get the full path for a specific input data file."""
        if not hasattr(self, field_name):
            raise ValueError(f"Field '{field_name}' does not exist in InputDataFiles.")

        path = self.base_path / getattr(self, field_name)
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

        self.analysis_settings = pd.read_json(
            self.data_files.get_path("analysis_settings")
        ).to_dict()

        self.location = pd.read_csv(self.data_files.get_path("location"))

        self.configuration = pd.read_json(
            self.data_files.get_path("configuration")
        ).to_dict()

    @abstractmethod
    def edit_account(self):
        """Edit the account data as needed for the test case."""
        pass

    @abstractmethod
    def edit_analysis_settings(self):
        """Edit the analysis settings as needed for the test case."""
        pass

    @abstractmethod
    def edit_location(self):
        """Edit the location data as needed for the test case."""
        pass

    @abstractmethod
    def edit_configuration(self):
        """Edit the configuration data as needed for the test case."""
        pass


@dataclass
class TestCase:
    """Class representing a test case for the software."""

    name: str
    description: str
    input_data: dict
    expected_output: dict = field(default_factory=dict)

    def run_test(self) -> bool:
        """Run the test case and return True if it passes, False otherwise."""
        # Placeholder for actual test execution logic
        print(f"Running test case: {self.name}")
        # Simulate test logic here
        actual_output = self.input_data
