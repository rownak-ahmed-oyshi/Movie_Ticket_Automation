# utils/data_loader.py

import json
from pathlib import Path
import os


def load_booking_test_data(key):
    """
    Loads test data from booking_data.json for a specific key.
    The path is resolved relative to the project root.
    """
    # Get the absolute path to the directory where this script (data_loader.py) is located
    current_dir = Path(__file__).resolve().parent

    # Construct the path to the booking_data.json file from the utils folder
    file_path = current_dir.parent / "data" / "booking_data.json"

    if not file_path.exists():
        raise FileNotFoundError(f"File not found at: {file_path}")

    with open(file_path, 'r') as f:
        data = json.load(f)

    return data.get(key, [])