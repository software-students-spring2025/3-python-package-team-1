"""Integration tests for the RatPack package."""

import os
import pytest

from ratpack.infest import infest, count_rats, exterminate, visualize_infestation
from tests.conftest import count_actual_rat_files


def test_full_workflow(temp_test_dir, clean_registry):
    """Test 5.1: Verify the entire workflow from infestation to extermination."""
    # TODO: Test full rat infestation workflow:
    # - Create decorated function and call it to create rats
    # - Check infestation with count_rats
    # - Visualize with visualize_infestation
    # - Exterminate with exterminate
    # - Verify all rats are gone
    pass


def test_multiple_decorators(temp_test_dir, clean_registry):
    """Test 5.2: Verify behavior when multiple functions are decorated."""
    # TODO: Test multiple decorated functions with different parameters
    # - Create multiple decorated functions with different parameters
    # - Call them in sequence
    # - Verify rats are created according to each function's parameters
    pass 