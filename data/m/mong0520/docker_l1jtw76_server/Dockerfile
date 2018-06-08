# ubuntu-openjdk-8-jdk  
#  
# VERSION 0.0.3  
#  
# Extends ubuntu-base with java 8 openjdk jdk installation  
#  
FROM ubuntu:16.04  
# This is in accordance to :
https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-
get-on-ubuntu-16-04  
ENV LANG C.UTF-8  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jdk  
RUN apt-get install -y vim  
RUN apt-get install -y telnet  
  
ADD L1J-TW_7.6.tar.gz /opt/l1jtw/  
ADD config/* /opt/l1jtw/L1J-TW_7.6/config/  
  
# Setup JAVA_HOME, this is useful for docker commandline  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
RUN export JAVA_HOME  
  
ARG L1JDB_HOST  
ARG L1JDB_ACCOUNT  
ARG L1JDB_PASSWORD  
  
RUN sed -i s/L1JDB_HOST/${L1JDB_HOST}/
/opt/l1jtw/L1J-TW_7.6/config/server.properties  
RUN sed -i s/L1JDB_ACCOUNT/${L1JDB_ACCOUNT}/
/opt/l1jtw/L1J-TW_7.6/config/server.properties  
RUN sed -i s/L1JDB_PASSWORD/${L1JDB_PASSWORD}/
/opt/l1jtw/L1J-TW_7.6/config/server.properties  
CMD ["/bin/bash"]  

