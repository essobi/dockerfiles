FROM jenkins  
  
MAINTAINER Fabrizio Lungo <docker@flungo.me>  
  
ARG user=jenkins  
  
# Change to root  
USER root  
  
# Install required packages  
RUN apt-get update && apt-get install -y cloc graphviz && rm -rf
/var/lib/apt/lists/*  
  
USER ${user}  

