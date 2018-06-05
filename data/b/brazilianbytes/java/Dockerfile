#  
# Oracle Java 8 JRE Server Dockerfile, by BrazilianBytes  
#  
# https://github.com/brazilianbytes/java  
# https://github.com/brazilianbytes/java/tree/master/oracle-java-8-server-jre  
#  
# Pull base image.  
FROM ubuntu:latest  
MAINTAINER Luciano Jesus Lima <developer@brazilianbytes.com>  
  
# Install Java.  
RUN apt-get update  
RUN apt-get -y install wget tar  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u25-b17/server-jre-8u25-linux-x64.tar.gz  
RUN mkdir -p /env/jdk  
RUN tar -xzf server-jre-8u25-linux-x64.tar.gz -C /env/jdk jdk1.8.0_25 --strip
1  
RUN apt-get clean  
RUN rm server-jre-8u25-linux-x64.tar.gz  
  
# Define working directory.  
WORKDIR /env/jdk  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /env/jdk  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# Define default command.  
CMD ["bash"]

