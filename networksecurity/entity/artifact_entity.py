from dataclasses import dataclass
import os
import sys


@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str