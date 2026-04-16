# web3_python_practice
Web3 与 Python 结合的实践项目，用于学习、测试与开发区块链相关功能，包含基础链上交互、合约调用、钱包操作等常用示例。

---

## 项目介绍
本项目基于 Python 实现 Web3 领域常用功能，适合区块链入门、合约调试、开发学习使用。
- 支持主流公链/测试网连接
- 基础钱包创建、导入、签名
- 合约 ABI 调用、交易发送
- 链上数据查询、事件监听

---

## 环境准备
```bash
# 安装依赖
pip install web3 python-dotenv eth-account
```

## 配置文件
新建 `.env` 文件，填入节点与账户信息：
```env
RPC_URL=https://eth-sepolia.g.alchemy.com/v2/your-api-key
PRIVATE_KEY=your-private-key
ADDRESS=your-wallet-address
```

---

## 主要功能
1. **连接区块链节点**
2. **查询余额、区块、交易信息**
3. **创建/导入以太坊钱包**
4. **发送原生代币交易**
5. **调用 ERC20/ERC721 合约**
6. **签名消息与验签**

---

## 使用说明
1. 克隆项目
```bash
git clone https://github.com/CHENZlHAO/web3_python_practice.git
cd web3_python_practice
```
2. 配置 `.env`
3. 运行示例脚本
```bash
python demo.py
```

---

## 常见问题
- **link fetch error**：RPC 节点不可达、网络不通或 API Key 错误
- 检查 RPC_URL 是否正确、网络能否访问、节点配额是否超限

---

## 协议
MIT License
