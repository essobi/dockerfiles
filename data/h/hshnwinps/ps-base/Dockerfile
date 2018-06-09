FROM ubuntu:latest  
MAINTAINER Prof. Dr. Detlef Kreuz <detlef.kreuz@hs-heilbronn.de>  
  
# Switch to german locale  
RUN locale-gen de_DE.UTF-8  
ENV LANG de_DE.UTF-8  
ENV LANGUAGE de_DE:de  
ENV LC_ALL de_DE.UTF-8  
  
# Update base OS and install always needed software  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y mercurial python3-pip vim-nox  
  
# Tox is for automated tests in Python  
RUN pip3 install tox  

