FROM ubuntu:14.04  
MAINTAINER Adarsh  
LABEL version="0.1"description="my first container"  
ARG BRANCH=master  
ARG REPOS=/home/adarsh/projects/docker/repos  
ENV foo=bar  
WORKDIR /home/adarsh/projects/docker/  
RUN apt-get update && apt-get install -y git wget python-pip cowsay  
RUN mkdir -p $REPOS  
RUN git clone -b $BRANCH https://gerrit.opnfv.org/gerrit/sdnvpn $REPOS/sdnvpn  
RUN echo "set nocompatible \nset backspace=2" >>
/home/adarsh/projects/docker/.vimrc  
RUN echo “set nocompatible” >> /home/adarsh/projects/docker/.exrc  

