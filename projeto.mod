param pn, integer, > 0;
param ln, integer, > 0;
param hn, integer, > 0;

set P := 1..pn;
set L := 1..ln;
set H := 1..hn;

param e{p in P}, >= 0;
param v{p in P}, >= 0;
param c{l in L}, >= 0;
param t{l in L}, >= 0;
param d{p in P, h in H}, >= 0;
param DM, > 0;

var x{p in P, l in L}, binary;
var y{p in P, h in H}, binary;

s.t. lim_volume{p in P}: sum{l in L} c[l] * x[p, l] >= v[p];
s.t. lim_espaco{p in P}: sum{l in L} t[l] * x[p, l] <= e[p];
s.t. lim_localizacao{h in H}: sum{p in P} y[p, h] = 1;
s.t. lim_lixeiras{p in P, h in H}: sum{l in L} x[p, l] >= y[p, h];
s.t. lim_distancia{p in P, h in H}: d[p, h] * y[p, h] <= DM;
s.t. lim_instalacao{l in L}: 0 <= sum{p in P} x[p, l] <= 1;

minimize distancia: sum{p in P, h in H} d[p, h] * y[p, h];
minimize lixeiras: sum{p in P, l in L} x[p, l];

end;
