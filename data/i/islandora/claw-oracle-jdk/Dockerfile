FROM islandora/claw-base  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "Description"="Base Java for Islandora CLAW" \  
"License"="MIT" \  
"Version"="0.0.1"  
  
ARG JAVA_VERSION=8.72.15  
  
ENV JAVA_HOME=/opt/jdk \  
JAVA_OPTS="" \  
PATH=${PATH}:/opt/jdk/bin  
  
# We remove a lot of libs and features which are not needed to reduce the size  
# of the image.  
RUN JAVA_MAJOR=${JAVA_VERSION%%.*} && JAVA_MINOR=$(echo ${JAVA_VERSION} | cut
-d. -f2) && JAVA_BUILD=${JAVA_VERSION#*.*.} && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR}u${JAVA_MINOR}-b${JAVA_BUILD}/jdk-${JAVA_MAJOR}u${JAVA_MINOR}-linux-x64.tar.gz
| \  
tar -xzf - -C /opt && \  
mv /opt/jdk1.${JAVA_MAJOR}.0_${JAVA_MINOR} /opt/jdk && \  
chown -R root:root /opt/jdk && \  
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
/opt/jdk/jre/lib/amd64/libjfx*.so \  
/opt/jdk/man && \  
cleanup  

