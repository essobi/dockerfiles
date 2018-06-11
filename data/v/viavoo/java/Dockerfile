FROM phusion/baseimage:0.9.22  
RUN add-apt-repository ppa:openjdk-r/ppa -y  
RUN apt-get update && apt-get install -y curl openjdk-8-jdk && rm -rf
/var/lib/apt/lists/*  
RUN echo 'JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"' >>/etc/environment  
ENV JAVA_HOME "/usr/lib/jvm/java-8-openjdk-amd64"  

