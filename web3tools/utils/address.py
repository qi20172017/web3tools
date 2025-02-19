"""Ethereum address utilities."""

from eth_utils import is_address, to_checksum_address


def validate_address(address: str) -> bool:
    """Validate an Ethereum address.

    Args:
        address: The address to validate

    Returns:
        bool: True if the address is valid
    """
    return is_address(address)


def to_valid_address(address: str) -> str:
    """Convert an address to checksum format.

    Args:
        address: The address to convert

    Returns:
        str: The checksum address
    """
    return to_checksum_address(address)
