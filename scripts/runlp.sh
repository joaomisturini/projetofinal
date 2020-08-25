#!/bin/bash

cplex -c "read $1" "optimize" "display solution objective *"
