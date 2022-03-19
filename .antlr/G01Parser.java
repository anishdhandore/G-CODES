// Generated from /Users/anishdhandore/Documents/Projects/G CODES/G01.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class G01Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, NUMBER=12, LETTER=13, WS=14;
	public static final int
		RULE_start = 0, RULE_expr = 1;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'G01'", "'print'", "'G28'", "'GC'", "'GFC'", "'PU'", "'PD'", "'BF'", 
			"'EF'", "'RT'", "'SETH'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"NUMBER", "LETTER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "G01.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public G01Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		try {
			setState(6);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__5:
			case T__6:
			case T__7:
			case T__8:
			case T__9:
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(4);
				expr();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SetOrientationContext extends ExprContext {
		public Token angle;
		public TerminalNode NUMBER() { return getToken(G01Parser.NUMBER, 0); }
		public SetOrientationContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class PenDownContext extends ExprContext {
		public PenDownContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class PenUpContext extends ExprContext {
		public PenUpContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class SpecifyColorContext extends ExprContext {
		public Token word;
		public TerminalNode LETTER() { return getToken(G01Parser.LETTER, 0); }
		public SpecifyColorContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class EndFillContext extends ExprContext {
		public EndFillContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class GoRightContext extends ExprContext {
		public Token angle;
		public TerminalNode NUMBER() { return getToken(G01Parser.NUMBER, 0); }
		public GoRightContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class DrawCircleContext extends ExprContext {
		public Token radius;
		public Token extent;
		public List<TerminalNode> NUMBER() { return getTokens(G01Parser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(G01Parser.NUMBER, i);
		}
		public DrawCircleContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class PrintlineExprContext extends ExprContext {
		public Token x_cord;
		public Token y_cord;
		public List<TerminalNode> NUMBER() { return getTokens(G01Parser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(G01Parser.NUMBER, i);
		}
		public PrintlineExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class SpecifyFillColorContext extends ExprContext {
		public Token word;
		public TerminalNode LETTER() { return getToken(G01Parser.LETTER, 0); }
		public SpecifyFillColorContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class BeginFillContext extends ExprContext {
		public BeginFillContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class DrawlineExprContext extends ExprContext {
		public Token x_cord;
		public Token y_cord;
		public List<TerminalNode> NUMBER() { return getTokens(G01Parser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(G01Parser.NUMBER, i);
		}
		public DrawlineExprContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expr);
		try {
			setState(29);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new DrawlineExprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(8);
				match(T__0);
				setState(9);
				((DrawlineExprContext)_localctx).x_cord = match(NUMBER);
				setState(10);
				((DrawlineExprContext)_localctx).y_cord = match(NUMBER);
				}
				break;
			case T__1:
				_localctx = new PrintlineExprContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(11);
				match(T__1);
				setState(12);
				((PrintlineExprContext)_localctx).x_cord = match(NUMBER);
				setState(13);
				((PrintlineExprContext)_localctx).y_cord = match(NUMBER);
				}
				break;
			case T__2:
				_localctx = new DrawCircleContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(14);
				match(T__2);
				setState(15);
				((DrawCircleContext)_localctx).radius = match(NUMBER);
				setState(16);
				((DrawCircleContext)_localctx).extent = match(NUMBER);
				}
				break;
			case T__3:
				_localctx = new SpecifyColorContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(17);
				match(T__3);
				setState(18);
				((SpecifyColorContext)_localctx).word = match(LETTER);
				}
				break;
			case T__4:
				_localctx = new SpecifyFillColorContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(19);
				match(T__4);
				setState(20);
				((SpecifyFillColorContext)_localctx).word = match(LETTER);
				}
				break;
			case T__5:
				_localctx = new PenUpContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(21);
				match(T__5);
				}
				break;
			case T__6:
				_localctx = new PenDownContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(22);
				match(T__6);
				}
				break;
			case T__7:
				_localctx = new BeginFillContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(23);
				match(T__7);
				}
				break;
			case T__8:
				_localctx = new EndFillContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(24);
				match(T__8);
				}
				break;
			case T__9:
				_localctx = new GoRightContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(25);
				match(T__9);
				setState(26);
				((GoRightContext)_localctx).angle = match(NUMBER);
				}
				break;
			case T__10:
				_localctx = new SetOrientationContext(_localctx);
				enterOuterAlt(_localctx, 11);
				{
				setState(27);
				match(T__10);
				setState(28);
				((SetOrientationContext)_localctx).angle = match(NUMBER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20\"\4\2\t\2\4\3"+
		"\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3 \n\3\3\3\2\2\4\2\4\2\2\2*\2\b"+
		"\3\2\2\2\4\37\3\2\2\2\6\t\5\4\3\2\7\t\3\2\2\2\b\6\3\2\2\2\b\7\3\2\2\2"+
		"\t\3\3\2\2\2\n\13\7\3\2\2\13\f\7\16\2\2\f \7\16\2\2\r\16\7\4\2\2\16\17"+
		"\7\16\2\2\17 \7\16\2\2\20\21\7\5\2\2\21\22\7\16\2\2\22 \7\16\2\2\23\24"+
		"\7\6\2\2\24 \7\17\2\2\25\26\7\7\2\2\26 \7\17\2\2\27 \7\b\2\2\30 \7\t\2"+
		"\2\31 \7\n\2\2\32 \7\13\2\2\33\34\7\f\2\2\34 \7\16\2\2\35\36\7\r\2\2\36"+
		" \7\16\2\2\37\n\3\2\2\2\37\r\3\2\2\2\37\20\3\2\2\2\37\23\3\2\2\2\37\25"+
		"\3\2\2\2\37\27\3\2\2\2\37\30\3\2\2\2\37\31\3\2\2\2\37\32\3\2\2\2\37\33"+
		"\3\2\2\2\37\35\3\2\2\2 \5\3\2\2\2\4\b\37";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}