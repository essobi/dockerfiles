FROM ubuntu:14.04  
MAINTAINER Coordenação de Aperfeiçoamento de Pessoal de Ensino Superior
<dti@capes.gov.br>  
  
# build packages  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -yq build-essential autoconf libtool zlib1g-dev  
RUN apt-get install -yq libcurl4-nss-dev libsasl2-dev  
RUN apt-get install -yq openjdk-6-jdk maven  
RUN apt-get install -yq python-dev python-boto  
RUN apt-get install -yq libsvn-dev libapr1-dev  
RUN apt-get install wget libunwind8 libcurl3 -y  
  
# export environment  
ENV JAVA_HOME /usr/lib/jvm/java-6-openjdk-amd64  
  
# include libmesos on library path  
ENV LD_LIBRARY_PATH /usr/local/lib  
  
  
ADD mesos-0.22.1-rc6.deb /tmp/  
  
RUN dpkg -i /tmp/mesos-0.22.1-rc6.deb  
  
RUN apt-get install -f  
  
#install docker support in container  
RUN wget -qO- https://get.docker.com/ | sh  
  

