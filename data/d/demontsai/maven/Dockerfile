#######################################################  
# This dockerfile builds a maven environment #  
# #  
# #  
# Author: Demon Tsai #  
# Repository: demontsai/maven:3.3.9 #  
# Version: 1.0 #  
# #  
#######################################################  
  
FROM demontsai/java:jdk7  
  
MAINTAINER Demon Tsai demontsai@estinet.com  
  
  
##### Update system and install apps  
RUN apt-get -qq update  
  
##### Environment  
ENV MVN_VERSION 3.3.9  
ENV MVN_FOLDER_NAME apache-maven-$MVN_VERSION  
ENV MVN_TAR_FILE_NAME $MVN_FOLDER_NAME-bin.tar.gz  
ENV MVN_REPO
http://ftp.tc.edu.tw/pub/Apache/maven/maven-3/$MVN_VERSION/binaries/$MVN_TAR_FILE_NAME  
  
##### Maven install  
WORKDIR installation  
RUN wget $MVN_REPO  
RUN tar xzvf $MVN_TAR_FILE_NAME  
RUN ln -s /root/installation/$MVN_FOLDER_NAME/bin/mvn /usr/bin/mvn  
ENV MAVEN_OPTS '-Xmx2048m -XX:MaxPermSize=1024m'  
WORKDIR /root  
  
##### Clean  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/root/installation/$MVN_TAR_FILE_NAME  

