# parser.py

# recursive descent parser for arithmetic expressions ll1

class Node:
    """Represents a node in the parse tree."""
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []

    def __repr__(self):
        return f"Node({self.type}, value={self.value})"

class Parser:
    """
    Parses a list of tokens and builds a parse tree based on a defined grammar.
    Grammar:
    E  -> T E'
    E' -> + T E' | - T E' | ε
    T  -> F T'
    T' -> * F T' | / F T' | ε
    F  -> ( E ) | number
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected_kind):
        token = self.current_token()
        if token and token['kind'] == expected_kind:
            self.pos += 1
            return token
        raise RuntimeError(f"Syntax Error: Expected {expected_kind} but got {token['kind'] if token else 'EOF'}")

    def parse_factor(self):
        """ F -> ( E ) | number """
        token = self.current_token()
        if token['kind'] == 'NUMBER':
            self.consume('NUMBER')
            return Node(type='NUMBER', value=token['value'])
        elif token['kind'] == 'LPAREN':
            self.consume('LPAREN')
            expr_node = self.parse_expression()
            self.consume('RPAREN')
            return expr_node
        else:
            raise RuntimeError(f"Syntax Error: Unexpected token {token}")

    def parse_term(self):
        """ T -> F T' """
        node = self.parse_factor()
        
        while self.current_token() and self.current_token()['kind'] in ('MULTIPLY', 'DIVIDE'):
            op_token = self.consume(self.current_token()['kind'])
            right_node = self.parse_factor()
            node = Node(type=op_token['kind'], children=[node, right_node], value=op_token['value'])
            
        return node

    def parse_expression(self):
        """ E -> T E' """
        node = self.parse_term()

        while self.current_token() and self.current_token()['kind'] in ('PLUS', 'MINUS'):
            op_token = self.consume(self.current_token()['kind'])
            right_node = self.parse_term()
            node = Node(type=op_token['kind'], children=[node, right_node], value=op_token['value'])
            
        return node

    def parse(self):
        """Starts the parsing process."""
        if not self.tokens:
            return None
        return self.parse_expression()



