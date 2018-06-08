FROM java:8-jdk  
MAINTAINER SequenceIQ  
  
RUN cd /usr/local && curl -LO 'http://download.oracle.com/otn-
pub/java/jdk/8u91-b14/jdk-8u91-linux-x64.tar.gz' -H 'Cookie:
oraclelicense=accept-securebackup-cookie'  
RUN cd /usr/local && tar -zxf jdk-8u91-linux-x64.tar.gz  
  
ENV JAVA_HOME /usr/local/jdk1.8.0_91  
ENV PATH $JAVA_HOME/bin:$PATH  

