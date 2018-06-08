FROM debian:jessie  
  
MAINTAINER Nicolas Dupont <nidupont@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8 && \  
apt-get remove -y locales  
  
ENV LANG C.UTF-8  
  
ENV JAVA_VERSION_MAJOR=7 \  
JAVA_VERSION_MINOR=79 \  
JAVA_VERSION_BUILD=15 \  
JAVA_PACKAGE=jdk  
  
RUN apt-get update -q && \  
apt-get install -q -y \--no-install-recommends ca-certificates wget && \  
mkdir -p /opt/jalios/downloads/oracle-jdk && \  
mkdir -p /opt/jalios/components/oracle-jdk && \  
mkdir -p /opt/jalios/instances/jvm && \  
wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
-O /opt/jalios/downloads/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz && \  
tar -xvf
/opt/jalios/downloads/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
-C /opt/jalios/components/oracle-jdk/ && \  
ln -s /opt/jalios/components/oracle-
jdk/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}
/opt/jalios/instances/jvm/jdk7 && \  
apt-get remove \--purge -y ca-certificates wget && \  
apt-get autoremove --purge -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

