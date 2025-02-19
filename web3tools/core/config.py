"""Configuration management for web3tools."""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class for web3tools."""

    ETHEREUM_NETWORK = os.getenv("ETHEREUM_NETWORK", "mainnet")
    INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")
