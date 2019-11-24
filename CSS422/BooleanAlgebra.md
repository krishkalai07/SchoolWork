# Table

A | B | A and B | A or B | A xor B | A nand B | A nor B | A xnor B
--- | --- | --- | --- | --- | --- | --- | ---
0 | 0 | 0 | 0 | 0 | 1 | 1 | 1
0 | 1 | 0 | 1 | 1 | 1 | 0 | 0
1 | 0 | 0 | 1 | 1 | 1 | 0 | 0
1 | 1 | 1 | 1 | 0 | 0 | 0 | 1

# Rules

Rule | Name
--- | ---
A ~A = false | AND identity
A + ~A  = true | OR identity
A ^ B = A~B + ~AB | XOR definition
~(A B) = ~A + ~B | NAND definition / De Morgan's (OR) Law
~(A + B) = ~A~B | NOR definition / De Morgan's (AND) Law
~(A ^ B) = ~A~B + AB | XNOR definition

