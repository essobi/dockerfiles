# Set the base image  
FROM google/cloud-sdk:174.0.0  
# Dockerfile author / maintainer  
MAINTAINER erds erds@badmoondev.com  
  
RUN echo "deb http://http.debian.net/debian jessie-backports main" | tee
--append /etc/apt/sources.list.d/jessie-backports.list > /dev/null \  
&& apt-get update \  
&& apt-get install -t jessie-backports openjdk-8-jdk -y \  
&& update-java-alternatives -s java-1.8.0-openjdk-amd64  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  

