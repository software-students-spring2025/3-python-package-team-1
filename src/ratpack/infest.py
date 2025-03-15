"""Module for simulating rat infestations in code.

This module provides functions to create, count, visualize, and remove virtual rat infestations
represented as files on the filesystem.
"""

import os
import random
import time
import json
import glob
import functools
import typing
from typing import List, Dict, Any, Optional, Callable, Set, Tuple, Union
import shutil

# Registry to keep track of rat files created
RAT_REGISTRY: Dict[str, Dict[str, Any]] = {}

# Available rat types
RAT_TYPES = ["sewer_rat", "brown_rat", "black_rat", "fancy_rat", "plague_rat"]

def infest(
    infestation_level: int = 3,
    rat_types: Optional[List[str]] = None,
    burrow_probability: float = 0.2
) -> Callable:
    """Decorator that creates rat files when the decorated function is called.
    
    Args:
        infestation_level: Controls how many rats are created (1-5)
        rat_types: List of rat types to create. If None, all types can appear
        burrow_probability: Chance (0.0-1.0) of creating a rat burrow instead of individual rats
        
    Returns:
        The decorated function
    """
    # TODO: Implement the decorator that wraps functions and creates rats when called
    pass

def create_rats(
    infestation_level: int,
    rat_types: List[str],
    burrow_probability: float,
    directory: str = "."
) -> None:
    """Create rat files in the specified directory.
    
    Args:
        infestation_level: Controls how many rats are created (1-5)
        rat_types: List of rat types to create
        burrow_probability: Chance (0.0-1.0) of creating a rat burrow
        directory: Directory to create rats in
    """
    # TODO: Implement rat file creation logic
    pass

def count_rats(
    directory: str = ".",
    include_burrows: bool = True,
    rat_types: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Count rat files in the specified directory.
    
    Args:
        directory: Directory to count rats in
        include_burrows: Whether to count rats inside burrows
        rat_types: List of rat types to count. If None, count all types
        
    Returns:
        Dictionary with statistics about the rat infestation
    """
    # TODO: Implement rat counting logic and return statistics
    pass

def exterminate(
    directory: str = ".",
    rat_types: Optional[List[str]] = None,
    burrows_only: bool = False,
    dry_run: bool = False
) -> Dict[str, Any]:
    """Remove rat files from the specified directory.
    
    Args:
        directory: Directory to remove rats from
        rat_types: List of rat types to remove. If None, remove all types
        burrows_only: If True, only remove burrows and rats inside them
        dry_run: If True, don't actually remove files, just report what would be removed
        
    Returns:
        Dictionary with statistics about the extermination
    """
    # TODO: Implement rat removal logic and return statistics
    pass

def visualize_infestation(
    directory: str = ".",
    output_format: str = "text",
    include_burrows: bool = True
) -> str:
    """Visualize the rat infestation.
    
    Args:
        directory: Directory to visualize rats in
        output_format: Format of the output, either "text" or "ascii"
        include_burrows: Whether to include rats inside burrows
        
    Returns:
        String representation of the rat infestation
    """
    visualized = ''
 
    for root, __, files in os.walk(directory):
        path = root.split(os.sep)
        visualized += (len(path) - 1) * '---' + os.path.basename(root) + '\n'
        for file in files:
            if (file == 'rat'): ### how do we want to visualize this
                visualized += len(path) * '---' + '🐀\n'
            else:
                visualized += len(path) * '---' + file + '\n'
    
    if output_format == 'ascii': ### not sure about this
        return list(bytes(visualized, 'ascii'))


    return visualized
