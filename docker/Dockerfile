FROM ubuntu:18.04

ARG USERNAME=joaomisturini
ARG USER_UID=1000
ARG USER_GID=1000

# instala common, java e python
RUN apt-get update && apt-get install -y --no-install-recommends sudo git openjdk-8-jdk glpk-utils python3 python3-pip

# troca user
RUN groupadd --gid $USER_GID $USERNAME && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME
RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && chmod 0440 /etc/sudoers.d/$USERNAME

# configura python
RUN pip3 install --upgrade pip setuptools
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi

# instala cplex
WORKDIR /home
COPY docker/cplex.bin cplex.bin
COPY docker/installer.properties installer.properties
RUN ./cplex.bin -f "./installer.properties"
RUN ln -s /opt/ibm/ILOG/CPLEX_Studio_Community129/cplex/bin/x86-64_linux/cplex /bin/cplex

# instala dependências via PIP e CPLEX for python
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN python /opt/ibm/ILOG/CPLEX_Studio_Community129/python/setup.py install

# limpeza
RUN rm -r /root/.cache
RUN rm cplex.bin installer.properties
RUN apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*

USER joaomisturini
