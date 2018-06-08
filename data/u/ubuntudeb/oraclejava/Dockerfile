#!/usr/bin/docker  
FROM ubuntu:14.04  
MAINTAINER Matt Chapman <Matt@NinjitsuWeb.com>  
  
RUN echo /usr/bin/debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository ppa:webupd8team/java  
  
RUN apt-get update  
RUN apt-get install -y oracle-java8-installer  

