# Ejemplos de lexer y parser usando ply
<pre>
G =< {E,T, F}, {+, ∗, num,(,)}, P, E >
E → E + T
E → T
T → T ∗ F
T → F
F → num
F → (E)
</pre>
