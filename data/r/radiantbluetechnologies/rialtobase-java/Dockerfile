# radiantbluetechnologies/rialtobase-java  
FROM radiantbluetechnologies/rialtobase-centos  
MAINTAINER mpg@flaxen.com  
  
# Prepare environment  
ENV JAVA_HOME /opt/java  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# Install Oracle Java7  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jdk/7u71-b14/jdk-7u71-linux-x64.tar.gz
&& \  
tar -xvf jdk-7u71-linux-x64.tar.gz && \  
rm jdk*.tar.gz && \  
mv jdk* ${JAVA_HOME}  

