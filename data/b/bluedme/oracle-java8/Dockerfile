# There is no official dockerhub with oracle java  
# this file is inspired from
https://github.com/dockerfile/java/blob/master/oracle-java8/Dockerfile  
  
FROM ubuntu:14.04  
MAINTAINER bluedme  
  
ENV VER 8u72  
  
RUN apt-get update && \  
apt-get install -y software-properties-common  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Define default command.  
CMD ["bash"]  

