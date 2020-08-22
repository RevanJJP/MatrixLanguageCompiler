# Matrix Language Interpreter

Interpreter prostego języka służącego do wykonywania obliczeń na macierzach.

Należy uruchomić ```main.py``` wraz z żądanym plikiem jako argumentem, lub bez argumentu, aby uruchomić kod przykładowy (```example.m```).

Kod zawiera:
		
- Skaner
- Parser 
- Generator drzewa składni (AST)
- Analizator semantyczny (Type Checker)
- Interpreter


## Specyfikacja języka

Obsługiwane:

- operatory binare: +, -, *, /
- macierzowe operatory binarne (dla operacji element po elemencie): .+, .-, .*, ./
- operatory przypisania: =, +=, -=, *=, /=
- operatory relacyjne: <, >, <=, >=, !=, ==
- nawiasy: (,), [,], {,}
- operator zakresu: :
- transpozycja macierzy: '
- przecinek i średnik: , ;
- słowa kluczowe: if, else, for, while
- słowa kluczowe: break, continue oraz return
- słowa kluczowe: eye, zeros oraz ones
- słowa kluczowe: print
- identyfikatory (pierwszy znak identyfikatora to litera lub znak _, w kolejnych znakach mogą dodatkowo wystąpić cyfry)
- liczby całkowite
- liczby zmiennoprzecinkowe
- stringi
	
### Przykładowy kod

	special functions, initializations
	
	A = zeros(3);  # create 3x3 matrix filled with zeros
	B = ones(2);   # create 2x2 matrix filled with ones
	I = eye(5);   # create 5x5 matrix filled with ones on diagonal and zeros elsewhere
	
	E1 = [10, 20, 30];
	print E1;
	
	A[1,2] = 3;
	print A;
	
	
	print "FOR loop";
	
	N = 5;
	M = 10;
	for i = 1:N {
	    for j = i:M {
	        print i, j;
	    }
	}
	
	print "WHILE loop (with IF, ELSE, BREAK and CONTINUE):";
	
	i = 0;
	
	while (i<5) {
	    i += 1;
	    print i;
	
	    if(i == 3)
	        break;
	    else
	        continue;
	}
	
	T = [ [ 1, 2, 3],
	       [ 4, 5, 6] ];
	return T';