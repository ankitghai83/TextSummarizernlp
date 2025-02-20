## entity is nothing but return type of function and to define that we can use dataclasses
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class   DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

