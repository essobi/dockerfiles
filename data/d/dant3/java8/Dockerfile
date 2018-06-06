FROM ubuntu:16.04  
  
MAINTAINER Viacheslav Blinov "blinov.vyacheslav@gmail.com"  
# Install java8  
# -1. update repositories  
RUN apt-get update  
# 0. install add-apt-repository  
RUN apt-get install -y software-properties-common  
# 1. Add repository to install oracle jdk:  
RUN add-apt-repository -y ppa:webupd8team/java && apt-get update  
# 2. Accept the license beforehand  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
# 3. run installer  
RUN apt-get install -y --force-yes oracle-java8-installer  

