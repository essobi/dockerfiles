FROM ubuntu:14.04  
MAINTAINER Francesco Pontillo <francescopontillo@gmail.com>  
  
RUN apt-get update -y && apt-get install -y \  
software-properties-common  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN add-apt-repository ppa:webupd8team/java -y \  
&& apt-get update -y && apt-get install -y \  
oracle-java7-installer \  
oracle-java7-set-default  

