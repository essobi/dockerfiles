# AlpineLinux with a glibc-2.21 and Oracle Java 8  
FROM alpine:latest  
# as shown in:  
# https://developer.atlassian.com/blog/2015/08/minimal-java-docker-containers/  
# Install cURL  
RUN apk --update add curl ca-certificates tar && \  
curl -Ls https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk > /tmp/glibc-2.21-r2.apk && \  
apk add --allow-untrusted /tmp/glibc-2.21-r2.apk && rm -rf /tmp/glibc* && rm
-rf /var/cache/apk/*  
  
# Java Version  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 92  
ENV JAVA_VERSION_BUILD 14  
ENV JAVA_PACKAGE server-jre  
  
# Download and unarchive Java  
RUN mkdir /opt && curl -jksSLH "Cookie: oraclelicense=accept-securebackup-
cookie"\  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
| tar -xzf - -C /opt && ln -s
/opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk  
  
# Set environment  
ENV JAVA_HOME /opt/jdk  
ENV PATH ${PATH}:${JAVA_HOME}/bin  

