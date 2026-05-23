# Agent 配置

## Scanner Agent

负责扫描代码库，识别技术债。

```yaml
agents:
  - name: "scanner_agent"
    type: "openclaw"
    model:
      provider: "openai"
      model: "gpt-4o"
      temperature: 0.2
      max_tokens: 8000
    system_prompt: |
      你是代码扫描专家。职责：
      1. 识别圈复杂度超标的方法
      2. 检测重复代码块
      3. 查找过时的 API 调用
      4. 生成技术债报告
    tools:
      - name: "代码分析"
        type: "python"
      - name: "复杂度计算"
        type: "python"
    knowledge_base:
      - "scanner"
    access:
      write_workspaces: ["scanner"]
      read_workspaces: ["scanner", "refactor"]
```

## Refactor Agent

负责生成重构代码。

```yaml
agents:
  - name: "refactor_agent"
    type: "openclaw"
    model:
      provider: "deepseek"
      model: "deepseek-coder-v2"
      temperature: 0.1
      max_tokens: 16000
    system_prompt: |
      你是代码重构专家。职责：
      1. 根据扫描结果生成重构代码
      2. 遵循编码规范
      3. 保持功能不变
      4. 生成单元测试
    tools:
      - name: "代码生成"
        type: "python"
      - name: "测试生成"
        type: "python"
    knowledge_base:
      - "refactor"
    access:
      write_workspaces: ["refactor"]
      read_workspaces: ["refactor", "scanner", "reviewer"]
```

## Reviewer Agent

负责代码审查。

```yaml
agents:
  - name: "reviewer_agent"
    type: "openclaw"
    model:
      provider: "anthropic"
      model: "claude-sonnet-4"
      temperature: 0.1
      max_tokens: 12000
    system_prompt: |
      你是代码审查专家。职责：
      1. 检查代码风格
      2. 识别潜在缺陷
      3. 评估性能影响
      4. 给出改进建议
    tools:
      - name: "代码审查"
        type: "python"
      - name: "风格检查"
        type: "python"
    knowledge_base:
      - "reviewer"
    access:
      write_workspaces: ["reviewer"]
      read_workspaces: ["refactor", "scanner"]
```

## 协同工作流

通过 Hermes 协调框架，3 个 Agent 并行工作：

1. **Scanner Agent** 扫描代码库
2. **Refactor Agent** 生成重构代码
3. **Reviewer Agent** 审查重构结果
4. 自动运行测试
5. 测试通过则合并 PR，失败则回滚