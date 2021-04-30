# Generated from gsl/grammar/G4Visitor.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .G4VisitorParser import G4VisitorParser
else:
    from G4VisitorParser import G4VisitorParser

# This class defines a complete generic visitor for a parse tree produced by G4VisitorParser.

class G4VisitorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by G4VisitorParser#visitor.
    def visitVisitor(self, ctx:G4VisitorParser.VisitorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#visitorRule.
    def visitVisitorRule(self, ctx:G4VisitorParser.VisitorRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#exprBody.
    def visitExprBody(self, ctx:G4VisitorParser.ExprBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#objectBody.
    def visitObjectBody(self, ctx:G4VisitorParser.ObjectBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#listBody.
    def visitListBody(self, ctx:G4VisitorParser.ListBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#dictBody.
    def visitDictBody(self, ctx:G4VisitorParser.DictBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#objectParam.
    def visitObjectParam(self, ctx:G4VisitorParser.ObjectParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#listItem.
    def visitListItem(self, ctx:G4VisitorParser.ListItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#dictItem.
    def visitDictItem(self, ctx:G4VisitorParser.DictItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#ruleExpr.
    def visitRuleExpr(self, ctx:G4VisitorParser.RuleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#tokenExpr.
    def visitTokenExpr(self, ctx:G4VisitorParser.TokenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#refExpr.
    def visitRefExpr(self, ctx:G4VisitorParser.RefExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#lcName.
    def visitLcName(self, ctx:G4VisitorParser.LcNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#ucName.
    def visitUcName(self, ctx:G4VisitorParser.UcNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#identifier.
    def visitIdentifier(self, ctx:G4VisitorParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#ruleName.
    def visitRuleName(self, ctx:G4VisitorParser.RuleNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#tokenName.
    def visitTokenName(self, ctx:G4VisitorParser.TokenNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4VisitorParser#attributeRef.
    def visitAttributeRef(self, ctx:G4VisitorParser.AttributeRefContext):
        return self.visitChildren(ctx)



del G4VisitorParser