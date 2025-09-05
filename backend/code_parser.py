import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.functions = []
        self.classes = []
        
    def visit_FunctionDef(self, node):
        doc = ast.get_docstring(node) or ""
        args = [arg.arg for arg in node.args.args]
        body = ast.unparse(node)
        self.functions.append({
            'name': node.name,
            'docstring': doc,
            'args': args,
            'body': body
        })
        self.generic_visit(node)
        
    def visit_ClassDef(self, node):
        doc = ast.get_docstring(node) or ""
        body = ast.unparse(node)
        
        self.classes.append({
            'name': node.name,
            'docstring': doc,
            'body': body
        })
        self.generic_visit(node)

def analyse_code(filename):
    with open(filename, 'r') as file:
        tree = ast.parse(file.read())

    analyser = CodeAnalyzer()
    analyser.visit(tree)

    return analyser.functions, analyser.classes

