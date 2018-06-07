  
# Oracle Java 7 Dockerfile on Ubuntu 12.04 LTS (Precise Pangolin)  
FROM ubuntu:12.04  
MAINTAINER Dan Kim "https://github.com/deekim"  
#########  
# setup #  
#########  
# update & update  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y upgrade  
  
# java install dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-software-
properties  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-
common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y upgrade  
  
# accept oracle license  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# install java  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java7-installer  
RUN update-alternatives --display java  
  
# set java environment variables  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java7-set-default  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
# cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

