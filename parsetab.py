
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNleft+-left*/rightUMINUSleftIFleftELSEADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOATNUM FOR ID IF INTNUM LESS LESSEQ MORE MOREEQ MULASSIGN NOTEQ ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSstart : instruction_setinstruction : expression\n                | conditional\n                | loopconditionalinstruction_set : instruction instruction_set\n                    | \'{\' instruction_set \'}\'\n                    | identifier : ID\n                | addressexpression : assignment ";"\n                | operation \';\'assignment : identifier \'=\' operand\n                | identifier \'=\' operation\n                | identifier assignoperation operand\n                | identifier assignoperation operationoperation : operand operator operand\n                | operand operator operation\n                | function \'(\' operand \')\'\n                | function \'(\' operation \')\'\n                | reservedoperation\n                | operand selfoperatorassignoperation : ADDASSIGN\n                        | SUBASSIGN\n                        | MULASSIGN\n                        | DIVASSIGNoperand : identifier\n            | number\n            | structure\n            | \'-\' operand %prec UMINUS\n            | addressoperator : \'+\'\n                | \'-\'\n                | \'*\'\n                | \'/\'operator : DOTADD\n                | DOTSUB\n                | DOTMUL\n                | DOTDIVselfoperator : "\'" function : ZEROS\n                | ONES\n                | EYEreservedoperation : RETURN operation\n                    | RETURN operand\n                    | RETURN\n                    | PRINT series\n                    | PRINT operation\n                    | PRINT operand\n                    | BREAK\n                    | CONTINUErelation : EQ\n                | NOTEQ\n                | LESS\n                | LESSEQ\n                | MORE\n                | MOREEQcondition : operand relation operand\n                | operation relation operand\n                | operand relation operation\n                | operation relation operationconditional : IF \'(\' condition \')\' instruction\n    | IF \'(\' condition \')\' \'{\' instruction_set \'}\'\n    | IF \'(\' condition \')\' instruction ELSE instruction\n    | IF \'(\' condition \')\' \'{\' instruction_set \'}\' ELSE instruction\n    | IF \'(\' condition \')\' instruction ELSE \'{\' instruction_set \'}\'\n    | IF \'(\' condition \')\' \'{\' instruction_set \'}\' ELSE \'{\' instruction_set \'}\'loopconditional : WHILE \'(\' condition \')\' instruction\n    | WHILE \'(\' condition \')\' \'{\' instruction_set \'}\'\n    | FOR identifier \'=\' range instruction\n    | FOR identifier \'=\' range \'{\' instruction_set \'}\' range : operand \':\' operandstructure : matrix\n                | STRINGmatrix : rows\n            | \'[\' rows \']\'rows : \'[\' series \']\'\n    | \'[\' series \']\' \',\' rowsseries : operand\n            | operand \',\' seriesinteger_series : number\n                    | number \',\' integer_seriesnumber : INTNUM\n            | FLOATNUMaddress : identifier \'[\' integer_series \']\''
    
