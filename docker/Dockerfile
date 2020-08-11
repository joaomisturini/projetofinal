FROM ubuntu:18.04

ARG USERNAME=joaomisturini
ARG USER_UID=1000
ARG USER_GID=1000

RUN apt-get update && apt-get install -y --no-install-recommends sudo openjdk-8-jdk glpk-utils

RUN groupadd --gid $USER_GID $USERNAME && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && chmod 0440 /etc/sudoers.d/$USERNAME

WORKDIR /home

COPY docker/cplex.bin cplex.bin
COPY docker/installer.properties installer.properties

RUN ./cplex.bin -f "./installer.properties"
RUN ln -s /opt/ibm/ILOG/CPLEX_Studio_Community129/cplex/bin/x86-64_linux/cplex /bin/cplex

RUN rm cplex.bin installer.properties
RUN apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*

USER joaomisturini
