"""Whale address monitoring system."""

import time
from typing import Callable, Dict

from web3tools.core.client import Web3Client
from web3tools.utils.address import validate_address


class WhaleWatcher:
    """Monitor whale addresses for transactions."""

    def __init__(self, client: Web3Client):
        """Initialize the whale watcher.

        Args:
            client: Web3Client instance
        """
        self.client = client
        self.watched_addresses = set()
        self.callbacks = []

    def add_address(self, address: str) -> bool:
        """Add an address to the watch list.

        Args:
            address: Ethereum address to monitor

        Returns:
            bool: True if address was added successfully
        """
        if validate_address(address):
            self.watched_addresses.add(address.lower())
            return True
        return False

    def add_callback(self, callback: Callable[[Dict], None]) -> None:
        """Add a callback function for transaction notifications.

        Args:
            callback: Function to call when a transaction is detected
        """
        self.callbacks.append(callback)

    def start_monitoring(self, poll_interval: int = 15) -> None:
        """Start monitoring watched addresses for new transactions.

        Args:
            poll_interval: Time between checks in seconds
        """
        last_block = self.client.w3.eth.block_number

        while True:
            try:
                current_block = self.client.w3.eth.block_number
                if current_block > last_block:
                    self._check_new_blocks(last_block + 1, current_block)
                    last_block = current_block

                time.sleep(poll_interval)
            except Exception as e:
                print(f"Error during monitoring: {e}")
                time.sleep(poll_interval)

    def _check_new_blocks(self, start_block: int, end_block: int) -> None:
        """Check new blocks for transactions involving watched addresses.

        Args:
            start_block: Starting block number
            end_block: Ending block number
        """
        for block_num in range(start_block, end_block + 1):
            block = self.client.w3.eth.get_block(block_num, full_transactions=True)
            for tx in block.transactions:
                if (
                    tx["from"].lower() in self.watched_addresses
                    or tx["to"].lower() in self.watched_addresses
                ):
                    self._notify_transaction(tx)

    def _notify_transaction(self, transaction: Dict) -> None:
        """Notify all callbacks about a new transaction.

        Args:
            transaction: Transaction data
        """
        for callback in self.callbacks:
            try:
                callback(transaction)
            except Exception as e:
                print(f"Error in callback: {e}")
