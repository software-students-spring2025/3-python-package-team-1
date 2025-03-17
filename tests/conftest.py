"""Test fixtures and utilities for RatPack tests."""

import os
import json
import random
import glob
import time
import pytest
import shutil
from typing import List, Dict, Any, Optional, Callable, Tuple

# Ensure src is in the path for imports
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ratpack.infest import RAT_REGISTRY, RAT_TYPES


@pytest.fixture
def temp_test_dir(tmp_path):
    """Create a temporary test directory for rats and clean up after tests."""
    # Create a unique test directory
    test_dir = tmp_path / "rats"
    test_dir.mkdir(parents=True, exist_ok=True)
    return test_dir
    

@pytest.fixture
def clean_registry():
    """Reset the rat registry before and after tests."""
    # Clear the registry before the test
    RAT_REGISTRY.clear()
    yield
    # Clear the registry after the test
    RAT_REGISTRY.clear()


def create_test_rat(
    directory: str,
    rat_type: str = "test_rat",
    in_burrow: bool = False,
    age: int = 100,
    hunger_level: int = 3,
    created_at: Optional[float] = None
) -> str:
    """Create a test rat file with specified properties.
    
    Args:
        directory: Directory to create the rat in
        rat_type: Type of rat to create
        in_burrow: Whether to create the rat in a burrow
        age: Age of the rat
        hunger_level: Hunger level of the rat
        created_at: Creation timestamp, uses current time if None
        
    Returns:
        Path to the created rat file
    """
    if created_at is None:
        created_at = time.time()
    
    # Create a burrow if needed
    if in_burrow:
        burrow_name = f"rat_burrow_{int(created_at)}_{random.randint(1000, 9999)}"
        burrow_path = os.path.join(directory, burrow_name)
        os.makedirs(burrow_path, exist_ok=True)
        
        # Register the burrow
        RAT_REGISTRY[burrow_path] = {
            "type": "burrow",
            "created_at": created_at,
            "contains": []
        }
        
        # Create rat inside the burrow
        rat_name = f"{rat_type}_{int(created_at)}_{random.randint(1000, 9999)}.rat"
        rat_path = os.path.join(burrow_path, rat_name)
    else:
        # Create individual rat
        rat_name = f"{rat_type}_{int(created_at)}_{random.randint(1000, 9999)}.rat"
        rat_path = os.path.join(directory, rat_name)
    
    # Create rat file with metadata
    rat_data = {
        "type": rat_type,
        "created_at": created_at,
        "hunger_level": hunger_level,
        "age": age
    }
    
    with open(rat_path, 'w') as f:
        json.dump(rat_data, f, indent=2)
    
    # Register the rat
    if in_burrow:
        RAT_REGISTRY[burrow_path]["contains"].append(rat_path)
    else:
        RAT_REGISTRY[rat_path] = {
            "type": "rat",
            "data": rat_data
        }
    
    return rat_path


def create_test_rats(
    directory: str,
    count: int = 5,
    rat_types: Optional[List[str]] = None,
    in_burrow: bool = False,
    time_spread: int = 10
) -> List[str]:
    """Create multiple test rats with different properties.
    
    Args:
        directory: Directory to create rats in
        count: Number of rats to create
        rat_types: Types of rats to create, uses RAT_TYPES if None
        in_burrow: Whether to create rats in a burrow
        time_spread: Time difference between rats in seconds
        
    Returns:
        List of paths to created rat files
    """
    if rat_types is None:
        rat_types = RAT_TYPES
    
    rat_files = []
    base_time = time.time() - (count * time_spread)
    
    # Create rats with different timestamps
    for i in range(count):
        rat_type = random.choice(rat_types)
        created_at = base_time + (i * time_spread)
        rat_path = create_test_rat(
            directory=directory,
            rat_type=rat_type,
            in_burrow=in_burrow,
            age=random.randint(1, 500),
            hunger_level=random.randint(1, 5),
            created_at=created_at
        )
        rat_files.append(rat_path)
    
    return rat_files


def count_actual_rat_files(directory: str, include_burrows: bool = True) -> Tuple[int, int]:
    """Count actual rat files in the filesystem.
    
    Args:
        directory: Directory to count rats in
        include_burrows: Whether to include rats in burrows
        
    Returns:
        Tuple of (rat_count, burrow_count)
    """
    rat_count = 0
    burrow_count = 0
    
    # Count individual rats
    rat_count += len(glob.glob(os.path.join(directory, "*.rat")))
    
    # Count burrows and rats in burrows
    if include_burrows:
        for burrow_dir in glob.glob(os.path.join(directory, "rat_burrow_*")):
            if os.path.isdir(burrow_dir):
                burrow_count += 1
                rat_count += len(glob.glob(os.path.join(burrow_dir, "*.rat")))
    
    return rat_count, burrow_count 