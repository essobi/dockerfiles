####################################################################################  
# Creates a container with OpenJDK 9  
####################################################################################  
  
# Command reference:  
# docker build -t avanzabank/ubuntu-openjdk9:0.0.1 -t avanzabank/ubuntu-
openjdk9:latest .  
# docker run -it avanzabank/ubuntu-openjdk9 /bin/bash  
  
  
FROM ubuntu:17.04  
RUN apt-get update && apt-get install -y \  
curl \  
wget \  
#ca-certificates-java \  
#openjdk-9-jdk-headless=9~b181-4 && \  
openjdk-9-jdk=9~b161-1 && \  
rm -rf /var/lib/apt/lists  
  
# Fix for bug in openjdk-9-jdk=9~b161-1 packaging  
ENV JAVA_HOME=/usr/lib/jvm/java-9-openjdk-amd64  
RUN bash -c '([[ ! -d $JAVA_SECURITY_DIR ]] && ln -s $JAVA_HOME/lib
$JAVA_HOME/conf) || (echo "Found java conf dir, package has been fixed, remove
this hack"; exit -1)'  
# End fix for bug  
  
WORKDIR /opt  

