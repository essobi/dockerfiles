################################################  
# Dockerfile to build Gemma software  
# Based on debian  
################################################  
  
# Set the base image to debian  
  
FROM debian:jessie  
  
LABEL version="0.97"  
  
# Set noninterative mode  
ENV DEBIAN_FRONTEND noninteractive  
ENV PACKAGES wget bzip2  
  
RUN apt-get update -y  
RUN apt-get install -y ${PACKAGES}  
  
ENV GEMMA_URL https://github.com/genetics-
statistics/GEMMA/releases/download/v0.97/gemma-git-
gn2-0.97-c760aa0-generic-x86_64.tar.bz2  
ENV GEMMA_NAME_ARCHIVE gemma-git-gn2-0.97-c760aa0-generic-x86_64.tar.bz2  
ENV GEMMA_PATH /opt/gemma/  
  
WORKDIR ${GEMMA_PATH}  
  
RUN wget ${GEMMA_URL} && tar xvjf ${GEMMA_NAME_ARCHIVE}  
  
RUN sh install.sh ${GEMMA_PATH}/install  
  
RUN cp ${GEMMA_PATH}/install/bin/* /usr/local/bin  
  
RUN /usr/local/bin/gemma -h  

