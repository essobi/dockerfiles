FROM boardiq/ubuntu:latest  
MAINTAINER BoardIQ <tech@boardintelligence.co.uk>  
  
RUN add-apt-repository ppa:webupd8team/java && apt-get update  
  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN apt-get -y install oracle-java7-installer && apt-get clean  
RUN update-alternatives --display java  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle

