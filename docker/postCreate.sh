#!/bin/bash

mkdir -p ~/.ssh
cp -r /.ssh-localhost/* ~/.ssh
chmod 700 ~/.ssh
chmod 600 ~/.ssh/*
