FROM buildpack-deps:xenial-scm  
  
MAINTAINER Vu Minh Tuan <vuminhtuan@live.com>  
  
# Upgrade system  
RUN \  
apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y autoclean && \  
apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Java Version and other ENV  
ENV JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=162 \  
JAVA_VERSION_BUILD=12 \  
JAVA_PACKAGE=jdk \  
JAVA_HOME=/opt/jdk \  
PATH=${PATH}:/opt/jdk/bin  
  
# Install JDK 8  
RUN set -ex && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/java.tar.gz \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/0da788060d494f5095bf8624735fa2f1/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
&& \  
JAVA_PACKAGE_SHA256=$(curl -sSL
https://www.oracle.com/webfolder/s/digest/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}checksum.html
| grep -E
"${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64\\.tar\\.gz"
| grep -Eo '(sha256: )[^<]+' | cut -d: -f2 | xargs) && \  
echo "${JAVA_PACKAGE_SHA256} /tmp/java.tar.gz" > /tmp/java.tar.gz.sha256 && \  
sha256sum -c /tmp/java.tar.gz.sha256 && \  
gunzip /tmp/java.tar.gz && \  
tar -C /opt -xf /tmp/java.tar && \  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \  
rm -rf /tmp/*  
  
# EOF  

