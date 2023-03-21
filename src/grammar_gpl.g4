grammar grammar_gpl;

// Tokens
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LBRACK : '[' ;
RBRACK : ']' ;
COMMA : ',' ;
SEMI : ';' ;
ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;
MOD : '%' ;
EQ : '==' ;
NE : '!=' ;
LT : '<' ;
LE : '<=' ;
GT : '>' ;
GE : '>=' ;
LAND : '&&' ;
LOR : '||' ;
LNOT : '!' ;
ASSIGN : '=' ;
QUESTION : '?' ;
COLON : ':' ;
DOT : '.' ;
ELLIPSIS : '...' ;
ARROW : '->' ;
BIT_OR : '|';
BIT_XOR : '^';
BIT_AND : '&';
BIT_SHL : '<<';
BIT_SHR : '>>';
BIT_NOT : '~';

// Rules
program : statement* EOF ;
statement : expression SEMI
          | variableDeclaration
          | ifStatement
          | whileStatement
          | forStatement
          | functionDeclaration
          | returnStatement
          ;
expression : assignmentExpression ;
assignmentExpression : ternaryExpression (ASSIGN ternaryExpression)* ;
ternaryExpression : logicalOrExpression (QUESTION expression COLON expression)? ;
logicalOrExpression : logicalAndExpression (LOR logicalAndExpression)* ;
logicalAndExpression : bitwiseOrExpression (LAND bitwiseOrExpression)* ;
bitwiseOrExpression : bitwiseXorExpression (BIT_OR bitwiseXorExpression)* ;
bitwiseXorExpression : bitwiseAndExpression (BIT_XOR bitwiseAndExpression)* ;
bitwiseAndExpression : equalityExpression (BIT_AND equalityExpression)* ;
equalityExpression : relationalExpression ((EQ | NE) relationalExpression)* ;
relationalExpression : shiftExpression ((LT | LE | GT | GE) shiftExpression)* ;
shiftExpression : additiveExpression ((BIT_SHL | BIT_SHR) additiveExpression)* ;
additiveExpression : multiplicativeExpression ((ADD | SUB) multiplicativeExpression)* ;
multiplicativeExpression : unaryExpression ((MUL | DIV | MOD) unaryExpression)* ;
arrayExpression: LBRACK expressionList? RBRACK;
objectExpression: LBRACE objectPairList? RBRACE;
objectPairList: objectPair (',' objectPair)*;
objectPair: IDENTIFIER ':' expression;
expressionList: expression (',' expression)*;
unaryExpression : (ADD | SUB | LNOT | BIT_NOT) unaryExpression
                 | primaryExpression ;
primaryExpression : literal
                   | identifier
                   | LPAREN expression RPAREN
                   | arrayExpression
                   | objectExpression
                   | functionExpression
                   ;
literal : numericLiteral
        | stringLiteral
        | booleanLiteral
        ;
numericLiteral : INT | FLOAT ;
stringLiteral : STRING ;
booleanLiteral : 'true' | 'false' ;
identifier : IDENTIFIER ;
arguments : LPAREN (expression (COMMA expression)*)? RPAREN ;
memberExpression : primaryExpression (DOT identifier | LBRACK expression RBRACK)* ;
functionDeclaration : 'function' identifier LPAREN (identifier (COMMA identifier)*)? RPAREN blockStatement ;
functionExpression : 'function' LPAREN (identifier (COMMA identifier)*)? RPAREN blockStatement ;
variableDeclaration : 'var' identifier (ASSIGN expression)? SEMI ;
ifStatement : 'if' LPAREN expression RPAREN blockStatement ('else' blockStatement)? ;
whileStatement : 'while' LPAREN expression RPAREN blockStatement ;
forStatement : 'for' LPAREN (variableDeclaration | expression)? SEMI expression SEMI expression RPAREN blockStatement ;
returnStatement : 'return' expression? SEMI ;
blockStatement : LBRACE statement* RBRACE ;

// Lexer rules
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]* '.' [0-9]+;
STRING : '"' (ESC | ~["\\])* '"' ;
ESC : '\\' ["\\/bfnrt] ;
WS: [ \t\n\r]+ -> skip;
