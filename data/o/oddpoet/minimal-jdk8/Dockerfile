#==============================================================================  
# minimal JDK8  
#==============================================================================  
# ubuntu 베이스로 변경한다. (LTS 버전)  
FROM ubuntu:16.04  
MAINTAINER yunsang.choi<oddpoet@gmail.com>  
  
# Java Version  
ENV JAVA_MAJOR_VERSION 8  
ENV JAVA_UPDATE_VERSION 162  
ENV JAVA_BUILD_VERSION 12  
ENV JDK_VERSION ${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}  
ENV JAVA_VERSION
1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_VERSION}  
ENV JAVA_PACKAGE jdk  
  
# prepare basic utils  
RUN apt-get update;  
RUN apt-get install -y curl zip unzip tar locales  
## locale 설정 : 한글  
RUN rm -rf /var/lib/apt/lists/* \  
&& localedef -i ko_KR -c -f UTF-8 -A /usr/share/locale/locale.alias
ko_KR.UTF-8  
ENV LANG ko_KR.utf8  
  
#--------------------------------------------------------------------------------  
# NOTICE:  
# I do not use sdkman to install jdk.  
# If jdk was installed by sdkman, docker image size will be larger then 700MB.  
#--------------------------------------------------------------------------------  
# Download and unarchive Java  
RUN mkdir -p /opt && curl -jksSLH "Cookie: oraclelicense=accept-securebackup-
cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_VERSION}/0da788060d494f5095bf8624735fa2f1/${JAVA_PACKAGE}-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz
\  
| tar -xzf - -C /opt &&\  
ln -s /opt/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION} /opt/jdk && \  
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
# Set environment  
ENV JAVA_HOME /opt/jdk  
ENV PATH ${PATH}:${JAVA_HOME}/bin  

