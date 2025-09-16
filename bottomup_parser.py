# bottomup_parser.py

class Node:
    """Represents a node in the parse tree."""
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        return f"Node({self.type}, value={self.value})"

class BottomUpParser:
    """
    Bottom-up (shift-reduce) parser for the grammar:

    E  -> E + T | E - T | T
    T  -> T * F | T / F | F
    F  -> ( E ) | NUMBER
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.stack = []  # holds tokens and partially reduced Nodes

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def shift(self):
        token = self.current_token()
        if token:
            self.stack.append(token)
            self.pos += 1

    def reduce(self):
        """Try reducing the stack according to grammar rules."""
        changed = True
        while changed:
            changed = False

            # F -> NUMBER
            if len(self.stack) >= 1 and isinstance(self.stack[-1], dict) and self.stack[-1]['kind'] == 'NUMBER':
                tok = self.stack.pop()
                self.stack.append(Node("NUMBER", value=tok['value']))
                changed = True

            # F -> ( E )
            elif len(self.stack) >= 3 and isinstance(self.stack[-3], dict) and \
                 self.stack[-3]['kind'] == 'LPAREN' and isinstance(self.stack[-2], Node) and \
                 isinstance(self.stack[-1], dict) and self.stack[-1]['kind'] == 'RPAREN':
                self.stack.pop()   # RPAREN
                expr = self.stack.pop()
                self.stack.pop()   # LPAREN
                self.stack.append(Node("F", children=[expr]))
                changed = True

            # T -> T * F | T / F
            elif len(self.stack) >= 3 and isinstance(self.stack[-3], Node) and \
                 isinstance(self.stack[-2], dict) and self.stack[-2]['kind'] in ("MULTIPLY", "DIVIDE") and \
                 isinstance(self.stack[-1], Node):
                right = self.stack.pop()
                op = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Node(op['kind'], children=[left, right], value=op['value']))
                changed = True

            # T -> F
            elif len(self.stack) >= 1 and isinstance(self.stack[-1], Node) and self.stack[-1].type in ("NUMBER", "F"):
                f = self.stack.pop()
                self.stack.append(Node("T", children=[f]))
                changed = True

            # E -> E + T | E - T
            elif len(self.stack) >= 3 and isinstance(self.stack[-3], Node) and \
                 isinstance(self.stack[-2], dict) and self.stack[-2]['kind'] in ("PLUS", "MINUS") and \
                 isinstance(self.stack[-1], Node):
                right = self.stack.pop()
                op = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Node(op['kind'], children=[left, right], value=op['value']))
                changed = True

            # E -> T
            elif len(self.stack) >= 1 and isinstance(self.stack[-1], Node) and self.stack[-1].type == "T":
                t = self.stack.pop()
                self.stack.append(Node("E", children=[t]))
                changed = True

    def parse(self):
        while self.current_token() is not None:
            self.shift()
            self.reduce()
        self.reduce()

        if len(self.stack) == 1 and isinstance(self.stack[0], Node):
            return self.stack[0]
        else:
            raise RuntimeError(f"Parsing failed. Stack: {self.stack}")
