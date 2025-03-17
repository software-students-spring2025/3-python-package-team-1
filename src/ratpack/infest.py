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
    def decorator(func):
        # TODO: add handling for not decorating functions in this package
        def wrapper(*args, **kwargs):
            create_rats(infestation_level, rat_types, burrow_probability)
            return func(*args, **kwargs)
        return wrapper
    return decorator

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

    # cap the infestation level and burrow probability
    infestation_level = max(1, infestation_level)
    infestation_level = min(5, infestation_level)

    burrow_probability = max(0.0, burrow_probability)
    burrow_probability = min(1.0, burrow_probability)

    while infestation_level > 0:

        if burrow_probability > random.random():
            ## create a new directory
            ## recursively make burrows and take all rats into burrow
            new_directory = directory + '/rat burrow'
            os.makedirs(new_directory)
            create_rats(infestation_level, rat_types, burrow_probability - 0.2, new_directory)
            infestation_level = 0
        else:
            # TODO: create one rat in current directory
            pass

        infestation_level -= 1

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
    rat_count = 0
    burrow_count = 0
    rat_files = [file for file in os.listdir(directory) if file.endswith(".rat")]
    
    if rat_types:
        filtered_files = []
        for file in rat_files:
            matching_rats = [rat for rat in rat_types if rat in file]
            if matching_rats:
                filtered_files.append(file)
        rat_files = filtered_files

    rat_count += len(rat_files)

    if include_burrows:
        burrow_dir = os.path.join(directory, "burrow")
        if os.path.exists(burrow_dir):
            burrow_files = [file for file in os.listdir(burrow_dir) if file.endswith(".rat")]
            if rat_types:
                filtered_files = []
                for file in rat_files:
                    matching_rats = [rat for rat in rat_types if rat in file]
                    if matching_rats:
                        filtered_files.append(file)
                rat_files = filtered_files
            burrow_count += len(burrow_files)

    return {
        "total_rats": rat_count + burrow_count,
        "surface_rats": rat_count,
        "burrowed_rats": burrow_count
    }

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
    visualized = ""

    rat_ct = count_rats(directory, include_burrows)
    
    if rat_ct['total_rats'] == 0:
        return 'No rats found \n Directory is clean \n'

    if output_format == 'text':
        visualized += "Rat Infestation Report\n"
        visualized += f"Total rats: {rat_ct["total_rats"]} \n"
        visualized += "Rats by type: \n" #TODO: count rats by type either here or in count_rats function
        for root, __, files in os.walk(directory):
            path = root.split(os.sep)
            fn = os.path.basename(root)
            if ".rat" in fn or fn == 'burrow':
                visualized += (len(path) - 1) * '---' + fn + '\n'
            if fn == 'burrow' and not include_burrows:
                continue
            for file in files:
                if ".rat" in file: ### how do we want to visualize this
                    visualized += len(path) * '---' + file + '\n'
    else: #ascii
        visualized += "RAT INFESTATION ALERT \n"
        visualized += f"Total rats: {rat_ct["total_rats"]} \n"
        for root, __, files in os.walk(directory):
            path = root.split(os.sep)
            fn = os.path.basename(root)
            if ".rat" in fn or fn == 'burrow':
                visualized += (len(path) - 1) * '---' + fn + '\n'
            if fn == 'burrow' and not include_burrows:
                continue
            for file in files:
                if ".rat" in file: ### how do we want to visualize this
                    visualized += len(path) * '---' + '''\n()——-()\n \o.o/\n  \ /~~~\n   `''' + '\n' 

    return visualized