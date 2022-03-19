grammar G01;

start : expr | <EOF> ;

expr     : 'G01' x_cord=NUMBER y_cord=NUMBER #drawlineExpr    
         | 'print' x_cord=NUMBER y_cord=NUMBER #printlineExpr   
         | 'G28' radius=NUMBER extent=NUMBER #drawCircle 
         | 'GC' word=LETTER #specifyColor
         | 'GFC' word=LETTER #specifyFillColor
         | 'PU' #PenUp
         | 'PD' #PenDown
         | 'BF' #beginFill
         | 'EF' #endFill
         | 'RT' angle=NUMBER #goRight
         | 'SETH' angle=NUMBER #setOrientation
         ;
NUMBER : '-'?('0' .. '9') + ('.' ('0' .. '9') +)? ;
LETTER : ('a' .. 'z')+;
WS : [ \r\n\t]+ -> skip;