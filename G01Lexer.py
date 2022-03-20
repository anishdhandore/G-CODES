# Generated from G01.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("i\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\5\16O")
        buf.write("\n\16\3\16\6\16R\n\16\r\16\16\16S\3\16\3\16\6\16X\n\16")
        buf.write("\r\16\16\16Y\5\16\\\n\16\3\17\6\17_\n\17\r\17\16\17`\3")
        buf.write("\20\6\20d\n\20\r\20\16\20e\3\20\3\20\2\2\21\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21\3\2\3\5\2\13\f\17\17\"\"\2n\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\3!\3\2\2\2\5%\3\2\2\2\7+\3\2\2\2\t/\3")
        buf.write("\2\2\2\13\62\3\2\2\2\r\66\3\2\2\2\179\3\2\2\2\21<\3\2")
        buf.write("\2\2\23?\3\2\2\2\25B\3\2\2\2\27E\3\2\2\2\31J\3\2\2\2\33")
        buf.write("N\3\2\2\2\35^\3\2\2\2\37c\3\2\2\2!\"\7I\2\2\"#\7\62\2")
        buf.write("\2#$\7\63\2\2$\4\3\2\2\2%&\7r\2\2&\'\7t\2\2\'(\7k\2\2")
        buf.write("()\7p\2\2)*\7v\2\2*\6\3\2\2\2+,\7I\2\2,-\7\64\2\2-.\7")
        buf.write(":\2\2.\b\3\2\2\2/\60\7I\2\2\60\61\7E\2\2\61\n\3\2\2\2")
        buf.write("\62\63\7I\2\2\63\64\7H\2\2\64\65\7E\2\2\65\f\3\2\2\2\66")
        buf.write("\67\7R\2\2\678\7W\2\28\16\3\2\2\29:\7R\2\2:;\7F\2\2;\20")
        buf.write("\3\2\2\2<=\7D\2\2=>\7H\2\2>\22\3\2\2\2?@\7G\2\2@A\7H\2")
        buf.write("\2A\24\3\2\2\2BC\7T\2\2CD\7V\2\2D\26\3\2\2\2EF\7U\2\2")
        buf.write("FG\7G\2\2GH\7V\2\2HI\7J\2\2I\30\3\2\2\2JK\7G\2\2KL\7V")
        buf.write("\2\2L\32\3\2\2\2MO\7/\2\2NM\3\2\2\2NO\3\2\2\2OQ\3\2\2")
        buf.write("\2PR\4\62;\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T")
        buf.write("[\3\2\2\2UW\7\60\2\2VX\4\62;\2WV\3\2\2\2XY\3\2\2\2YW\3")
        buf.write("\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[U\3\2\2\2[\\\3\2\2\2\\\34")
        buf.write("\3\2\2\2]_\4c|\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2")
        buf.write("\2a\36\3\2\2\2bd\t\2\2\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2")
        buf.write("ef\3\2\2\2fg\3\2\2\2gh\b\20\2\2h \3\2\2\2\t\2NSY[`e\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class G01Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    NUMBER = 13
    LETTER = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'G01'", "'print'", "'G28'", "'GC'", "'GFC'", "'PU'", "'PD'", 
            "'BF'", "'EF'", "'RT'", "'SETH'", "'ET'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "LETTER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "NUMBER", "LETTER", 
                  "WS" ]

    grammarFileName = "G01.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


