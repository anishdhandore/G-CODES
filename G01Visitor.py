# Generated from G01.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .G01Parser import G01Parser
else:
    from G01Parser import G01Parser

# This class defines a complete generic visitor for a parse tree produced by G01Parser.

import turtle as tutu
tutu.bgcolor('grey')
tutu.pensize(10)
tutu.speed(3)

class G01Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by G01Parser#start.
    def visitStart(self, ctx:G01Parser.StartContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:G01Parser.DrawlineExprContext):
        target_x    = float(ctx.x_cord.text)
        target_y    = float(ctx.y_cord.text)

        tutu.goto(target_x, target_y)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#printlineExpr.
    def visitPrintlineExpr(self, ctx:G01Parser.PrintlineExprContext):
        print(ctx.x_cord.text, ctx.y_cord.text)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#drawCircle.
    def visitDrawCircle(self, ctx:G01Parser.DrawCircleContext):
        radius = float(ctx.radius.text)
        extent = float(ctx.extent.text)
        tutu.circle(radius,extent)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#specifyColor.
    def visitSpecifyColor(self, ctx:G01Parser.SpecifyColorContext):
        color = ctx.word.text
        tutu.color(color)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#specifyFillColor.
    def visitSpecifyFillColor(self, ctx:G01Parser.SpecifyFillColorContext):
        fill_color = ctx.word.text
        tutu.fillcolor(fill_color)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#PenUp.
    def visitPenUp(self, ctx:G01Parser.PenUpContext):
        tutu.pu()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#PenDown.
    def visitPenDown(self, ctx:G01Parser.PenDownContext):
        tutu.pd()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#beginFill.
    def visitBeginFill(self, ctx:G01Parser.BeginFillContext):
        tutu.begin_fill()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#endFill.
    def visitEndFill(self, ctx:G01Parser.EndFillContext):
        tutu.end_fill()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#goRight.
    def visitGoRight(self, ctx:G01Parser.GoRightContext):
        angle = float(ctx.angle.text)
        tutu.right(angle)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#setOrientation.
    def visitSetOrientation(self, ctx:G01Parser.SetOrientationContext):
        angle = float(ctx.angle.text)
        tutu.seth(angle)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by G01Parser#endTurtle.
    def visitEndTurtle(self, ctx:G01Parser.EndTurtleContext):
        tutu.done()
        return self.visitChildren(ctx)

del G01Parser