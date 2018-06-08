FROM ubuntu:14.04  
  
RUN apt-get update  
RUN apt-get install software-properties-common -y  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN apt-get install oracle-java8-installer -y  
RUN apt-get install oracle-java8-set-default  
  
RUN mkdir /home/check  

