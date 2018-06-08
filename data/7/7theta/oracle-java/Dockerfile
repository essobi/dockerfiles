FROM alpine:3.4  
MAINTAINER Achint Sandhu <sandhu@7theta.com>  
  
# Java Version  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 102  
ENV JAVA_VERSION_BUILD 14  
ENV JAVA_PACKAGE jre  
ENV GLIBC_VERSION 2.23-r3  
  
RUN apk add --no-cache curl  
  
# Install glibc (required for java)  
RUN curl -jsSL -o /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
curl -jsSL -O https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \  
apk add glibc-${GLIBC_VERSION}.apk  
  
# Install Java  
RUN mkdir /opt && \  
curl -jsSL -H "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
| tar -xzf - -C /opt && \  
ln -s /opt/${JAVA_PACKAGE}1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}
/opt/${JAVA_PACKAGE} && \  
cd /opt/${JAVA_PACKAGE}/ && rm -rf *src.zip lib/missioncontrol lib/visualvm
lib/plugin.jar plugin lib/*javafx* lib/*jfx* lib/ext/jfxrt.jar bin/javaws
lib/javaws.jar lib/desktop lib/deploy* lib/amd64/libdecora_sse.so
lib/amd64/libprism_*.so lib/amd64/libfxplugins.so lib/amd64/libglass.so
lib/amd64/libgstreamer-lite.so lib/amd64/libjavafx*.so lib/amd64/libjfx*.  
  
# Install Java Cryptography Extension (JCE) Unlimited Strength  
RUN curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/jce_policy.zip \  
http://download.oracle.com/otn-
pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip && \  
unzip -o -d /opt/${JAVA_PACKAGE}/lib/security /tmp/jce_policy.zip && rm -f
/tmp/jce_policy.zip  
  
RUN apk del curl  
  
ENV PATH /opt/jre/bin:${PATH}  
  
ENTRYPOINT ["java"]  
CMD ["-version"]  
  

