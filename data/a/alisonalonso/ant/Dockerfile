##  
# Apache Ant on a alpine linux with jre8  
#  
FROM alisonalonso/java:jdk8  
MAINTAINER Alison Alonso <alisonlba@gmail.com>  
  
# Ant  
ENV ANT_FILENAME=apache-ant-1.9.7 \  
ANT_HOME=/opt/ant \  
PATH=${PATH}:/opt/ant/bin  
  
ADD https://www.apache.org/dist/ant/binaries/${ANT_FILENAME}-bin.tar.bz2
/tmp/ant.tar.bz2  
  
RUN tar -C /opt -xjf /tmp/ant.tar.bz2 && \  
ln -s /opt/${ANT_FILENAME} /opt/ant && \  
rm -rf /tmp/* /var/cache/apk/* /opt/ant/manual/*  

