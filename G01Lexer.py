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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\5\rJ\n\r\3\r\6\rM\n\r\r\r\16")
        buf.write("\rN\3\r\3\r\6\rS\n\r\r\r\16\rT\5\rW\n\r\3\16\6\16Z\n\16")
        buf.write("\r\16\16\16[\3\17\6\17_\n\17\r\17\16\17`\3\17\3\17\2\2")
        buf.write("\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\3\2\3\5\2\13\f\17\17\"\"\2i\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\3\37\3\2\2\2\5#\3\2\2\2\7)\3\2\2\2\t-\3\2\2\2")
        buf.write("\13\60\3\2\2\2\r\64\3\2\2\2\17\67\3\2\2\2\21:\3\2\2\2")
        buf.write("\23=\3\2\2\2\25@\3\2\2\2\27C\3\2\2\2\31I\3\2\2\2\33Y\3")
        buf.write("\2\2\2\35^\3\2\2\2\37 \7I\2\2 !\7\62\2\2!\"\7\63\2\2\"")
        buf.write("\4\3\2\2\2#$\7r\2\2$%\7t\2\2%&\7k\2\2&\'\7p\2\2\'(\7v")
        buf.write("\2\2(\6\3\2\2\2)*\7I\2\2*+\7\64\2\2+,\7:\2\2,\b\3\2\2")
        buf.write("\2-.\7I\2\2./\7E\2\2/\n\3\2\2\2\60\61\7I\2\2\61\62\7H")
        buf.write("\2\2\62\63\7E\2\2\63\f\3\2\2\2\64\65\7R\2\2\65\66\7W\2")
        buf.write("\2\66\16\3\2\2\2\678\7R\2\289\7F\2\29\20\3\2\2\2:;\7D")
        buf.write("\2\2;<\7H\2\2<\22\3\2\2\2=>\7G\2\2>?\7H\2\2?\24\3\2\2")
        buf.write("\2@A\7T\2\2AB\7V\2\2B\26\3\2\2\2CD\7U\2\2DE\7G\2\2EF\7")
        buf.write("V\2\2FG\7J\2\2G\30\3\2\2\2HJ\7/\2\2IH\3\2\2\2IJ\3\2\2")
        buf.write("\2JL\3\2\2\2KM\4\62;\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2N")
        buf.write("O\3\2\2\2OV\3\2\2\2PR\7\60\2\2QS\4\62;\2RQ\3\2\2\2ST\3")
        buf.write("\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2VP\3\2\2\2VW\3\2\2")
        buf.write("\2W\32\3\2\2\2XZ\4c|\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[")
        buf.write("\\\3\2\2\2\\\34\3\2\2\2]_\t\2\2\2^]\3\2\2\2_`\3\2\2\2")
        buf.write("`^\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\b\17\2\2c\36\3\2\2\2")
        buf.write("\t\2INTV[`\3\b\2\2")
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
    NUMBER = 12
    LETTER = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'G01'", "'print'", "'G28'", "'GC'", "'GFC'", "'PU'", "'PD'", 
            "'BF'", "'EF'", "'RT'", "'SETH'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "LETTER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "NUMBER", "LETTER", "WS" ]

    grammarFileName = "G01.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


