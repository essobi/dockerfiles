FROM debian:latest  
  
# Install Oracle JDK 8  
ENV VERSION 8  
ENV UPDATE 45  
ENV BUILD 14  
ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-oracle  
  
RUN apt-get update && apt-get install ca-certificates curl -y && \  
curl --silent --location --retry 3 --cacert
/etc/ssl/certs/GeoTrust_Global_CA.pem \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/jdk-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz
\  
| tar xz -C /tmp && \  
mkdir -p /usr/lib/jvm && mv /tmp/jdk1.${VERSION}.0_${UPDATE} "${JAVA_HOME}" &&
\  
apt-get autoclean && apt-get --purge -y autoremove && \  
rm "${JAVA_HOME}/javafx-src.zip" && \  
rm "${JAVA_HOME}/src.zip" && \  
rm -rf "${JAVA_HOME}/lib/missioncontrol" \  
"${JAVA_HOME}/lib/visualvm" \  
"${JAVA_HOME}/lib/*javafx*" \  
"${JAVA_HOME}/jre/lib/plugin.jar" \  
"${JAVA_HOME}/jre/lib/ext/jfxrt.jar" \  
"${JAVA_HOME}/jre/bin/javaws" \  
"${JAVA_HOME}/jre/lib/javaws.jar" \  
"${JAVA_HOME}/jre/lib/desktop" \  
"${JAVA_HOME}/jre/plugin" \  
"${JAVA_HOME}/jre/lib/deploy*" \  
"${JAVA_HOME}/jre/lib/*javafx*" \  
"${JAVA_HOME}/jre/lib/*jfx*" \  
"${JAVA_HOME}/jre/lib/amd64/libdecora_sse.so" \  
"${JAVA_HOME}/jre/lib/amd64/libprism_*.so" \  
"${JAVA_HOME}jre/lib/amd64/libfxplugins.so" \  
"${JAVA_HOME}/jre/lib/amd64/libglass.so" \  
"${JAVA_HOME}/jre/lib/amd64/libgstreamer-lite.so" \  
"${JAVA_HOME}/jre/lib/amd64/libjavafx*.so" \  
"${JAVA_HOME}/jre/lib/amd64/libjfx*.so" && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN update-alternatives --install "/usr/bin/java" "java"
"${JAVA_HOME}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"${JAVA_HOME}/bin/javaws" 1 && \  
update-alternatives --install "/usr/bin/javac" "javac"
"${JAVA_HOME}/bin/javac" 1 && \  
update-alternatives --set java "${JAVA_HOME}/bin/java" && \  
update-alternatives --set javaws "${JAVA_HOME}/bin/javaws" && \  
update-alternatives --set javac "${JAVA_HOME}/bin/javac"

