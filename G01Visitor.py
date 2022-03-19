# Generated from G01.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .G01Parser import G01Parser
else:
    from G01Parser import G01Parser

# This class defines a complete generic visitor for a parse tree produced by G01Parser.

import turtle as t
# tutu = turtle.Turtle()
t.title("Sasuke Mangekyou Sharingan")
t.bgcolor('#bf0404')
t.pensize(10)
t.speed(5)

class G01Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by G01Parser#start.
    def visitStart(self, ctx:G01Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:G01Parser.DrawlineExprContext):
        target_x = float(ctx.x_cord.text)
        target_y = float(ctx.y_cord.text)
        t.goto(target_x, target_y)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#printlineExpr.
    def visitPrintlineExpr(self, ctx:G01Parser.PrintlineExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#drawCircle.
    def visitDrawCircle(self, ctx:G01Parser.DrawCircleContext):
        radius = float(ctx.radius.text)
        extent = float(ctx.extent.text)
        t.circle(radius, extent)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#specifyColor.
    def visitSpecifyColor(self, ctx:G01Parser.SpecifyColorContext):
        color = ctx.word.text
        t.color(color)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#specifyFillColor.
    def visitSpecifyFillColor(self, ctx:G01Parser.SpecifyFillColorContext):
        fillColor = ctx.word.text
        t.fillcolor(fillColor)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#PenUp.
    def visitPenUp(self, ctx:G01Parser.PenUpContext):
        t.pu()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#PenDown.
    def visitPenDown(self, ctx:G01Parser.PenDownContext):
        t.pd()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#beginFill.
    def visitBeginFill(self, ctx:G01Parser.BeginFillContext):
        t.begin_fill()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#endFill.
    def visitEndFill(self, ctx:G01Parser.EndFillContext):
        t.end_fill()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#goRight.
    def visitGoRight(self, ctx:G01Parser.GoRightContext):
        angle = float(ctx.angle.text)
        t.right(angle)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G01Parser#setOrientation.
    def visitSetOrientation(self, ctx:G01Parser.SetOrientationContext):
        orientAngle = float(ctx.angle.text)
        t.seth(orientAngle)
        return self.visitChildren(ctx)

del G01Parser