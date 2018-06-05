##  
# Alpine Linux with a glibc-2.23 and Oracle Java 8  
#  
FROM alpine:3.3  
MAINTAINER Alison Alonso <alisonlba@gmail.com>  
  
##  
# Glibc  
# @see https://github.com/andyshinn/alpine-pkg-glibc  
#  
ENV GLIBC_VERSION 2.23-r1  
  
ADD https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk
/tmp/glibc.apk  
RUN apk add --allow-untrusted /tmp/glibc.apk  
  
##  
# Oracle Java 8  
#  
# Java Version and other ENV  
ENV LANG=C.UTF-8 \  
JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=91 \  
JAVA_PACKAGE=jre  
  
ENV JAVA_HOME=/opt/${JAVA_PACKAGE} \  
PATH=${PATH}:/opt/${JAVA_PACKAGE}/bin  
  
ADD http://javadl.oracle.com/webapps/download/AutoDL?BundleId=207765
/tmp/java.tar.gz  
  
## Discover current Java Version  
#ADD http://javadl.oracle.com/webapps/download/AutoDL?BundleId=207765 /tmp/  
#RUN export JAVA_VERSION_MAJOR=$(basename /tmp/jre-*-linux-x64.tar.gz .tar.gz
| sed 's/.*\\([0-9]\\)u.*/\1/g') && \  
# export JAVA_VERSION_MINOR=$(basename /tmp/jre-*-linux-x64.tar.gz .tar.gz |
sed 's/.*u\\([0-9]\\+\\).*/\1/g')  
# Ins  
RUN apk upgrade --update && \  
apk add --update bash && \  
mkdir /opt && tar -C /opt -xzf /tmp/java.tar.gz && \  
ln -s /opt/${JAVA_PACKAGE}1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}
/opt/${JAVA_PACKAGE} && \  
rm -rf /tmp/* /var/cache/apk/*  