_lr_action_items = {'{':([0,3,4,5,6,7,17,19,20,30,31,32,33,34,37,38,62,63,64,91,92,93,102,103,105,111,112,117,118,119,120,124,125,129,130,131,132,133,134,136,137,138,139,141,],[4,4,4,-2,-3,-4,-8,-27,-28,-82,-83,-72,-73,-74,-10,-11,-29,-26,-9,-75,-76,112,118,120,-84,-61,4,-67,4,-69,4,-77,131,-71,-63,4,-62,-68,-70,138,-65,4,-64,-66,]),'$end':([0,1,2,3,5,6,7,35,37,38,74,111,117,119,130,132,133,134,137,139,141,],[-7,0,-1,-7,-2,-3,-4,-5,-10,-11,-6,-61,-67,-69,-63,-62,-68,-70,-65,-64,-66,]),'IF':([0,3,4,5,6,7,17,19,20,30,31,32,33,34,37,38,62,63,64,91,92,93,102,103,105,111,112,117,118,119,120,124,125,129,130,131,132,133,134,136,137,138,139,141,],[10,10,10,-2,-3,-4,-8,-27,-28,-82,-83,-72,-73,-74,-10,-11,-29,-26,-9,-75,-76,10,10,10,-84,-61,10,-67,10,-69,10,-77,10,-71,-63,10,-62,-68,-70,10,-65,10,-64,-66,]),'WHILE':([0,3,4,5,6,7,17,19,20,30,31,32,33,34,37,38,62,63,64,91,92,93,102,103,105,111,112,117,118,119,120,124,125,129,130,131,132,133,134,136,137,138,139,141,],[11,11,11,-2,-3,-4,-8,-27,-28,-82,-83,-72,-73,-74,-10,-11,-29,-26,-9,-75,-76,11,11,11,-84,-61,11,-67,11,-69,11,-77,11,-71,-63,11,-62,-68,-70,11,-65,11,-64,-66,]),'FOR':([0,3,4,5,6,7,17,19,20,30,31,32,33,34,37,38,62,63,64,91,92,93,102,103,105,111,112,117,118,119,120,124,125,129,130,131,132,133,134,136,137,138,139,141,],[12,12,12,-2,-3,-4,-8,-27,-28,-82,-83,-72,-73,-74,-10,-11,-29,-26,-9,-75,-76,12,12,12,-84,-61,12,-67,12,-69,12,-77,12,-71,-63,12,-62,-68,-70,12,-65,12,-64,-66,]),'ID':([0,3,4,5,6,7,12,17,19,20,21,25,26,29,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,70,79,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,111,112,117,118,119,120,121,123,124,125,129,130,131,132,133,134,136,137,138,139,141,],[17,17,17,-2,-3,-4,17,-8,-27,-28,17,17,17,17,-82,-83,-72,-73,-74,-10,-11,17,17,17,17,-22,-23,-24,-25,17,-31,-32,-33,-34,-35,-36,-37,-38,17,-29,-26,-9,17,17,17,-75,-76,17,17,-51,-52,-53,-54,-55,-56,17,17,17,-84,-61,17,-67,17,-69,17,17,17,-77,17,-71,-63,17,-62,-68,-70,17,-65,17,-64,-66,]),'-':([0,3,4,5,6,7,13,14,17,18,19,20,21,25,26,29,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,66,69,70,76,79,80,82,86,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,111,112,113,116,117,118,119,120,121,123,124,125,129,130,131,132,133,134,136,137,138,139,141,],[21,21,21,-2,-3,-4,-26,53,-8,-9,-27,-28,21,21,21,21,-82,-83,-72,-73,-74,-10,-11,21,21,21,21,-22,-23,-24,-25,21,-31,-32,-33,-34,-35,-36,-37,-38,21,-29,-26,-9,53,53,21,53,21,53,53,53,53,21,-75,-76,21,21,-51,-52,-53,-54,-55,-56,21,21,21,-84,-61,21,53,53,-67,21,-69,21,21,21,-77,21,-71,-63,21,-62,-68,-70,21,-65,21,-64,-66,]),'ZEROS':([0,3,4,5,6,7,17,19,20,25,26,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,91,92,93,94,95,96,97,98,99,100,101,102,103,105,111,112,117,118,119,120,124,125,129,130,131,132,133,134,136,137,138,139,141,],[22,22,22,-2,-3,-4,-8,-27,-28,22,22,-82,-83,-72,-73,-74,-10,-11,22,22,22,22,-22,-23,-24,-25,22,-31,-32,-33,-34,-35,-36,-37,-38,22,-29,-26,-9,-75,-76,22,22,-51,-52,-53,-54,-55,-56,22,22,22,-84,-61,22,-67,22,-69,22,-77,22,-71,-63,22,-62,-68,-70,22,-65,22,-64,-66,]),'ONES':([0,3,4,5,6,7,17,19,20,25,26,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,91,92,93,94,95,96,97,98,99,100,101,102,103,105,111,112,117,118,119,120,124,125,129,130,131,132,133,134,136,137,138,139,141,],[23,23,23,-2,-3,-4,-8,-27,-28,23,23,-82,-83,-72,-73,-74,-10,-11,23,23,23,23,-22,-23,-24,-25,23,-31,-32,-33,-34,-35,-36,-37,-38,23,-29,-26,-9,-75,-76,23,23,-51,-52,-53,-54,-55,-56,23,23,23,-84,-61,23,-67,23,-69,23,-77,23,-71,-63,23,-62,-68,-70,23,-65,23,-64,-66,]),'EYE':([0,3,4,5,6,7,17,19,20,25,26,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,91,92,93,94,95,96,97,98,99,100,101,102,103,105,111,112,117,118,119,120,124,125,129,130,131,132,133,134,136,137,138,139,141,],[24,24,24,-2,-3,-4,-8,-27,-28,24,24,-82,-83,-72,-73,-74,-10,-11,24,24,24,24,-22,-23,-24,-25,24,-31,-32,-33,-34,-35,-36,-37,-38,24,-29,-26,-9,-75,-76,24,24,-51,-52,-53,-54,-55,-56,24,24,24,-84,-61,24,-67,24,-69,24,-77,24,-71,-63,24,-62,-68,-70,24,-65,24,-64,-66,]),'RETURN':([0,3,4,5,6,7,17,19,20,25,26,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,91,92,93,94,95,96,97,98,99,100,101,102,103,105,111,112,117,118,119,120,124,125,129,130,131,132,133,134,136,137,138,139,141,],[25,25,25,-2,-3,-4,-8,-27,-28,25,25,-82,-83,-72,-73,-74,-10,-11,25,25,25,25,-22,-23,-24,-25,25,-31,-32,-33,-34,-35,-36,-37,-38,25,-29,-26,-9,-75,-76,25,25,-51,-52,-53,-54,-55,-56,25,25,25,-84,-61,25,-67,25,-69,25,-77,25,-71,-63,25,-62,-68,-70,25,-65,25,-64,-66,]),'PRINT':([0,3,4,5,6,7,17,19,20,25,26,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,91,92,93,94,95,96,97,98,99,100,101,102,103,105,111,112,117,118,119,120,124,125,129,130,131,132,133,134,136,137,138,139,141,],[26,26,26,-2,-3,-4,-8,-27,-28,26,26,-82,-83,-72,-73,-74,-10,-11,26,26,26,26,-22,-23,-24,-25,26,-31,-32,-33,-34,-35,-36,-37,-38,26,-29,-26,-9,-75,-76,26,26,-51,-52,-53,-54,-55,-56,26,26,26,-84,-61,26,-67,26,-69,26,-77,26,-71,-63,26,-62,-68,-70,26,-65,26,-64,-66,]),'BREAK':([0,3,4,5,6,7,17,19,20,25,26,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,91,92,93,94,95,96,97,98,99,100,101,102,103,105,111,112,117,118,119,120,124,125,129,130,131,132,133,134,136,137,138,139,141,],[27,27,27,-2,-3,-4,-8,-27,-28,27,27,-82,-83,-72,-73,-74,-10,-11,27,27,27,27,-22,-23,-24,-25,27,-31,-32,-33,-34,-35,-36,-37,-38,27,-29,-26,-9,-75,-76,27,27,-51,-52,-53,-54,-55,-56,27,27,27,-84,-61,27,-67,27,-69,27,-77,27,-71,-63,27,-62,-68,-70,27,-65,27,-64,-66,]),'CONTINUE':([0,3,4,5,6,7,17,19,20,25,26,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,91,92,93,94,95,96,97,98,99,100,101,102,103,105,111,112,117,118,119,120,124,125,129,130,131,132,133,134,136,137,138,139,141,],[28,28,28,-2,-3,-4,-8,-27,-28,28,28,-82,-83,-72,-73,-74,-10,-11,28,28,28,28,-22,-23,-24,-25,28,-31,-32,-33,-34,-35,-36,-37,-38,28,-29,-26,-9,-75,-76,28,28,-51,-52,-53,-54,-55,-56,28,28,28,-84,-61,28,-67,28,-69,28,-77,28,-71,-63,28,-62,-68,-70,28,-65,28,-64,-66,]),'INTNUM':([0,3,4,5,6,7,17,19,20,21,25,26,29,30,31,32,33,34,37,38,39,40,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,70,79,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,106,111,112,117,118,119,120,121,123,124,125,129,130,131,132,133,134,136,137,138,139,141,],[30,30,30,-2,-3,-4,-8,-27,-28,30,30,30,30,-82,-83,-72,-73,-74,-10,-11,30,30,30,30,30,-22,-23,-24,-25,30,-31,-32,-33,-34,-35,-36,-37,-38,30,-29,-26,-9,30,30,30,-75,-76,30,30,-51,-52,-53,-54,-55,-56,30,30,30,-84,30,-61,30,-67,30,-69,30,30,30,-77,30,-71,-63,30,-62,-68,-70,30,-65,30,-64,-66,]),'FLOATNUM':([0,3,4,5,6,7,17,19,20,21,25,26,29,30,31,32,33,34,37,38,39,40,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,70,79,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,106,111,112,117,118,119,120,121,123,124,125,129,130,131,132,133,134,136,137,138,139,141,],[31,31,31,-2,-3,-4,-8,-27,-28,31,31,31,31,-82,-83,-72,-73,-74,-10,-11,31,31,31,31,31,-22,-23,-24,-25,31,-31,-32,-33,-34,-35,-36,-37,-38,31,-29,-26,-9,31,31,31,-75,-76,31,31,-51,-52,-53,-54,-55,-56,31,31,31,-84,31,-61,31,-67,31,-69,31,31,31,-77,31,-71,-63,31,-62,-68,-70,31,-65,31,-64,-66,]),'STRING':([0,3,4,5,6,7,17,19,20,21,25,26,29,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,70,79,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,111,112,117,118,119,120,121,123,124,125,129,130,131,132,133,134,136,137,138,139,141,],[33,33,33,-2,-3,-4,-8,-27,-28,33,33,33,33,-82,-83,-72,-73,-74,-10,-11,33,33,33,33,-22,-23,-24,-25,33,-31,-32,-33,-34,-35,-36,-37,-38,33,-29,-26,-9,33,33,33,-75,-76,33,33,-51,-52,-53,-54,-55,-56,33,33,33,-84,-61,33,-67,33,-69,33,33,33,-77,33,-71,-63,33,-62,-68,-70,33,-65,33,-64,-66,]),'[':([0,3,4,5,6,7,13,17,18,19,20,21,25,26,29,30,31,32,33,34,37,38,39,40,41,42,43,44,46,47,48,49,50,52,53,54,55,56,57,58,59,61,62,63,64,70,79,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,110,111,112,117,118,119,120,121,123,124,125,129,130,131,132,133,134,136,137,138,139,141,],[29,29,29,-2,-3,-4,45,-8,-9,-27,-28,29,29,29,70,-82,-83,-72,-73,-74,-10,-11,29,29,45,-9,29,29,-22,-23,-24,-25,29,-31,-32,-33,-34,-35,-36,-37,-38,29,-29,45,-9,70,29,29,-75,-76,29,29,-51,-52,-53,-54,-55,-56,29,29,29,-84,123,-61,29,-67,29,-69,29,29,29,-77,29,-71,-63,29,-62,-68,-70,29,-65,29,-64,-66,]),'}':([3,4,5,6,7,35,36,37,38,74,111,112,117,118,119,120,126,127,128,130,131,132,133,134,135,137,138,139,140,141,],[-7,-7,-2,-3,-4,-5,74,-10,-11,-6,-61,-7,-67,-7,-69,-7,132,133,134,-63,-7,-62,-68,-70,137,-65,-7,-64,141,-66,]),'ELSE':([5,6,7,37,38,111,117,119,130,132,133,134,137,139,141,],[-2,-3,-4,-10,-11,125,-67,-69,-63,136,-68,-70,-65,-64,-66,]),';':([8,9,16,17,19,20,25,27,28,30,31,32,33,34,51,60,62,63,64,65,66,67,68,69,73,80,81,82,83,86,87,91,92,105,107,108,109,124,],[37,38,-20,-8,-27,-28,-45,-49,-50,-82,-83,-72,-73,-74,-21,-39,-29,-26,-9,-43,-44,-46,-47,-48,-78,-12,-13,-14,-15,-16,-17,-75,-76,-84,-18,-19,-79,-77,]),'(':([10,11,15,22,23,24,],[39,40,61,-40,-41,-42,]),'=':([13,17,18,41,42,105,],[43,-8,-9,79,-9,-84,]),'+':([13,14,17,18,19,20,30,31,32,33,34,62,63,64,66,69,76,80,82,86,88,91,92,105,113,116,124,],[-26,52,-8,-9,-27,-28,-82,-83,-72,-73,-74,-29,-26,-9,52,52,52,52,52,52,52,-75,-76,-84,52,52,-77,]),'*':([13,14,17,18,19,20,30,31,32,33,34,62,63,64,66,69,76,80,82,86,88,91,92,105,113,116,124,],[-26,54,-8,-9,-27,-28,-82,-83,-72,-73,-74,-29,-26,-9,54,54,54,54,54,54,54,-75,-76,-84,54,54,-77,]),'/':([13,14,17,18,19,20,30,31,32,33,34,62,63,64,66,69,76,80,82,86,88,91,92,105,113,116,124,],[-26,55,-8,-9,-27,-28,-82,-83,-72,-73,-74,-29,-26,-9,55,55,55,55,55,55,55,-75,-76,-84,55,55,-77,]),'DOTADD':([13,14,17,18,19,20,30,31,32,33,34,62,63,64,66,69,76,80,82,86,88,91,92,105,113,116,124,],[-26,56,-8,-9,-27,-28,-82,-83,-72,-73,-74,-29,-26,-9,56,56,56,56,56,56,56,-75,-76,-84,56,56,-77,]),'DOTSUB':([13,14,17,18,19,20,30,31,32,33,34,62,63,64,66,69,76,80,82,86,88,91,92,105,113,116,124,],[-26,57,-8,-9,-27,-28,-82,-83,-72,-73,-74,-29,-26,-9,57,57,57,57,57,57,57,-75,-76,-84,57,57,-77,]),'DOTMUL':([13,14,17,18,19,20,30,31,32,33,34,62,63,64,66,69,76,80,82,86,88,91,92,105,113,116,124,],[-26,58,-8,-9,-27,-28,-82,-83,-72,-73,-74,-29,-26,-9,58,58,58,58,58,58,58,-75,-76,-84,58,58,-77,]),'DOTDIV':([13,14,17,18,19,20,30,31,32,33,34,62,63,64,66,69,76,80,82,86,88,91,92,105,113,116,124,],[-26,59,-8,-9,-27,-28,-82,-83,-72,-73,-74,-29,-26,-9,59,59,59,59,59,59,59,-75,-76,-84,59,59,-77,]),"'":([13,14,17,18,19,20,30,31,32,33,34,62,63,64,66,69,76,80,82,86,88,91,92,105,113,116,124,],[-26,60,-8,-9,-27,-28,-82,-83,-72,-73,-74,-29,-26,-9,60,60,60,60,60,60,60,-75,-76,-84,60,60,-77,]),'ADDASSIGN':([13,17,18,105,],[46,-8,-9,-84,]),'SUBASSIGN':([13,17,18,105,],[47,-8,-9,-84,]),'MULASSIGN':([13,17,18,105,],[48,-8,-9,-84,]),'DIVASSIGN':([13,17,18,105,],[49,-8,-9,-84,]),'EQ':([16,17,19,20,25,27,28,30,31,32,33,34,51,60,62,63,64,65,66,67,68,69,73,76,77,86,87,91,92,105,107,108,109,124,],[-20,-8,-27,-28,-45,-49,-50,-82,-83,-72,-73,-74,-21,-39,-29,-26,-9,-43,-44,-46,-47,-48,-78,95,95,-16,-17,-75,-76,-84,-18,-19,-79,-77,]),'NOTEQ':([16,17,19,20,25,27,28,30,31,32,33,34,51,60,62,63,64,65,66,67,68,69,73,76,77,86,87,91,92,105,107,108,109,124,],[-20,-8,-27,-28,-45,-49,-50,-82,-83,-72,-73,-74,-21,-39,-29,-26,-9,-43,-44,-46,-47,-48,-78,96,96,-16,-17,-75,-76,-84,-18,-19,-79,-77,]),'LESS':([16,17,19,20,25,27,28,30,31,32,33,34,51,60,62,63,64,65,66,67,68,69,73,76,77,86,87,91,92,105,107,108,109,124,],[-20,-8,-27,-28,-45,-49,-50,-82,-83,-72,-73,-74,-21,-39,-29,-26,-9,-43,-44,-46,-47,-48,-78,97,97,-16,-17,-75,-76,-84,-18,-19,-79,-77,]),'LESSEQ':([16,17,19,20,25,27,28,30,31,32,33,34,51,60,62,63,64,65,66,67,68,69,73,76,77,86,87,91,92,105,107,108,109,124,],[-20,-8,-27,-28,-45,-49,-50,-82,-83,-72,-73,-74,-21,-39,-29,-26,-9,-43,-44,-46,-47,-48,-78,98,98,-16,-17,-75,-76,-84,-18,-19,-79,-77,]),'MORE':([16,17,19,20,25,27,28,30,31,32,33,34,51,60,62,63,64,65,66,67,68,69,73,76,77,86,87,91,92,105,107,108,109,124,],[-20,-8,-27,-28,-45,-49,-50,-82,-83,-72,-73,-74,-21,-39,-29,-26,-9,-43,-44,-46,-47,-48,-78,99,99,-16,-17,-75,-76,-84,-18,-19,-79,-77,]),'MOREEQ':([16,17,19,20,25,27,28,30,31,32,33,34,51,60,62,63,64,65,66,67,68,69,73,76,77,86,87,91,92,105,107,108,109,124,],[-20,-8,-27,-28,-45,-49,-50,-82,-83,-72,-73,-74,-21,-39,-29,-26,-9,-43,-44,-46,-47,-48,-78,100,100,-16,-17,-75,-76,-84,-18,-19,-79,-77,]),')':([16,17,19,20,25,27,28,30,31,32,33,34,51,60,62,63,64,65,66,67,68,69,73,75,78,86,87,88,89,91,92,105,107,108,109,113,114,115,116,124,],[-20,-8,-27,-28,-45,-49,-50,-82,-83,-72,-73,-74,-21,-39,-29,-26,-9,-43,-44,-46,-47,-48,-78,93,102,-16,-17,107,108,-75,-76,-84,-18,-19,-79,-57,-59,-60,-58,-77,]),',':([17,19,20,30,31,32,33,34,62,63,64,69,71,73,85,91,92,105,124,],[-8,-27,-28,-82,-83,-72,-73,-74,-29,-26,-9,90,-74,90,106,-75,110,-84,-77,]),']':([17,19,20,30,31,32,33,34,62,63,64,71,72,73,84,85,91,92,105,109,122,124,],[-8,-27,-28,-82,-83,-72,-73,-74,-29,-26,-9,91,92,-78,105,-80,-75,-76,-84,-79,-81,-77,]),':':([17,19,20,30,31,32,33,34,62,63,64,91,92,104,105,124,],[-8,-27,-28,-82,-83,-72,-73,-74,-29,-26,-9,-75,-76,121,-84,-77,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'instruction_set':([0,3,4,112,118,120,131,138,],[2,35,36,126,127,128,135,140,]),'instruction':([0,3,4,93,102,103,112,118,120,125,131,136,138,],[3,3,3,111,117,119,3,3,3,130,3,139,3,]),'expression':([0,3,4,93,102,103,112,118,120,125,131,136,138,],[5,5,5,5,5,5,5,5,5,5,5,5,5,]),'conditional':([0,3,4,93,102,103,112,118,120,125,131,136,138,],[6,6,6,6,6,6,6,6,6,6,6,6,6,]),'loopconditional':([0,3,4,93,102,103,112,118,120,125,131,136,138,],[7,7,7,7,7,7,7,7,7,7,7,7,7,]),'assignment':([0,3,4,93,102,103,112,118,120,125,131,136,138,],[8,8,8,8,8,8,8,8,8,8,8,8,8,]),'operation':([0,3,4,25,26,39,40,43,44,50,61,93,94,101,102,103,112,118,120,125,131,136,138,],[9,9,9,65,68,77,77,81,83,87,89,9,114,115,9,9,9,9,9,9,9,9,9,]),'identifier':([0,3,4,12,21,25,26,29,39,40,43,44,50,61,70,79,90,93,94,101,102,103,112,118,120,121,123,125,131,136,138,],[13,13,13,41,63,63,63,63,63,63,63,63,63,63,63,63,63,13,63,63,13,13,13,13,13,63,63,13,13,13,13,]),'operand':([0,3,4,21,25,26,29,39,40,43,44,50,61,70,79,90,93,94,101,102,103,112,118,120,121,123,125,131,136,138,],[14,14,14,62,66,69,73,76,76,80,82,86,88,73,104,73,14,113,116,14,14,14,14,14,129,73,14,14,14,14,]),'function':([0,3,4,25,26,39,40,43,44,50,61,93,94,101,102,103,112,118,120,125,131,136,138,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'reservedoperation':([0,3,4,25,26,39,40,43,44,50,61,93,94,101,102,103,112,118,120,125,131,136,138,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'address':([0,3,4,12,21,25,26,29,39,40,43,44,50,61,70,79,90,93,94,101,102,103,112,118,120,121,123,125,131,136,138,],[18,18,18,42,64,64,64,64,64,64,64,64,64,64,64,64,64,18,64,64,18,18,18,18,18,64,64,18,18,18,18,]),'number':([0,3,4,21,25,26,29,39,40,43,44,45,50,61,70,79,90,93,94,101,102,103,106,112,118,120,121,123,125,131,136,138,],[19,19,19,19,19,19,19,19,19,19,19,85,19,19,19,19,19,19,19,19,19,19,85,19,19,19,19,19,19,19,19,19,]),'structure':([0,3,4,21,25,26,29,39,40,43,44,50,61,70,79,90,93,94,101,102,103,112,118,120,121,123,125,131,136,138,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'matrix':([0,3,4,21,25,26,29,39,40,43,44,50,61,70,79,90,93,94,101,102,103,112,118,120,121,123,125,131,136,138,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'rows':([0,3,4,21,25,26,29,39,40,43,44,50,61,70,79,90,93,94,101,102,103,110,112,118,120,121,123,125,131,136,138,],[34,34,34,34,34,34,71,34,34,34,34,34,34,71,34,34,34,34,34,34,34,124,34,34,34,34,34,34,34,34,34,]),'assignoperation':([13,],[44,]),'operator':([14,66,69,76,80,82,86,88,113,116,],[50,50,50,50,50,50,50,50,50,50,]),'selfoperator':([14,66,69,76,80,82,86,88,113,116,],[51,51,51,51,51,51,51,51,51,51,]),'series':([26,29,70,90,123,],[67,72,72,109,72,]),'condition':([39,40,],[75,78,]),'integer_series':([45,106,],[84,122,]),'relation':([76,77,],[94,101,]),'range':([79,],[103,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> instruction_set','start',1,'p_start','parser.py',27),
  ('instruction -> expression','instruction',1,'p_instruction','parser.py',32),
  ('instruction -> conditional','instruction',1,'p_instruction','parser.py',33),
  ('instruction -> loopconditional','instruction',1,'p_instruction','parser.py',34),
  ('instruction_set -> instruction instruction_set','instruction_set',2,'p_instruction_set','parser.py',39),
  ('instruction_set -> { instruction_set }','instruction_set',3,'p_instruction_set','parser.py',40),
  ('instruction_set -> <empty>','instruction_set',0,'p_instruction_set','parser.py',41),
  ('identifier -> ID','identifier',1,'p_identifier','parser.py',51),
  ('identifier -> address','identifier',1,'p_identifier','parser.py',52),
  ('expression -> assignment ;','expression',2,'p_expression','parser.py',57),
  ('expression -> operation ;','expression',2,'p_expression','parser.py',58),
  ('assignment -> identifier = operand','assignment',3,'p_assignment','parser.py',63),
  ('assignment -> identifier = operation','assignment',3,'p_assignment','parser.py',64),
  ('assignment -> identifier assignoperation operand','assignment',3,'p_assignment','parser.py',65),
  ('assignment -> identifier assignoperation operation','assignment',3,'p_assignment','parser.py',66),
  ('operation -> operand operator operand','operation',3,'p_operation','parser.py',71),
  ('operation -> operand operator operation','operation',3,'p_operation','parser.py',72),
  ('operation -> function ( operand )','operation',4,'p_operation','parser.py',73),
  ('operation -> function ( operation )','operation',4,'p_operation','parser.py',74),
  ('operation -> reservedoperation','operation',1,'p_operation','parser.py',75),
  ('operation -> operand selfoperator','operation',2,'p_operation','parser.py',76),
  ('assignoperation -> ADDASSIGN','assignoperation',1,'p_assignoperation','parser.py',88),
  ('assignoperation -> SUBASSIGN','assignoperation',1,'p_assignoperation','parser.py',89),
  ('assignoperation -> MULASSIGN','assignoperation',1,'p_assignoperation','parser.py',90),
  ('assignoperation -> DIVASSIGN','assignoperation',1,'p_assignoperation','parser.py',91),
  ('operand -> identifier','operand',1,'p_operand','parser.py',96),
  ('operand -> number','operand',1,'p_operand','parser.py',97),
  ('operand -> structure','operand',1,'p_operand','parser.py',98),
  ('operand -> - operand','operand',2,'p_operand','parser.py',99),
  ('operand -> address','operand',1,'p_operand','parser.py',100),
  ('operator -> +','operator',1,'p_standard_operators','parser.py',108),
  ('operator -> -','operator',1,'p_standard_operators','parser.py',109),
  ('operator -> *','operator',1,'p_standard_operators','parser.py',110),
  ('operator -> /','operator',1,'p_standard_operators','parser.py',111),
  ('operator -> DOTADD','operator',1,'p_dot_operators','parser.py',116),
  ('operator -> DOTSUB','operator',1,'p_dot_operators','parser.py',117),
  ('operator -> DOTMUL','operator',1,'p_dot_operators','parser.py',118),
  ('operator -> DOTDIV','operator',1,'p_dot_operators','parser.py',119),
  ("selfoperator -> '",'selfoperator',1,'p_selfoperator','parser.py',124),
  ('function -> ZEROS','function',1,'p_function','parser.py',129),
  ('function -> ONES','function',1,'p_function','parser.py',130),
  ('function -> EYE','function',1,'p_function','parser.py',131),
  ('reservedoperation -> RETURN operation','reservedoperation',2,'p_reserved_operation','parser.py',136),
  ('reservedoperation -> RETURN operand','reservedoperation',2,'p_reserved_operation','parser.py',137),
  ('reservedoperation -> RETURN','reservedoperation',1,'p_reserved_operation','parser.py',138),
  ('reservedoperation -> PRINT series','reservedoperation',2,'p_reserved_operation','parser.py',139),
  ('reservedoperation -> PRINT operation','reservedoperation',2,'p_reserved_operation','parser.py',140),
  ('reservedoperation -> PRINT operand','reservedoperation',2,'p_reserved_operation','parser.py',141),
  ('reservedoperation -> BREAK','reservedoperation',1,'p_reserved_operation','parser.py',142),
  ('reservedoperation -> CONTINUE','reservedoperation',1,'p_reserved_operation','parser.py',143),
  ('relation -> EQ','relation',1,'p_relation','parser.py',151),
  ('relation -> NOTEQ','relation',1,'p_relation','parser.py',152),
  ('relation -> LESS','relation',1,'p_relation','parser.py',153),
  ('relation -> LESSEQ','relation',1,'p_relation','parser.py',154),
  ('relation -> MORE','relation',1,'p_relation','parser.py',155),
  ('relation -> MOREEQ','relation',1,'p_relation','parser.py',156),
  ('condition -> operand relation operand','condition',3,'p_condition','parser.py',161),
  ('condition -> operation relation operand','condition',3,'p_condition','parser.py',162),
  ('condition -> operand relation operation','condition',3,'p_condition','parser.py',163),
  ('condition -> operation relation operation','condition',3,'p_condition','parser.py',164),
  ('conditional -> IF ( condition ) instruction','conditional',5,'p_conditional','parser.py',169),
  ('conditional -> IF ( condition ) { instruction_set }','conditional',7,'p_conditional','parser.py',170),
  ('conditional -> IF ( condition ) instruction ELSE instruction','conditional',7,'p_conditional','parser.py',171),
  ('conditional -> IF ( condition ) { instruction_set } ELSE instruction','conditional',9,'p_conditional','parser.py',172),
  ('conditional -> IF ( condition ) instruction ELSE { instruction_set }','conditional',9,'p_conditional','parser.py',173),
  ('conditional -> IF ( condition ) { instruction_set } ELSE { instruction_set }','conditional',11,'p_conditional','parser.py',174),
  ('loopconditional -> WHILE ( condition ) instruction','loopconditional',5,'p_loopconditional','parser.py',191),
  ('loopconditional -> WHILE ( condition ) { instruction_set }','loopconditional',7,'p_loopconditional','parser.py',192),
  ('loopconditional -> FOR identifier = range instruction','loopconditional',5,'p_loopconditional','parser.py',193),
  ('loopconditional -> FOR identifier = range { instruction_set }','loopconditional',7,'p_loopconditional','parser.py',194),
  ('range -> operand : operand','range',3,'p_range','parser.py',206),
  ('structure -> matrix','structure',1,'p_structure','parser.py',211),
  ('structure -> STRING','structure',1,'p_structure','parser.py',212),
  ('matrix -> rows','matrix',1,'p_matrix','parser.py',217),
  ('matrix -> [ rows ]','matrix',3,'p_matrix','parser.py',218),
  ('rows -> [ series ]','rows',3,'p_rows','parser.py',226),
  ('rows -> [ series ] , rows','rows',5,'p_rows','parser.py',227),
  ('series -> operand','series',1,'p_series','parser.py',235),
  ('series -> operand , series','series',3,'p_series','parser.py',236),
  ('integer_series -> number','integer_series',1,'p_integer_series','parser.py',244),
  ('integer_series -> number , integer_series','integer_series',3,'p_integer_series','parser.py',245),
  ('number -> INTNUM','number',1,'p_number','parser.py',253),
  ('number -> FLOATNUM','number',1,'p_number','parser.py',254),
  ('address -> identifier [ integer_series ]','address',4,'p_address','parser.py',259),
]
