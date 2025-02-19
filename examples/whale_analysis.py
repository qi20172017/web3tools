"""Example of whale address detection and monitoring."""

from web3 import Web3

from web3tools.analysis.whale_detector import WhaleDetector
from web3tools.core.client import Web3Client
from web3tools.core.config import Config
from web3tools.monitoring.whale_watcher import WhaleWatcher


def transaction_callback(tx):
    """Handle new whale transactions."""
    value_eth = Web3.from_wei(tx["value"], "ether")
    print("Whale Transaction Detected!")
    print(f"From: {tx['from']}")
    print(f"To: {tx['to']}")
    print(f"Value: {value_eth} ETH")
    print("-------------------")


def main():
    """Run whale detection and monitoring example."""
    # Initialize client with Infura
    client = Web3Client(f"https://mainnet.infura.io/v3/{Config.INFURA_PROJECT_ID}")

    # Create whale detector
    detector = WhaleDetector(client, min_balance_eth=1000.0)

    # Analyze recent transactions
    current_block = client.w3.eth.block_number
    start_block = current_block - 100  # analyze last 100 blocks
    whale_data = detector.analyze_transactions(start_block, current_block)

    # Print found whale addresses
    print("Found Whale Transactions:")
    for data in whale_data:
        print(f"Address: {data['address']}")
        print(f"Transaction Count: {data['tx_count']}")
        print(f"Total Value: {data['total_value']} ETH")
        print("-------------------")

    # Start monitoring whale addresses
    watcher = WhaleWatcher(client)
    for data in whale_data:
        watcher.add_address(data["address"])

    watcher.add_callback(transaction_callback)
    print("Starting whale address monitoring...")
    watcher.start_monitoring()


if __name__ == "__main__":
    main()
