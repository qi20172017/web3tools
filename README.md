# Web3Tools 🌐

Web3Tools 是一个用于以太坊区块链交互的 Python 工具集，主要功能包括：
- 🔍 监控大额交易
- 🐋 识别巨鲸地址
- 📊 分析交易数据

## ✨ 功能特点

- 📡 实时监控指定地址的交易
- 🔎 分析历史交易识别巨鲸地址
- ⚙️ 支持自定义交易金额阈值
- 🔔 灵活的回调机制处理交易通知

## 🚀 快速开始

### 安装

1. 克隆仓库：
```bash
git clone https://github.com/其0172017/web3tools.git
cd web3tools
```

2. 创建虚拟环境：
```bash
conda create -n web3-env python=3.9
conda activate web3-env
```

3. 安装依赖：
```bash
pip install -e .
```

### 配置

1. 复制环境变量模板：
```bash
cp .env.example .env
```

2. 在 `.env` 文件中设置：
```bash
ETHEREUM_NETWORK=mainnet
INFURA_PROJECT_ID=your_infura_project_id
```

## 📖 使用示例

### 监控大额交易
```python
from web3tools.core.client import Web3Client
from web3tools.monitoring.whale_watcher import WhaleWatcher

# 初始化客户端
client = Web3Client("YOUR_INFURA_URL")

# 创建监控器
watcher = WhaleWatcher(client)

# 添加要监控的地址
watcher.add_address("0x742d35Cc6634C0532925a3b844Bc454e4438f44e")

# 开始监控
watcher.start_monitoring()
```

### 分析巨鲸交易
```python
from web3tools.analysis.whale_detector import WhaleDetector

# 创建检测器
detector = WhaleDetector(client, min_balance_eth=1000.0)

# 分析最近100个区块
current_block = client.w3.eth.block_number
whale_data = detector.analyze_transactions(current_block - 100, current_block)
```

更多示例请查看 [`examples`](examples/) 目录。

## 🛠️ 开发

### 环境设置

1. 安装开发依赖：
```bash
pip install -r requirements.txt
```

2. 安装 pre-commit hooks：
```bash
pre-commit install
```

### 运行测试
```bash
pytest
```

## 📚 文档

- [Web3.py 学习入门](docs/web3.py学习入门.md)
- [API 文档](docs/api.md)

## 🤝 贡献

欢迎提交 Pull Requests！

1. Fork 本仓库
2. 创建您的特性分支：
```bash
git checkout -b feature/amazing-feature
```
3. 提交您的更改：
```bash
git commit -m 'Add some amazing feature'
```
4. 推送到分支：
```bash
git push origin feature/amazing-feature
```
5. 提交 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 📮 联系方式

- 作者：Minner
- 邮箱：xiaoqideguge@gmail.com
- GitHub：[qi20172017](https://github.com/qi20172017)

---

<p align="center">
  Made with ❤️ by Minner
</p>
