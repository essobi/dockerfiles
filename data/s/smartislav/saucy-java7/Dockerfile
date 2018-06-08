FROM stackbrew/ubuntu:saucy  
  
MAINTAINER Ilya Epifanov <elijah.epifanov@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo 'oracle-java7-installer shared/accepted-oracle-license-v1-1 boolean
true' | debconf-set-selections -  
RUN apt-get install -y oracle-java7-set-default  
  

