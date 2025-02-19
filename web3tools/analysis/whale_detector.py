"""Whale address detection and analysis."""

from typing import Dict, List, Optional

from web3tools.core.client import Web3Client


class WhaleDetector:
    """Detector class for identifying and analyzing whale addresses."""

    def __init__(self, client: Web3Client, min_balance_eth: float = 1000.0):
        """Initialize the whale detector.

        Args:
            client: Web3Client instance
            min_balance_eth: Minimum balance in ETH to be considered a whale
        """
        self.client = client
        self.min_balance_wei = client.w3.to_wei(min_balance_eth, "ether")

    def analyze_transactions(
        self, start_block: int, end_block: Optional[int] = None
    ) -> List[Dict]:
        """Analyze transactions within block range to identify whale addresses.

        Args:
            start_block: Starting block number
            end_block: Ending block number (defaults to latest)

        Returns:
            List of whale addresses with their transaction data
        """
        if end_block is None:
            end_block = self.client.w3.eth.block_number

        whale_data = []
        for block_num in range(start_block, end_block + 1):
            block = self.client.w3.eth.get_block(block_num, full_transactions=True)
            for tx in block.transactions:
                if self._is_whale_transaction(tx):
                    whale_data.append(self._process_transaction(tx))

        return whale_data

    def _is_whale_transaction(self, tx: Dict) -> bool:
        """Check if a transaction involves a whale address.

        Args:
            tx: Transaction data

        Returns:
            bool: True if transaction value exceeds whale threshold
        """
        return tx.value >= self.min_balance_wei

    def _process_transaction(self, tx: Dict) -> Dict:
        """Process a whale transaction and extract relevant data.

        Args:
            tx: Transaction data

        Returns:
            Dict containing processed transaction data
        """
        value_eth = self.client.w3.from_wei(tx["value"], "ether")
        return {
            "address": tx["from"],
            "tx_hash": tx["hash"].hex(),
            "value": value_eth,
            "to": tx["to"],
            "block_number": tx["blockNumber"],
            "tx_count": 1,
            "total_value": value_eth,
        }
