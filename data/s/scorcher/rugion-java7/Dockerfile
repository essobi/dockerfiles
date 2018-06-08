FROM ubuntu:14.04  
  
MAINTAINER Nikolay Didenko "nd@info74.ru"  
# Install java7  
RUN apt-get install -y software-properties-common && add-apt-repository -y
ppa:webupd8team/java && apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java7-installer  
  
# Cleaning  
RUN apt-get clean  
  

