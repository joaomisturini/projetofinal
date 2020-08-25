#!/bin/bash

glpsol --check -m projeto.mod -d ./testes/$1.mod --wlp ./testes/$1.lp
