"""Module for simulating rat infestations in code.

This module provides functions to create, count, visualize, and remove virtual rat infestations
represented as files on the filesystem.
"""

import os
import random
import importlib.resources
from functools import wraps
import time
import json
import glob
import typing
from typing import List, Dict, Any, Optional, Callable, Set, Tuple, Union
import shutil

from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
from pathlib import Path

# Registry to keep track of rat files created
RAT_REGISTRY: Dict[str, Dict[str, Any]] = {}

# Available rat types
RAT_TYPES = ["sewer_rat", "brown_rat", "black_rat", "fancy_rat", "plague_rat"]

def infest(
    infestation_level: int = 3,
    rat_types: Optional[List[str]] = None,
    burrow_probability: float = 0.2,
    random_seed: int = None,
    directory: str = "."
) -> Callable:
    """Decorator that creates rat files when the decorated function is called.
    
    Args:
        infestation_level: Controls how many rats are created (1-5)
        rat_types: List of rat types to create. If None, all types can appear
        burrow_probability: Chance (0.0-1.0) of creating a rat burrow instead of individual rats
        random_seed: Set the random seed of the random number generator
    Returns:
        The decorated function
    """
    # set random seed
    if random_seed is not None:
        random.seed(random_seed)

    def decorator(func):
        # TODO: add handling for not decorating functions in this package
        @wraps(func)
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

    # cap the infestation level and burrow probability
    infestation_level = max(1, infestation_level)
    infestation_level = min(5, infestation_level)

    burrow_probability = max(0.0, burrow_probability)
    burrow_probability = min(1.0, burrow_probability)

    # load images directory for rat infesting
    with importlib.resources.files(__package__).joinpath('images') as images_path:
        images = [file for file in images_path.iterdir() if file.is_file()]

    while infestation_level > 0:

        in_burrow = False

        if burrow_probability > random.random():
            ## create a new directory
            ## iteratively make burrows and take all rats into burrow
            directory = os.path.join(directory, 'burrow')
            os.makedirs(directory, exist_ok=True)
            burrow_probability -= 0.2
            in_burrow = True

            # Register the burrow
            RAT_REGISTRY[directory] = {
                "type": "burrow",
                "contains": []
            }
            

        # TODO: add more advanced file creation logic
        rat_count = count_rats(directory, include_burrows=False)['total_rats']

        src_image_path = random.choice(images)

        if rat_types is None:
            rat_types = RAT_TYPES

        rat_type = random.choice(rat_types)

        rat_path = os.path.join(directory, f'{rat_type}_id_{rat_count + 1}.rat')

        rat_data = {
            "type": rat_type,
            "id": rat_count + 1
        }
        
        shutil.copy(src_image_path, rat_path)
        
        # Register the rat
        if in_burrow:
            RAT_REGISTRY[directory]["contains"].append(rat_path)
        else:
            RAT_REGISTRY[rat_path] = {
                "type": "rat",
                "data": rat_data
            }          

        infestation_level -= 1

def check_path(
    path: Path
) -> bool:
    """Checks if an path is valid for the package to modify.
    
    Args:
        path: pathname
    Returns:
        True if the path is either a directory named burrow or a image with the correct tags
    """
    if not os.path.isdir(path):
        return 'rat_id' in path and '.rat' in path

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
    rat_files = [file for file in os.listdir(directory) if check_path(os.path.join(directory, file))]
    
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
            burrow_files = [file for file in os.listdir(burrow_dir) if check_path(os.path.join(directory, file))]
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
    stats = {'rats_removed': 0, 'burrows_removed': 0}  
    if (burrows_only):
        stats['surface_rats_left'] = count_rats(directory=directory)['surface_rats']

    types_remove = rat_types if rat_types is not None else RAT_TYPES
    in_burrow = False
    for root, __, files in os.walk(directory):
            fn = os.path.basename(root)
            if fn == 'burrow':
                stats['burrows_removed'] += 1
                in_burrow = True
            for file in files:
                if check_path(os.path.join(directory, file)): ### how do we want to visualize this
                    matching_rats = [rat for rat in types_remove if rat in file]
                    if matching_rats:
                        if not in_burrow and burrows_only:
                            continue
                        stats['rats_removed'] += 1
                        if not dry_run:
                            os.remove(os.path.join(root,file))

    #finally removing burrow as long as its not empty
    burrow_dir = os.path.join(directory,'burrow')
    if os.path.exists(burrow_dir):
        if not dry_run and len(os.listdir(burrow_dir)) == 0:
            try:
                shutil.rmtree(burrow_dir)
            except Exception as e:
                print(f"Error removing directory '{burrow_dir}': {e}")

    return stats

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
        visualized += f"Total rats: {rat_ct['total_rats']} \n"
        for root, __, files in os.walk(directory):
            path = root.split(os.sep)
            fn = os.path.basename(root)
            if check_path(root) or fn == 'burrow':
                visualized += (len(path) - 1) * '---' + fn + '\n'
            if fn == 'burrow' and not include_burrows:
                continue
            for file in files:
                if check_path(os.path.join(directory, file)): ### how do we want to visualize this
                    visualized += len(path) * '---' + file + '\n'
    else: #ascii
        visualized += "RAT INFESTATION ALERT \n"
        visualized += f"Total rats: {rat_ct['total_rats']} \n"
        for root, __, files in os.walk(directory):
            path = root.split(os.sep)
            fn = os.path.basename(root)
            if check_path(root) or fn == 'burrow':
                visualized += (len(path) - 1) * '---' + fn + '\n'
            if fn == 'burrow' and not include_burrows:
                continue
            for file in files:
                if check_path(os.path.join(directory, file)): ### how do we want to visualize this
                    visualized += len(path) * '---' + '''ᘛ⁐̤ᕐᐷ''' + '\n' 

    return visualized