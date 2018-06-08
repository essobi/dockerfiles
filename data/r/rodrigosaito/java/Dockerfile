FROM alpine:3.3  
# Java Version  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 66  
ENV JAVA_VERSION_BUILD 17  
ENV JAVA_PACKAGE jdk  
  
# Set environment  
ENV JAVA_BASE_PATH /usr/lib/jvm  
ENV JAVA_HOME ${JAVA_BASE_PATH}/jdk  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
# Install Java  
RUN apk --update --virtual=build-dependencies add curl ca-certificates tar &&
\  
curl -Ls https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk > /tmp/glibc-2.21-r2.apk && \  
apk add --allow-untrusted /tmp/glibc-2.21-r2.apk && \  
/usr/glibc/usr/bin/ldconfig "/lib" "/usr/glibc/usr/lib" && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
mkdir $JAVA_BASE_PATH && curl -jksSLH "Cookie: oraclelicense=accept-
securebackup-cookie"\  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
| tar -xzf - -C $JAVA_BASE_PATH &&\  
ln -s $JAVA_BASE_PATH/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}
$JAVA_HOME &&\  
rm -rf $JAVA_HOME/*src.zip \  
$JAVA_HOME/lib/missioncontrol \  
$JAVA_HOME/lib/visualvm \  
$JAVA_HOME/lib/*javafx* \  
$JAVA_HOME/jre/lib/plugin.jar \  
$JAVA_HOME/jre/lib/ext/jfxrt.jar \  
$JAVA_HOME/jre/bin/javaws \  
$JAVA_HOME/jre/lib/javaws.jar \  
$JAVA_HOME/jre/lib/desktop \  
$JAVA_HOME/jre/plugin \  
$JAVA_HOME/jre/lib/deploy* \  
$JAVA_HOME/jre/lib/*javafx* \  
$JAVA_HOME/jre/lib/*jfx* \  
$JAVA_HOME/jre/lib/amd64/libdecora_sse.so \  
$JAVA_HOME/jre/lib/amd64/libprism_*.so \  
$JAVA_HOME/jre/lib/amd64/libfxplugins.so \  
$JAVA_HOME/jre/lib/amd64/libglass.so \  
$JAVA_HOME/jre/lib/amd64/libgstreamer-lite.so \  
$JAVA_HOME/jre/lib/amd64/libjavafx*.so \  
$JAVA_HOME/jre/lib/amd64/libjfx*.so \  
&& apk del build-dependencies  

