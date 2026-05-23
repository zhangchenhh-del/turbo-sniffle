# Turbo Sniffle

> 基于 OpenClaw 的多 Agent 代码库自动化重构系统

## 📋 项目简介

Turbo Sniffle 是一个基于 OpenClaw 构建的多 Agent 代码库自动化重构系统，通过 Hermes 协同引擎协调多个 Agent 并行执行代码扫描、重构生成、代码审查和测试验证，实现技术债的自动化管理。

## 🚀 核心特性

- **多 Agent 协同**：Hermes 协同框架调度多个 Agent 并行工作
- **知识库隔离**：采用只写隔离、只读共享机制，避免知识库污染
- **多模型支持**：支持 GPT-4o、DeepSeek Coder V2、Claude Sonnet 4 等大模型
- **自动化重构**：自动识别技术债并生成符合规范的代码
- **测试覆盖**：自动生成单元测试和集成测试，验证重构质量

## 🏗️ 系统架构

```
┌─────────────────────────────────────────────────────┐
│                    Hermes 协同引擎                       │
├─────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌───────┐  │
│  │  Scanner Agent  │  │ Refactor Agent  │  │Reviewer│  │
│  │   (GPT-4o)      │  │(DeepSeek Coder) │  │ Agent │  │
│  └────────┬────────┘  └────────┬────────┘  └───┬───┘  │
│           │                   │                │      │
│  ┌────────┴───────────────────┴────────────────┴───┐  │
│  │            OpenClaw 知识库（分区隔离）             │  │
│  └────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

## 📊 落地成果

| 指标 | 优化前 | 优化后 | 提升 |
|------|:------:|:------:|:----:|
| 技术债密度 | 32.7 | 18.4 | ⬇️ 44% |
| 单元测试覆盖率 | 62% | 81% | ⬆️ 31% |
| 线上故障率 | 基准 | -35% | ⬇️ 35% |
| 新人上手周期 | 3个月 | 1.5个月 | ⬇️ 50% |

## 🔧 技术栈

- **框架**：OpenClaw + Hermes 协同引擎
- **向量数据库**：ChromaDB（知识库分区隔离）
- **大模型**：GPT-4o / DeepSeek Coder V2 / Claude Sonnet 4
- **存储**：Redis（Agent 记忆）+ MinIO（版本产物）
- **CI/CD**：GitLab CI + Argo Workflow

## 📦 资源消耗

| Agent | 模型 | 日均 Token | 月度 Token |
|-------|------|:----------:|:----------:|
| Scanner Agent | GPT-4o | 800 万 | 4.92 亿 |
| Refactor Agent | DeepSeek Coder V2 | 1200 万 | 7.38 亿 |
| Reviewer Agent | Claude Sonnet 4 | 600 万 | 3.69 亿 |
| **合计** | | **2600 万** | **16 亿** |

## 🛠️ 安装

```bash
# 克隆仓库
git clone https://github.com/zhangchenhh-del/turbo-sniffle.git
cd turbo-sniffle

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入你的 API Keys

# 启动服务
python main.py
```

## 📖 使用文档

详细文档请参考 [docs/](./docs/) 目录：

- [快速开始](./docs/quick-start.md)
- [Agent 配置](./docs/agent-config.md)
- [知识库管理](./docs/knowledge-base.md)
- [Hermes 协同](./docs/hermes.md)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](./LICENSE) 文件

## 🌟 Star

如果这个项目对你有帮助，请给我们一个 Star！

---

**Turbo Sniffle** © 2024-2026 张辰