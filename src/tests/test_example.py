import os
import asyncio
import pytest
from src.code.solution import example_add_two_numbers


def test_example_add_two_numbers():
    result = example_add_two_numbers(1, 2)
    assert type(result) is int
    assert result == 3


def test_success_env():
    first_value = os.environ.get("FIRST_VALUE")
    second_value = os.environ.get("SECOND_VALUE")
    assert first_value == "first"
    assert second_value == "second"

def test_github_env():
    env_value = os.environ.get("GITHUB_REPOSITORY")
    correct_value = "Daniil-Solo/CourseTaskTemplate/"
    assert env_value == correct_value, f"expected {correct_value}, got {env_value}"


async def test_success_async():
    await asyncio.sleep(0.5)
