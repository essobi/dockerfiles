  
# Java-Build Dockerfile  
# VERSION 1.8  
#  
# Pull Alpine Linux stable base image  
FROM quay.io/appelgriebsch/alpine-sdk:3.7  
MAINTAINER Andreas Gerlach <info@appelgriebsch.com>  
LABEL AUTHOR="Andreas Gerlach <info@appelgriebsch.com>"  
LABEL NAME="java-build"  
LABEL VERSION="1.8"  
  
ENV MAVEN_VERSION 3.5.2  
ENV GRADLE_VERSION 4.3.1  
USER root  
RUN \  
cd /tmp && \  
curl -L -o maven-${MAVEN_VERSION}.tar.gz
"http://www.eu.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz" && \  
tar -xzf maven-${MAVEN_VERSION}.tar.gz && \  
cp -R apache-maven*/* /usr/local/ && \  
rm -rf maven.tar.gz apache-maven* && \  
curl -L -o gradle-${GRADLE_VERSION}-bin.zip
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"
&& \  
unzip gradle-${GRADLE_VERSION}-bin.zip && \  
cp -R gradle-*/* /usr/local/ && \  
rm -rf gradle-${GRADLE_VERSION}-bin.zip gradle-* && \  
rm -rf /usr/local/lib/gradle-logging*  
  
# add updated startup-scripts  
COPY scripts/*.sh /tmp/scripts/  
COPY start_instance.sh /tmp/  
RUN \  
chmod 755 /tmp/start_instance.sh  

