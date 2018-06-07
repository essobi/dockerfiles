FROM ubuntu:16.04  
  
MAINTAINER Ismael Cabaas Garcia <ismaelcabanas@gmail.com>  
  
# disable interactive functions  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-get install -y python-software-properties && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get install -y oracle-java8-installer  
#RUN apt-get install software-properties-common  
#RUN apt-get install python-software-properties  
#RUN add-apt-repository ppa:webupd8team/java  
#RUN apt-get update  
#RUN apt-get install oracle-java8-installer  
  

