#!/bin/bash

cplex -c "read ./testes/$1.lp" "optimize" "display solution objective *"
