#  
# dandelion/sample-tomcat  
#  
FROM dandelion/tomcat:7.0.62-jdk8  
MAINTAINER Thibault Duchateau <thibault.duchateau@gmail.com>  
  
ENV MAVEN_HOME /usr/local/apache-maven-3.2.5  
ENV PATH $MAVEN_HOME/bin:$PATH  
  
# Install utilities and Maven  
# Also prepare the build directory  
RUN apt-get update && \  
apt-get install -y wget unzip && \  
wget -q -nv http://apache.crihan.fr/dist/maven/maven-3/3.2.5/binaries/apache-
maven-3.2.5-bin.zip -P /usr/local && \  
cd /usr/local && \  
unzip apache-maven-3.2.5-bin.zip && \  
rm -f apache-maven-3.2.5-bin.zip && \  
mkdir -p /home/dandelion  

