"""
代码扫描器 - Scanner Agent
"""

import os
import ast
from pathlib import Path
from typing import List, Dict
import json


class CodeScanner:
    """代码扫描器"""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.issues = []

    def scan_repository(self) -> List[Dict]:
        """扫描整个代码库"""
        self.issues = []

        for py_file in self.repo_path.rglob("*.py"):
            self._scan_file(py_file)

        return self.issues

    def _scan_file(self, file_path: Path):
        """扫描单个 Python 文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()

            tree = ast.parse(code)

            # 检查圈复杂度
            complexity = self._calculate_complexity(tree)
            if complexity > 10:
                self.issues.append({
                    "type": "high_complexity",
                    "file": str(file_path),
                    "complexity": complexity,
                    "severity": "warning"
                })

        except Exception as e:
            print(f"Error scanning {file_path}: {e}")

    def _calculate_complexity(self, tree: ast.AST) -> int:
        """计算圈复杂度"""
        complexity = 1

        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.For, ast.While, ast.Try)):
                complexity += 1

        return complexity

    def generate_report(self) -> str:
        """生成扫描报告"""
        report = {
            "total_issues": len(self.issues),
            "by_type": {},
            "by_severity": {}
        }

        for issue in self.issues:
            issue_type = issue["type"]
            severity = issue["severity"]

            report["by_type"][issue_type] = report["by_type"].get(issue_type, 0) + 1
            report["by_severity"][severity] = report["by_severity"].get(severity, 0) + 1

        return json.dumps(report, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    # 示例使用
    scanner = CodeScanner("/path/to/repo")
    issues = scanner.scan_repository()

    print(f"发现 {len(issues)} 个问题")
    print(scanner.generate_report())