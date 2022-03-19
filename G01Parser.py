# Generated from G01.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("\"\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3 \n\3\3\3\2\2\4\2\4\2\2\2*\2\b\3\2\2\2")
        buf.write("\4\37\3\2\2\2\6\t\5\4\3\2\7\t\3\2\2\2\b\6\3\2\2\2\b\7")
        buf.write("\3\2\2\2\t\3\3\2\2\2\n\13\7\3\2\2\13\f\7\16\2\2\f \7\16")
        buf.write("\2\2\r\16\7\4\2\2\16\17\7\16\2\2\17 \7\16\2\2\20\21\7")
        buf.write("\5\2\2\21\22\7\16\2\2\22 \7\16\2\2\23\24\7\6\2\2\24 \7")
        buf.write("\17\2\2\25\26\7\7\2\2\26 \7\17\2\2\27 \7\b\2\2\30 \7\t")
        buf.write("\2\2\31 \7\n\2\2\32 \7\13\2\2\33\34\7\f\2\2\34 \7\16\2")
        buf.write("\2\35\36\7\r\2\2\36 \7\16\2\2\37\n\3\2\2\2\37\r\3\2\2")
        buf.write("\2\37\20\3\2\2\2\37\23\3\2\2\2\37\25\3\2\2\2\37\27\3\2")
        buf.write("\2\2\37\30\3\2\2\2\37\31\3\2\2\2\37\32\3\2\2\2\37\33\3")
        buf.write("\2\2\2\37\35\3\2\2\2 \5\3\2\2\2\4\b\37")
        return buf.getvalue()


