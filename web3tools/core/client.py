"""Web3 client implementation."""

from web3 import Web3
from web3.middleware import geth_poa_middleware


class Web3Client:
    """A Web3 client wrapper for simplified blockchain interactions."""

    def __init__(self, provider_url: str):
        """Initialize the Web3 client.

        Args:
            provider_url: The URL of the Web3 provider
        """
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        # Add middleware for POA chains like BSC
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def get_balance(self, address: str) -> float:
        """Get the balance of an address in ETH.

        Args:
            address: The Ethereum address to check

        Returns:
            float: The balance in ETH
        """
        balance_wei = self.w3.eth.get_balance(address)
        return self.w3.from_wei(balance_wei, "ether")
