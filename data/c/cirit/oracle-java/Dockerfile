FROM debian:jessie  
  
MAINTAINER Cagdas Cirit <cagdascirit@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV VERSION 8  
ENV UPDATE 60  
ENV BUILD 27  
ENV JAVA_VERSION ${VERSION}u${UPDATE}  
  
RUN echo "deb http://httpredir.debian.org/debian stretch main contrib" | tee
-a /etc/apt/sources.list  
  
RUN apt-get -y update && \  
apt-get -y install \  
wget \  
java-package  
  
RUN useradd javjav && \  
mkdir javjavws && \  
chown javjav:javjav javjavws && \  
cd javjavws && \  
wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}-b${BUILD}/jdk-${JAVA_VERSION}-linux-x64.tar.gz &&
\  
runuser -l javjav -c "yes Y | fakeroot make-jpkg
jdk-${JAVA_VERSION}-linux-x64.tar.gz" && \  
dpkg -i oracle-java${VERSION}-jdk_${JAVA_VERSION}_amd64.deb  
  
RUN sed -i '$ d' /etc/apt/sources.list && \  
rm -rf javjavws && \  
userdel javjav && \  
apt-get -y remove wget && \  
apt-get -y remove java-package && \  
apt-get -y --purge autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV JAVA_HOME /usr/lib/jvm/jdk-${VERSION}-oracle-x64  
ENV JRE_HOME ${JAVA_HOME}/jre  
  
ENV LANG en_US.UTF-8  

