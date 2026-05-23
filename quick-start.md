# 快速开始

## 环境准备

### 1. 安装依赖

```bash
pip install openclaw hermes chromadb redis
```

### 2. 配置 API Keys

创建 `.env` 文件：

```bash
# GPT-4o
OPENAI_API_KEY=your_openai_api_key

# DeepSeek
DEEPSEEK_API_KEY=your_deepseek_api_key

# Claude
ANTHROPIC_API_KEY=your_anthropic_api_key

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# ChromaDB
CHROMADB_HOST=localhost
CHROMADB_PORT=8000
```

## 启动 Agent

### 启动单个 Agent

```bash
python main.py --agent scanner
python main.py --agent refactor
python main.py --agent reviewer
```

### 启动所有 Agent

```bash
python main.py --all
```

## 验证安装

```bash
python -m pytest tests/
```

## 下一步

- [Agent 配置](./agent-config.md)
- [知识库管理](./knowledge-base.md)
- [Hermes 协同](./hermes.md)