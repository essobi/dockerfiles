FROM alpine:3.2  
  
MAINTAINER Aldrin Leal <aldrin@leal.eng.br>  
  
RUN apk --update add curl ca-certificates tar supervisor && \  
curl -Ls https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk > /tmp/glibc-2.21-r2.apk && \  
apk add --allow-untrusted /tmp/glibc-2.21-r2.apk  
  
# Java Version  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 60  
ENV JAVA_VERSION_BUILD 27  
ENV JAVA_PACKAGE jdk  
  
# Download and unarchive Java  
RUN mkdir /opt && curl -jksSLH "Cookie: oraclelicense=accept-securebackup-
cookie"\  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
| tar -xzf - -C /opt &&\  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk &&\  
mkdir -p /opt/jdk/lib/security &&\  
rm -rf /opt/jdk/*src.zip \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/lib/*javafx* \  
/opt/jdk/jre/lib/plugin.jar \  
/opt/jdk/jre/lib/ext/jfxrt.jar \  
/opt/jdk/jre/bin/javaws \  
/opt/jdk/jre/lib/javaws.jar \  
/opt/jdk/jre/lib/desktop \  
/opt/jdk/jre/plugin \  
/opt/jdk/jre/lib/deploy* \  
/opt/jdk/jre/lib/*javafx* \  
/opt/jdk/jre/lib/*jfx* \  
/opt/jdk/jre/lib/amd64/libdecora_sse.so \  
/opt/jdk/jre/lib/amd64/libprism_*.so \  
/opt/jdk/jre/lib/amd64/libfxplugins.so \  
/opt/jdk/jre/lib/amd64/libglass.so \  
/opt/jdk/jre/lib/amd64/libgstreamer-lite.so \  
/opt/jdk/jre/lib/amd64/libjavafx*.so \  
/opt/jdk/jre/lib/amd64/libjfx*.so  
  
RUN POLICY_DIR="UnlimitedJCEPolicyJDK${JAVA_VERSION_MAJOR}" \  
&& curl -s -k -L -C - -b "oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip >
/tmp/policy.zip \  
&& cd /tmp \  
&& unzip /tmp/policy.zip \  
&& mv /tmp/$POLICY_DIR/*.jar /opt/jdk/lib/security/ \  
&& rm -rf /tmp/*  
  
# Set environment  
ENV JAVA_HOME /opt/jdk  
ENV PATH ${PATH}:${JAVA_HOME}/bin  

