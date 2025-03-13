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
def temp_test_dir(request):
    """Create a temporary test directory for rats and clean up after tests."""
    # TODO: Create a unique test directory and clean it up after tests
    pass


@pytest.fixture
def clean_registry():
    """Reset the rat registry before and after tests."""
    # TODO: Clear the registry before and after tests
    pass


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
    # TODO: Implement test rat creation logic
    pass


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
    # TODO: Implement multiple test rats creation logic
    pass


def count_actual_rat_files(directory: str, include_burrows: bool = True) -> Tuple[int, int]:
    """Count actual rat files in the filesystem.
    
    Args:
        directory: Directory to count rats in
        include_burrows: Whether to include rats in burrows
        
    Returns:
        Tuple of (rat_count, burrow_count)
    """
    # TODO: Implement file counting logic
    pass 