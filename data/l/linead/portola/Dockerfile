FROM alpine:3.5  
MAINTAINER "Daniel Fullarton" <linead@gmail.com>  
  
RUN apk add --no-cache curl  
  
RUN curl
http://download.java.net/java/jdk9-alpine/archive/171/binaries/jdk-9-ea+171_linux-x64-musl_bin.tar.gz
-o /tmp/java.tar.gz && mkdir /usr/local/java && cd /usr/local/java && tar xf
/tmp/java.tar.gz && ln -s /usr/local/java/jdk-9/bin/* /usr/local/bin && rm
/usr/local/java/jdk-9/lib/src.zip && rm /tmp/java.tar.gz  
  
ENV JAVA_HOME /usr/local/java/jdk-9  

