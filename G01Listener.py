# Generated from G01.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .G01Parser import G01Parser
else:
    from G01Parser import G01Parser

# This class defines a complete listener for a parse tree produced by G01Parser.
class G01Listener(ParseTreeListener):

    # Enter a parse tree produced by G01Parser#start.
    def enterStart(self, ctx:G01Parser.StartContext):
        pass

    # Exit a parse tree produced by G01Parser#start.
    def exitStart(self, ctx:G01Parser.StartContext):
        pass


    # Enter a parse tree produced by G01Parser#drawlineExpr.
    def enterDrawlineExpr(self, ctx:G01Parser.DrawlineExprContext):
        pass

    # Exit a parse tree produced by G01Parser#drawlineExpr.
    def exitDrawlineExpr(self, ctx:G01Parser.DrawlineExprContext):
        pass


    # Enter a parse tree produced by G01Parser#printlineExpr.
    def enterPrintlineExpr(self, ctx:G01Parser.PrintlineExprContext):
        pass

    # Exit a parse tree produced by G01Parser#printlineExpr.
    def exitPrintlineExpr(self, ctx:G01Parser.PrintlineExprContext):
        pass


    # Enter a parse tree produced by G01Parser#drawCircle.
    def enterDrawCircle(self, ctx:G01Parser.DrawCircleContext):
        pass

    # Exit a parse tree produced by G01Parser#drawCircle.
    def exitDrawCircle(self, ctx:G01Parser.DrawCircleContext):
        pass


    # Enter a parse tree produced by G01Parser#specifyColor.
    def enterSpecifyColor(self, ctx:G01Parser.SpecifyColorContext):
        pass

    # Exit a parse tree produced by G01Parser#specifyColor.
    def exitSpecifyColor(self, ctx:G01Parser.SpecifyColorContext):
        pass


    # Enter a parse tree produced by G01Parser#specifyFillColor.
    def enterSpecifyFillColor(self, ctx:G01Parser.SpecifyFillColorContext):
        pass

    # Exit a parse tree produced by G01Parser#specifyFillColor.
    def exitSpecifyFillColor(self, ctx:G01Parser.SpecifyFillColorContext):
        pass


    # Enter a parse tree produced by G01Parser#PenUp.
    def enterPenUp(self, ctx:G01Parser.PenUpContext):
        pass

    # Exit a parse tree produced by G01Parser#PenUp.
    def exitPenUp(self, ctx:G01Parser.PenUpContext):
        pass


    # Enter a parse tree produced by G01Parser#PenDown.
    def enterPenDown(self, ctx:G01Parser.PenDownContext):
        pass

    # Exit a parse tree produced by G01Parser#PenDown.
    def exitPenDown(self, ctx:G01Parser.PenDownContext):
        pass


    # Enter a parse tree produced by G01Parser#beginFill.
    def enterBeginFill(self, ctx:G01Parser.BeginFillContext):
        pass

    # Exit a parse tree produced by G01Parser#beginFill.
    def exitBeginFill(self, ctx:G01Parser.BeginFillContext):
        pass


    # Enter a parse tree produced by G01Parser#endFill.
    def enterEndFill(self, ctx:G01Parser.EndFillContext):
        pass

    # Exit a parse tree produced by G01Parser#endFill.
    def exitEndFill(self, ctx:G01Parser.EndFillContext):
        pass


    # Enter a parse tree produced by G01Parser#goRight.
    def enterGoRight(self, ctx:G01Parser.GoRightContext):
        pass

    # Exit a parse tree produced by G01Parser#goRight.
    def exitGoRight(self, ctx:G01Parser.GoRightContext):
        pass


    # Enter a parse tree produced by G01Parser#setOrientation.
    def enterSetOrientation(self, ctx:G01Parser.SetOrientationContext):
        pass

    # Exit a parse tree produced by G01Parser#setOrientation.
    def exitSetOrientation(self, ctx:G01Parser.SetOrientationContext):
        pass



del G01Parser