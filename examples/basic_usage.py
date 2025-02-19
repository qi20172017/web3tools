"""Basic usage examples for web3tools."""

from web3tools.core.client import Web3Client
from web3tools.utils.address import validate_address


def main():
    """Demonstrate basic usage of web3tools."""
    # Initialize client
    client = Web3Client("https://mainnet.infura.io/v3/your-project-id")

    # Example address
    address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

    # Validate address
    if validate_address(address):
        # Get balance
        balance = client.get_balance(address)
        print(f"Balance of {address}: {balance} ETH")


if __name__ == "__main__":
    main()
