"""Pytest configuration file."""

import pytest

from web3tools.core.client import Web3Client


@pytest.fixture
def web3_client():
    """Create a Web3Client instance for testing."""
    return Web3Client("https://mainnet.infura.io/v3/your-project-id")
