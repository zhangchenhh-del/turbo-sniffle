"""
示例代码：圈复杂度检测
"""

def calculate_cyclomatic_complexity(func):
    """
    计算函数的圈复杂度

    Args:
        func: 函数对象

    Returns:
        int: 圈复杂度
    """
    import ast

    class ComplexityVisitor(ast.NodeVisitor):
        def __init__(self):
            self.complexity = 1

        def visit_If(self, node):
            self.complexity += 1
            self.generic_visit(node)

        def visit_For(self, node):
            self.complexity += 1
            self.generic_visit(node)

        def visit_While(self, node):
            self.complexity += 1
            self.generic_visit(node)

        def visit_Try(self, node):
            self.complexity += 1
            self.generic_visit(node)

    tree = ast.parse(func.__code__.co_code)
    visitor = ComplexityVisitor()
    visitor.visit(tree)

    return visitor.complexity


if __name__ == "__main__":
    # 示例函数
    def example_function(x):
        if x > 0:
            for i in range(10):
                if i % 2 == 0:
                    return i * 2
        else:
            while x < 100:
                x += 1
                if x == 50:
                    break
        return x

    complexity = calculate_cyclomatic_complexity(example_function)
    print(f"圈复杂度: {complexity}")