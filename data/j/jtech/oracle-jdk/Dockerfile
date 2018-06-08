## Alpine Linux with a glibc-2.21 and Oracle Java 8  
  
FROM alpine:3.3  
  
MAINTAINER Terrence Miao <TerrenceMiao@users.noreply.github.com>  
  
## Install cURL, ca-certifications, tar then install glibc library  
## Original https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk now returns HTTP 404  
RUN apk --update add curl ca-certificates tar && \  
curl -Ls https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.21-r2/glibc-2.21-r2.apk > /tmp/glibc-2.21-r2.apk &&
\  
apk add --allow-untrusted /tmp/glibc-2.21-r2.apk && \  
rm /tmp/glibc-2.21-r2.apk  
  
## Alpine Linux doesn't use pam, which means that there is no
/etc/nsswitch.conf,  
## but Java relies on /etc/nsswitch.conf to check the order of DNS resolving  
## (i.e. check /etc/hosts first and then lookup DNS-servers).  
## To fix this we just create /etc/nsswitch.conf and add the following line:  
RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
  
## Java Version  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 131  
ENV JAVA_VERSION_BUILD 11  
ENV JAVA_PACKAGE jdk  
ENV JAVA_CHECKSUM d54c1d3a095b4ff2b6607d096fa80163  
  
## Download and install Java  
RUN curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie"\  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_CHECKSUM}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
| tar -xzf - -C /usr/local && \  
ln -s /usr/local/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}
/usr/local/jdk && \  
rm -rf /usr/local/jdk/*src.zip \  
/usr/local/jdk/lib/missioncontrol \  
/usr/local/jdk/lib/visualvm \  
/usr/local/jdk/lib/*javafx* \  
/usr/local/jdk/jre/lib/plugin.jar \  
/usr/local/jdk/jre/lib/ext/jfxrt.jar \  
/usr/local/jdk/jre/bin/javaws \  
/usr/local/jdk/jre/lib/javaws.jar \  
/usr/local/jdk/jre/lib/desktop \  
/usr/local/jdk/jre/plugin \  
/usr/local/jdk/jre/lib/deploy* \  
/usr/local/jdk/jre/lib/*javafx* \  
/usr/local/jdk/jre/lib/*jfx* \  
/usr/local/jdk/jre/lib/amd64/libdecora_sse.so \  
/usr/local/jdk/jre/lib/amd64/libprism_*.so \  
/usr/local/jdk/jre/lib/amd64/libfxplugins.so \  
/usr/local/jdk/jre/lib/amd64/libglass.so \  
/usr/local/jdk/jre/lib/amd64/libgstreamer-lite.so \  
/usr/local/jdk/jre/lib/amd64/libjavafx*.so \  
/usr/local/jdk/jre/lib/amd64/libjfx*.so  
## Set JAVA_HOME environment  
ENV JAVA_HOME /usr/local/jdk  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
## Set up Locale  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  