class G01Parser ( Parser ):

    grammarFileName = "G01.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'G01'", "'print'", "'G28'", "'GC'", "'GFC'", 
                     "'PU'", "'PD'", "'BF'", "'EF'", "'RT'", "'SETH'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "LETTER", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    NUMBER=12
    LETTER=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(G01Parser.ExprContext,0)


        def getRuleIndex(self):
            return G01Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = G01Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [G01Parser.T__0, G01Parser.T__1, G01Parser.T__2, G01Parser.T__3, G01Parser.T__4, G01Parser.T__5, G01Parser.T__6, G01Parser.T__7, G01Parser.T__8, G01Parser.T__9, G01Parser.T__10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [G01Parser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return G01Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SetOrientationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.angle = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(G01Parser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetOrientation" ):
                listener.enterSetOrientation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetOrientation" ):
                listener.exitSetOrientation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetOrientation" ):
                return visitor.visitSetOrientation(self)
            else:
                return visitor.visitChildren(self)


    class PenDownContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPenDown" ):
                listener.enterPenDown(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPenDown" ):
                listener.exitPenDown(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPenDown" ):
                return visitor.visitPenDown(self)
            else:
                return visitor.visitChildren(self)


    class PenUpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPenUp" ):
                listener.enterPenUp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPenUp" ):
                listener.exitPenUp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPenUp" ):
                return visitor.visitPenUp(self)
            else:
                return visitor.visitChildren(self)


    class SpecifyColorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.word = None # Token
            self.copyFrom(ctx)

        def LETTER(self):
            return self.getToken(G01Parser.LETTER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecifyColor" ):
                listener.enterSpecifyColor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecifyColor" ):
                listener.exitSpecifyColor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecifyColor" ):
                return visitor.visitSpecifyColor(self)
            else:
                return visitor.visitChildren(self)


    class EndFillContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndFill" ):
                listener.enterEndFill(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndFill" ):
                listener.exitEndFill(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndFill" ):
                return visitor.visitEndFill(self)
            else:
                return visitor.visitChildren(self)


    class GoRightContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.angle = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(G01Parser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoRight" ):
                listener.enterGoRight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoRight" ):
                listener.exitGoRight(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoRight" ):
                return visitor.visitGoRight(self)
            else:
                return visitor.visitChildren(self)


    class DrawCircleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.radius = None # Token
            self.extent = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(G01Parser.NUMBER)
            else:
                return self.getToken(G01Parser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawCircle" ):
                listener.enterDrawCircle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawCircle" ):
                listener.exitDrawCircle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawCircle" ):
                return visitor.visitDrawCircle(self)
            else:
                return visitor.visitChildren(self)


    class PrintlineExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(G01Parser.NUMBER)
            else:
                return self.getToken(G01Parser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintlineExpr" ):
                listener.enterPrintlineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintlineExpr" ):
                listener.exitPrintlineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintlineExpr" ):
                return visitor.visitPrintlineExpr(self)
            else:
                return visitor.visitChildren(self)


    class SpecifyFillColorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.word = None # Token
            self.copyFrom(ctx)

        def LETTER(self):
            return self.getToken(G01Parser.LETTER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecifyFillColor" ):
                listener.enterSpecifyFillColor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecifyFillColor" ):
                listener.exitSpecifyFillColor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecifyFillColor" ):
                return visitor.visitSpecifyFillColor(self)
            else:
                return visitor.visitChildren(self)


    class BeginFillContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeginFill" ):
                listener.enterBeginFill(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeginFill" ):
                listener.exitBeginFill(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBeginFill" ):
                return visitor.visitBeginFill(self)
            else:
                return visitor.visitChildren(self)


    class DrawlineExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(G01Parser.NUMBER)
            else:
                return self.getToken(G01Parser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawlineExpr" ):
                listener.enterDrawlineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawlineExpr" ):
                listener.exitDrawlineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawlineExpr" ):
                return visitor.visitDrawlineExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = G01Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [G01Parser.T__0]:
                localctx = G01Parser.DrawlineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(G01Parser.T__0)
                self.state = 9
                localctx.x_cord = self.match(G01Parser.NUMBER)
                self.state = 10
                localctx.y_cord = self.match(G01Parser.NUMBER)
                pass
            elif token in [G01Parser.T__1]:
                localctx = G01Parser.PrintlineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(G01Parser.T__1)
                self.state = 12
                localctx.x_cord = self.match(G01Parser.NUMBER)
                self.state = 13
                localctx.y_cord = self.match(G01Parser.NUMBER)
                pass
            elif token in [G01Parser.T__2]:
                localctx = G01Parser.DrawCircleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(G01Parser.T__2)
                self.state = 15
                localctx.radius = self.match(G01Parser.NUMBER)
                self.state = 16
                localctx.extent = self.match(G01Parser.NUMBER)
                pass
            elif token in [G01Parser.T__3]:
                localctx = G01Parser.SpecifyColorContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.match(G01Parser.T__3)
                self.state = 18
                localctx.word = self.match(G01Parser.LETTER)
                pass
            elif token in [G01Parser.T__4]:
                localctx = G01Parser.SpecifyFillColorContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 19
                self.match(G01Parser.T__4)
                self.state = 20
                localctx.word = self.match(G01Parser.LETTER)
                pass
            elif token in [G01Parser.T__5]:
                localctx = G01Parser.PenUpContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 21
                self.match(G01Parser.T__5)
                pass
            elif token in [G01Parser.T__6]:
                localctx = G01Parser.PenDownContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 22
                self.match(G01Parser.T__6)
                pass
            elif token in [G01Parser.T__7]:
                localctx = G01Parser.BeginFillContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 23
                self.match(G01Parser.T__7)
                pass
            elif token in [G01Parser.T__8]:
                localctx = G01Parser.EndFillContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 24
                self.match(G01Parser.T__8)
                pass
            elif token in [G01Parser.T__9]:
                localctx = G01Parser.GoRightContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 25
                self.match(G01Parser.T__9)
                self.state = 26
                localctx.angle = self.match(G01Parser.NUMBER)
                pass
            elif token in [G01Parser.T__10]:
                localctx = G01Parser.SetOrientationContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 27
                self.match(G01Parser.T__10)
                self.state = 28
                localctx.angle = self.match(G01Parser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





