from antlr4 import *
from grammar_gplLexer import grammar_gplLexer
from grammar_gplParser import grammar_gplParser

# create a stream of input characters
input_stream = InputStream("size 50")

# create a lexer that reads from the input stream
lexer = grammar_gplLexer(input_stream)

# create a stream of tokens from the lexer
token_stream = CommonTokenStream(lexer)

# create a parser that reads from the token stream
parser = grammar_gplParser(token_stream)

# parse the input and print the result
tree = parser.program()

print(tree.toStringTree(recog=parser))
print(input_stream)
print(lexer)
print(token_stream)
print(parser)
