# special functions, initializations

A = zeros(3);  # create 3x3 matrix filled with zeros
B = ones(2);   # create 2x2 matrix filled with ones
I = eye(5);   # create 5x5 matrix filled with ones on diagonal and zeros elsewhere

E1 = [ 10, 20, 30];
print E1;

A[1,2] = 3;
print A;


print "Pętla FOR:";

N = 5;
M = 10;
for i = 1:N {
    for j = i:M {
        print i, j;
    }
}

print "Pętla WHILE (wraz z IF, ELSE, BREAK i CONTINUE):";

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