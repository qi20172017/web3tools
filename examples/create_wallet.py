"""Create a new Ethereum wallet for testing."""

import secrets

from eth_account import Account


def create_wallet():
    """Generate a new Ethereum wallet."""
    # 生成一个安全的随机私钥
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    account = Account.from_key(private_key)

    print("新钱包创建成功！")
    print(f"地址: {account.address}")
    print(f"私钥: {private_key}")
    print("\n重要提示：")
    print("1. 请保存好这个私钥，丢失将无法找回")
    print("2. 不要向这个钱包转入大量资产")
    print("3. 仅用于测试目的")

    return account.address, private_key


if __name__ == "__main__":
    address, key = create_wallet()
