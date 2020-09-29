param pn, integer, > 0;
param hn, integer, > 0;

set P := 1..pn;
set H := 1..hn;

param e{p in P}, >= 0;
param v{h in H}, >= 0;
param d{p in P, h in H}, >= 0;
param cl, >= 0;
param tl, >= 0;
param dm, > 0;

var x{p in P}, integer, >= 0;
var y{p in P, h in H}, binary;

s.t. lim_volume{p in P}: cl * x[p] >= sum{h in H} v[h] * y[p, h];
s.t. lim_espaco{p in P}: tl * x[p] <= e[p];
s.t. lim_localizacao{h in H}: sum{p in P} y[p, h] = 1;
s.t. lim_lixeiras{p in P, h in H}: x[p] >= y[p, h];
s.t. lim_distancia{p in P, h in H}: d[p, h] * y[p, h] <= dm;

minimize distancia: sum{p in P, h in H} d[p, h] * y[p, h];
minimize lixeiras: sum{p in P} x[p];

end;
