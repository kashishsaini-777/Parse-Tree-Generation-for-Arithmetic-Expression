# lexer.py
import re

def tokenize(text):
    """
    Performs lexical analysis on the input text to produce a stream of tokens.
    """
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or float
        ('PLUS',     r'\+'),           # Addition
        ('MINUS',    r'-'),           # Subtraction
        ('MULTIPLY', r'\*'),           # Multiplication
        ('DIVIDE',   r'/'),           # Division
        ('LPAREN',   r'\('),           # Left parenthesis
        ('RPAREN',   r'\)'),           # Right parenthesis
        ('SKIP',     r'[ \t]+'),       # Skip spaces and tabs
        ('MISMATCH', r'.'),           # Any other character
    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []
    
    for mo in re.finditer(tok_regex, text):
        kind = mo.lastgroup
        value = mo.group()
        
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Error: Unexpected character "{value}"')
        
        tokens.append({'kind': kind, 'value': value})
        
    return tokens