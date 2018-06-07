FROM debian:jessie  
  
MAINTAINER Jakub Kulhan <jakub.kulhan@gmail.com>  
  
ENV JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=74 \  
JAVA_VERSION_BUILD=02 \  
JAVA_PACKAGE=jdk \  
JAVA_HOME=/opt/jdk \  
PATH=${PATH}:/opt/jdk/bin \  
LANG=C.UTF-8  
  
RUN set -ex && \  
apt-get update && \  
apt-get install -y curl ca-certificates && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/java.tar.gz \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
&& \  
tar -C /opt -xzf /tmp/java.tar.gz && \  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \  
apt-get remove -y curl && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

