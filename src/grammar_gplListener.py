# Generated from D:/pythonProject/GPL\grammar_gpl.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammar_gplParser import grammar_gplParser
else:
    from grammar_gplParser import grammar_gplParser


# This class defines a complete listener for a parse tree produced by grammar_gplParser.
class grammar_gplListener(ParseTreeListener):

    # Enter a parse tree produced by grammar_gplParser#program.
    def enterProgram(self, ctx:grammar_gplParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#program.
    def exitProgram(self, ctx:grammar_gplParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#statement.
    def enterStatement(self, ctx:grammar_gplParser.StatementContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#statement.
    def exitStatement(self, ctx:grammar_gplParser.StatementContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#expression.
    def enterExpression(self, ctx:grammar_gplParser.ExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#expression.
    def exitExpression(self, ctx:grammar_gplParser.ExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:grammar_gplParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:grammar_gplParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#ternaryExpression.
    def enterTernaryExpression(self, ctx:grammar_gplParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#ternaryExpression.
    def exitTernaryExpression(self, ctx:grammar_gplParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:grammar_gplParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:grammar_gplParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:grammar_gplParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:grammar_gplParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#bitwiseOrExpression.
    def enterBitwiseOrExpression(self, ctx:grammar_gplParser.BitwiseOrExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#bitwiseOrExpression.
    def exitBitwiseOrExpression(self, ctx:grammar_gplParser.BitwiseOrExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#bitwiseXorExpression.
    def enterBitwiseXorExpression(self, ctx:grammar_gplParser.BitwiseXorExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#bitwiseXorExpression.
    def exitBitwiseXorExpression(self, ctx:grammar_gplParser.BitwiseXorExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#bitwiseAndExpression.
    def enterBitwiseAndExpression(self, ctx:grammar_gplParser.BitwiseAndExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#bitwiseAndExpression.
    def exitBitwiseAndExpression(self, ctx:grammar_gplParser.BitwiseAndExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#equalityExpression.
    def enterEqualityExpression(self, ctx:grammar_gplParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#equalityExpression.
    def exitEqualityExpression(self, ctx:grammar_gplParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#relationalExpression.
    def enterRelationalExpression(self, ctx:grammar_gplParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#relationalExpression.
    def exitRelationalExpression(self, ctx:grammar_gplParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#shiftExpression.
    def enterShiftExpression(self, ctx:grammar_gplParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#shiftExpression.
    def exitShiftExpression(self, ctx:grammar_gplParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:grammar_gplParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:grammar_gplParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:grammar_gplParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:grammar_gplParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#arrayExpression.
    def enterArrayExpression(self, ctx:grammar_gplParser.ArrayExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#arrayExpression.
    def exitArrayExpression(self, ctx:grammar_gplParser.ArrayExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#objectExpression.
    def enterObjectExpression(self, ctx:grammar_gplParser.ObjectExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#objectExpression.
    def exitObjectExpression(self, ctx:grammar_gplParser.ObjectExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#objectPairList.
    def enterObjectPairList(self, ctx:grammar_gplParser.ObjectPairListContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#objectPairList.
    def exitObjectPairList(self, ctx:grammar_gplParser.ObjectPairListContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#objectPair.
    def enterObjectPair(self, ctx:grammar_gplParser.ObjectPairContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#objectPair.
    def exitObjectPair(self, ctx:grammar_gplParser.ObjectPairContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#expressionList.
    def enterExpressionList(self, ctx:grammar_gplParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#expressionList.
    def exitExpressionList(self, ctx:grammar_gplParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#unaryExpression.
    def enterUnaryExpression(self, ctx:grammar_gplParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#unaryExpression.
    def exitUnaryExpression(self, ctx:grammar_gplParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:grammar_gplParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:grammar_gplParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#literal.
    def enterLiteral(self, ctx:grammar_gplParser.LiteralContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#literal.
    def exitLiteral(self, ctx:grammar_gplParser.LiteralContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#numericLiteral.
    def enterNumericLiteral(self, ctx:grammar_gplParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#numericLiteral.
    def exitNumericLiteral(self, ctx:grammar_gplParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#stringLiteral.
    def enterStringLiteral(self, ctx:grammar_gplParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#stringLiteral.
    def exitStringLiteral(self, ctx:grammar_gplParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:grammar_gplParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:grammar_gplParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#identifier.
    def enterIdentifier(self, ctx:grammar_gplParser.IdentifierContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#identifier.
    def exitIdentifier(self, ctx:grammar_gplParser.IdentifierContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#arguments.
    def enterArguments(self, ctx:grammar_gplParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#arguments.
    def exitArguments(self, ctx:grammar_gplParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#memberExpression.
    def enterMemberExpression(self, ctx:grammar_gplParser.MemberExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#memberExpression.
    def exitMemberExpression(self, ctx:grammar_gplParser.MemberExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:grammar_gplParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:grammar_gplParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#functionExpression.
    def enterFunctionExpression(self, ctx:grammar_gplParser.FunctionExpressionContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#functionExpression.
    def exitFunctionExpression(self, ctx:grammar_gplParser.FunctionExpressionContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:grammar_gplParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:grammar_gplParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#ifStatement.
    def enterIfStatement(self, ctx:grammar_gplParser.IfStatementContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#ifStatement.
    def exitIfStatement(self, ctx:grammar_gplParser.IfStatementContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#whileStatement.
    def enterWhileStatement(self, ctx:grammar_gplParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#whileStatement.
    def exitWhileStatement(self, ctx:grammar_gplParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#forStatement.
    def enterForStatement(self, ctx:grammar_gplParser.ForStatementContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#forStatement.
    def exitForStatement(self, ctx:grammar_gplParser.ForStatementContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#returnStatement.
    def enterReturnStatement(self, ctx:grammar_gplParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#returnStatement.
    def exitReturnStatement(self, ctx:grammar_gplParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by grammar_gplParser#blockStatement.
    def enterBlockStatement(self, ctx:grammar_gplParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by grammar_gplParser#blockStatement.
    def exitBlockStatement(self, ctx:grammar_gplParser.BlockStatementContext):
        pass



del grammar_gplParser