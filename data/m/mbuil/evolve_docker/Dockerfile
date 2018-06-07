FROM ubuntu:14.04  
MAINTAINER Jose Lausuch<jose.lausuch@ericsson.com>  
LABEL version="0.1"description="my first container"  
ARG BRANCH=master  
ARG REPOS=/home/evolve/repos/  
ENV foo=bar  
WORKDIR /home/evolve/  
RUN apt-get update &&apt-get install -y git wget cowsay  
RUN mkdir -p $REPOS  
RUN echo "set nocompatible \nset backspace=2" >> /home/evolve/.vimrc  
RUN echo “set nocompatible” >> /home/evolve/.exrc  

