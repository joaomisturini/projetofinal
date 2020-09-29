param pn, integer, > 0;
param hn, integer, > 0;

set P := 1..pn;
set H := 1..hn;

param x{p in P}, binary;
param d{p in P, h in H}, >= 0;

var y{p in P, h in H}, binary;

s.t. lim_localizacao{h in H}: sum{p in P} y[p, h] * x[p] = 1;

minimize distancia: sum{p in P, h in H} d[p, h] * y[p, h];

end;
