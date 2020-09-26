#!/bin/bash

glpsol --check -m projeto-posicao.mod -d ./testes/$1.mod --wlp ./testes/$1.lp
