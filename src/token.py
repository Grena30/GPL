

TokenType = str


class Token:
    def __init__(self, token_type: TokenType, literal: str):
        self.type = token_type
        self.literal = literal


def New(token_type: TokenType, literal: str) -> Token:
    return Token(token_type, literal)


# Constants
ILLEGAL = "ILLEGAL"
EOF = "EOF"

# Identifiers
IDENT = "IDENT"
INT = "INT"
FLOAT = "FLOAT"
STRING = "STRING"

# Operators
ASSIGN = "="
PLUS = "+"
MINUS = "-"
BANG = "!"
ASTERISK = "*"
SLASH = "/"

LT = "<"
GT = ">"

LOE = "<="
GOE = ">="

EQ = "=="
NOT_EQ = "!="

AND = "&&"
OR = "||"

# Delimiters
COMMA = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"
LBRACKET = "["
RBRACKET = "]"

# Keywords
FUNCTION = "FUNCTION"
TRUE = "TRUE"
FALSE = "FALSE"
IF = "IF"
ELSE = "ELSE"
RETURN = "RETURN"
FOR = "FOR"

keywords = {
    "fn": FUNCTION,
    "true": TRUE,
    "false": FALSE,
    "if": IF,
    "else": ELSE,
    "return": RETURN,
    "for": FOR,
}


def GetKeywordToken(word: str) -> Token:
    if tok := keywords.get(word):
        return New(tok, word)
    return New(IDENT, word)


def LookupIdentifier(ident: str) -> TokenType:
    if tok := keywords.get(ident):
        return tok
    return IDENT
