# Generated from D:/pythonProject/GPL\grammar_gpl.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammar_gplParser import grammar_gplParser
else:
    from grammar_gplParser import grammar_gplParser


# This class defines a complete generic visitor for a parse tree produced by grammar_gplParser.

class grammar_gplVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammar_gplParser#program.
    def visitProgram(self, ctx:grammar_gplParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#statement.
    def visitStatement(self, ctx:grammar_gplParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#expression.
    def visitExpression(self, ctx:grammar_gplParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:grammar_gplParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#ternaryExpression.
    def visitTernaryExpression(self, ctx:grammar_gplParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:grammar_gplParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:grammar_gplParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#bitwiseOrExpression.
    def visitBitwiseOrExpression(self, ctx:grammar_gplParser.BitwiseOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#bitwiseXorExpression.
    def visitBitwiseXorExpression(self, ctx:grammar_gplParser.BitwiseXorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#bitwiseAndExpression.
    def visitBitwiseAndExpression(self, ctx:grammar_gplParser.BitwiseAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#equalityExpression.
    def visitEqualityExpression(self, ctx:grammar_gplParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#relationalExpression.
    def visitRelationalExpression(self, ctx:grammar_gplParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#shiftExpression.
    def visitShiftExpression(self, ctx:grammar_gplParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:grammar_gplParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:grammar_gplParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#arrayExpression.
    def visitArrayExpression(self, ctx:grammar_gplParser.ArrayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#objectExpression.
    def visitObjectExpression(self, ctx:grammar_gplParser.ObjectExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#objectPairList.
    def visitObjectPairList(self, ctx:grammar_gplParser.ObjectPairListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#objectPair.
    def visitObjectPair(self, ctx:grammar_gplParser.ObjectPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#expressionList.
    def visitExpressionList(self, ctx:grammar_gplParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#unaryExpression.
    def visitUnaryExpression(self, ctx:grammar_gplParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:grammar_gplParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#literal.
    def visitLiteral(self, ctx:grammar_gplParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#numericLiteral.
    def visitNumericLiteral(self, ctx:grammar_gplParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#stringLiteral.
    def visitStringLiteral(self, ctx:grammar_gplParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:grammar_gplParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#identifier.
    def visitIdentifier(self, ctx:grammar_gplParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#arguments.
    def visitArguments(self, ctx:grammar_gplParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#memberExpression.
    def visitMemberExpression(self, ctx:grammar_gplParser.MemberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:grammar_gplParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#functionExpression.
    def visitFunctionExpression(self, ctx:grammar_gplParser.FunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:grammar_gplParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#ifStatement.
    def visitIfStatement(self, ctx:grammar_gplParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#whileStatement.
    def visitWhileStatement(self, ctx:grammar_gplParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#forStatement.
    def visitForStatement(self, ctx:grammar_gplParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#returnStatement.
    def visitReturnStatement(self, ctx:grammar_gplParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_gplParser#blockStatement.
    def visitBlockStatement(self, ctx:grammar_gplParser.BlockStatementContext):
        return self.visitChildren(ctx)



del grammar_gplParser