"""Tests for the count_rats function."""

import os
import json
import time
import glob
import pytest

from ratpack.infest import count_rats, RAT_REGISTRY, RAT_TYPES
from tests.conftest import create_test_rat, create_test_rats, count_actual_rat_files


def test_basic_counting(temp_test_dir, clean_registry):
    """Test 2.1: Verify that count_rats() correctly counts all rats in a directory."""
    # TODO: Create rat files and verify they are counted correctly
    num_rats = 4
    create_test_rats(temp_test_dir, num_rats)
    counted_rats = count_rats(temp_test_dir)
    assert counted_rats["total_rats"] == num_rats, f"Expected {num_rats}, but got {counted_rats['total_rats']}"

def test_directory_parameter(temp_test_dir, clean_registry):
    """Test 2.2: Verify that the directory parameter limits counting to a specific directory."""
    # TODO: Test that only rats in the specified directory are counted
    create_test_rats(temp_test_dir, 3)
    # create another directory to test against
    # the other directory has different number of rats
    another_dir = temp_test_dir / "other_dir"
    another_dir.mkdir()
    create_test_rats(another_dir, 2)
    counted_rats = count_rats(temp_test_dir)
    # If get something different from 3
    assert counted_rats["total_rats"] == 3, f"Expected 3, but got {counted_rats['total_rats']}"

    # If get something different from 2
    counted_rats_other = count_rats(another_dir)
    assert counted_rats_other["total_rats"] == 2, f"Expected 2, but got {counted_rats_other['total_rats']}"


def test_include_burrows_parameter(temp_test_dir, clean_registry):
    """Test 2.3: Verify that the include_burrows parameter controls whether rats in burrows are counted."""
    # TODO: Test counting rats with and without including burrows
    pass


def test_rat_types_parameter(temp_test_dir, clean_registry):
    """Test 2.4: Verify that the rat_types parameter filters rats by type."""
    # TODO: Test counting only specific rat types
    pass


def test_statistics_accuracy(temp_test_dir, clean_registry):
    """Test 2.5: Verify that the statistics in the return value are accurate."""
    # TODO: Test the accuracy of the statistics returned by count_rats
    pass 