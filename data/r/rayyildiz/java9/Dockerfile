FROM ubuntu:17.04  
# Java Version  
ENV JAVA_VERSION=9.0.1 \  
JAVA_BUILD=11 \  
JAVA_HOME=/usr/lib/jvm/current-java  
  
# Openjdk
http://download.java.net/java/GA/jdk9/9.0.1/binaries/openjdk-9.0.1_linux-x64_bin.tar.gz  
  
RUN apt-get update -y && apt-get upgrade -y  
  
RUN apt-get install wget tar bash -y  
  
RUN cd /tmp && \  
wget
"http://download.java.net/java/GA/jdk9/${JAVA_VERSION}/binaries/openjdk-${JAVA_VERSION}_linux-x64_bin.tar.gz"
&& \  
tar xzf "openjdk-${JAVA_VERSION}_linux-x64_bin.tar.gz" && \  
mkdir -p /usr/lib/jvm && mv "/tmp/jdk-${JAVA_VERSION}"
"/usr/lib/jvm/openjdk-${JAVA_VERSION}" && \  
ln -s "openjdk-${JAVA_VERSION}" $JAVA_HOME && \  
ln -s $JAVA_HOME/bin/java /usr/bin/java && \  
ln -s $JAVA_HOME/bin/javac /usr/bin/javac && \  
ln -s $JAVA_HOME/bin/jshell /usr/bin/jshell  
  
RUN rm -rf $JAVA_HOME/*.txt && \  
rm -rf $JAVA_HOME/*.html && \  
rm -rf $JAVA_HOME/man && \  
rm -rf $JAVA_HOME/lib/src.zip && \  
rm /tmp/*  
  
RUN apt-get remove --purge wget -y && apt-get clean  

