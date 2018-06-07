FROM jenkins/jenkins:lts  
  
ARG user=jenkins  
  
LABEL maintainer="gilgamez@gmail.com"  
  
USER root  
  
RUN apt-get update && apt-get install -y build-essential && rm -rf
/var/lib/apt/lists/*  
  
USER ${user}  

