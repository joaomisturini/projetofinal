\* Problem: binModel *\

Minimize multi-objectives
 distancia: AbsTol=0
 + 10 y(1,1) + 120 y(1,2) + 50 y(1,3) + 60 y(1,4) + 40 y(2,1) + 80 y(2,2)
 + 20 y(2,3) + 120 y(2,4) + 70 y(3,1) + 40 y(3,2) + 10 y(3,3) + 130 y(3,4)
 + 120 y(4,1) + 100 y(4,2) + 160 y(4,3) + 10 y(4,4) + 70 y(5,1) + 30 y(5,2)
 + 100 y(5,3) + 70 y(5,4)
 lixeiras: Priority=-1
 + x(1) + x(2) + x(3) + x(4) + x(5)

Subject To
 lim_volume(1): + 1000 x(1) - 108.9 y(1,1) - 1089 y(1,2) - 29.04 y(1,3)
 - 72.6 y(1,4) >= -0
 lim_volume(2): + 1000 x(2) - 108.9 y(2,1) - 1089 y(2,2) - 29.04 y(2,3)
 - 72.6 y(2,4) >= -0
 lim_volume(3): + 1000 x(3) - 108.9 y(3,1) - 1089 y(3,2) - 29.04 y(3,3)
 - 72.6 y(3,4) >= -0
 lim_volume(4): + 1000 x(4) - 108.9 y(4,1) - 1089 y(4,2) - 29.04 y(4,3)
 - 72.6 y(4,4) >= -0
 lim_volume(5): + 1000 x(5) - 108.9 y(5,1) - 1089 y(5,2) - 29.04 y(5,3)
 - 72.6 y(5,4) >= -0
 lim_espaco(1): + 3 x(1) <= 30
 lim_espaco(2): + 3 x(2) <= 30
 lim_espaco(3): + 3 x(3) <= 30
 lim_espaco(4): + 3 x(4) <= 30
 lim_espaco(5): + 3 x(5) <= 30
 lim_localizacao(1): + y(1,1) + y(2,1) + y(3,1) + y(4,1) + y(5,1) = 1
 lim_localizacao(2): + y(1,2) + y(2,2) + y(3,2) + y(4,2) + y(5,2) = 1
 lim_localizacao(3): + y(1,3) + y(2,3) + y(3,3) + y(4,3) + y(5,3) = 1
 lim_localizacao(4): + y(1,4) + y(2,4) + y(3,4) + y(4,4) + y(5,4) = 1
 lim_lixeiras(1,1): + x(1) - y(1,1) >= -0
 lim_lixeiras(1,2): + x(1) - y(1,2) >= -0
 lim_lixeiras(1,3): + x(1) - y(1,3) >= -0
 lim_lixeiras(1,4): + x(1) - y(1,4) >= -0
 lim_lixeiras(2,1): + x(2) - y(2,1) >= -0
 lim_lixeiras(2,2): + x(2) - y(2,2) >= -0
 lim_lixeiras(2,3): + x(2) - y(2,3) >= -0
 lim_lixeiras(2,4): + x(2) - y(2,4) >= -0
 lim_lixeiras(3,1): + x(3) - y(3,1) >= -0
 lim_lixeiras(3,2): + x(3) - y(3,2) >= -0
 lim_lixeiras(3,3): + x(3) - y(3,3) >= -0
 lim_lixeiras(3,4): + x(3) - y(3,4) >= -0
 lim_lixeiras(4,1): + x(4) - y(4,1) >= -0
 lim_lixeiras(4,2): + x(4) - y(4,2) >= -0
 lim_lixeiras(4,3): + x(4) - y(4,3) >= -0
 lim_lixeiras(4,4): + x(4) - y(4,4) >= -0
 lim_lixeiras(5,1): + x(5) - y(5,1) >= -0
 lim_lixeiras(5,2): + x(5) - y(5,2) >= -0
 lim_lixeiras(5,3): + x(5) - y(5,3) >= -0
 lim_lixeiras(5,4): + x(5) - y(5,4) >= -0
 lim_distancia(1,1): + 10 y(1,1) <= 100
 lim_distancia(1,2): + 120 y(1,2) <= 100
 lim_distancia(1,3): + 50 y(1,3) <= 100
 lim_distancia(1,4): + 60 y(1,4) <= 100
 lim_distancia(2,1): + 40 y(2,1) <= 100
 lim_distancia(2,2): + 80 y(2,2) <= 100
 lim_distancia(2,3): + 20 y(2,3) <= 100
 lim_distancia(2,4): + 120 y(2,4) <= 100
 lim_distancia(3,1): + 70 y(3,1) <= 100
 lim_distancia(3,2): + 40 y(3,2) <= 100
 lim_distancia(3,3): + 10 y(3,3) <= 100
 lim_distancia(3,4): + 130 y(3,4) <= 100
 lim_distancia(4,1): + 120 y(4,1) <= 100
 lim_distancia(4,2): + 100 y(4,2) <= 100
 lim_distancia(4,3): + 160 y(4,3) <= 100
 lim_distancia(4,4): + 10 y(4,4) <= 100
 lim_distancia(5,1): + 70 y(5,1) <= 100
 lim_distancia(5,2): + 30 y(5,2) <= 100
 lim_distancia(5,3): + 100 y(5,3) <= 100
 lim_distancia(5,4): + 70 y(5,4) <= 100

Bounds
 0 <= y(1,1) <= 1
 0 <= y(1,2) <= 1
 0 <= y(1,3) <= 1
 0 <= y(1,4) <= 1
 0 <= y(2,1) <= 1
 0 <= y(2,2) <= 1
 0 <= y(2,3) <= 1
 0 <= y(2,4) <= 1
 0 <= y(3,1) <= 1
 0 <= y(3,2) <= 1
 0 <= y(3,3) <= 1
 0 <= y(3,4) <= 1
 0 <= y(4,1) <= 1
 0 <= y(4,2) <= 1
 0 <= y(4,3) <= 1
 0 <= y(4,4) <= 1
 0 <= y(5,1) <= 1
 0 <= y(5,2) <= 1
 0 <= y(5,3) <= 1
 0 <= y(5,4) <= 1

Generals
 x(1)
 x(2)
 x(3)
 x(4)
 x(5)
 y(1,1)
 y(1,2)
 y(1,3)
 y(1,4)
 y(2,1)
 y(2,2)
 y(2,3)
 y(2,4)
 y(3,1)
 y(3,2)
 y(3,3)
 y(3,4)
 y(4,1)
 y(4,2)
 y(4,3)
 y(4,4)
 y(5,1)
 y(5,2)
 y(5,3)
 y(5,4)

End
