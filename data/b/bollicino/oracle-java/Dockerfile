FROM ubuntu:18.04  
MAINTAINER Alessandro Poli <alessandro.poli@mondora.com>  
  
# Install Oracle JRE  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  

