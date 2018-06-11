FROM lsiobase/alpine  
  
MAINTAINER xeroxmalf  
  
# set versions  
ARG BUILD_DATE  
ARG VERSION  
ARG BUILD_CORES  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
# set env  
ENV PKG_CONFIG_PATH=/usr/local/lib/pkgconfig  
ENV JAVA_HOME /opt/jdk  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
# install runtime packages  
RUN NB_CORES=${BUILD_CORES-`getconf _NPROCESSORS_CONF`} && \  
apk add --no-cache \  
ca-certificates \  
wget \  
dtach \  
tar && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk -O /tmp/glibc-2.25-r0.apk &&
\  
apk add --allow-untrusted --no-cache /tmp/glibc-2.25-r0.apk && \  
  
# install jre  
mkdir /opt && \  
cd /opt && \  
wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u121-linux-x64.tar.gz
&& \  
tar xvf jdk-8u121-linux-x64.tar.gz && \  
rm jdk-8u121-linux-x64.tar.gz && \  
cd jdk1.8.0_121 && \  
ln -s /opt/jdk1.8.0_121/ /opt/jdk && \  
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
/opt/jdk/jre/lib/amd64/libjfx*.so && \  
# clean up  
rm -rf \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 25565  
VOLUME /config  

