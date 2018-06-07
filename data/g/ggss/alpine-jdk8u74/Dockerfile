# Linux alpine 3.3 x86_64 & Oracle Java 8 (8u74-b02-linux-x64) => 172.3 MB  
  
FROM alpine:3.3  
MAINTAINER offer4job@outlook.com  
  
# Setup Java version & environment  
  
ENV JAVA_VERSION="1.8.0_74" \  
JAVA_VERSION_MAJOR="8" \  
JAVA_VERSION_MINOR="74" \  
JAVA_VERSION_BUILD="02" \  
JAVA_PACKAGE="jdk" \  
JAVA_HOME="/opt/jdk" \  
PATH="${PATH}:${JAVA_HOME}/bin" \  
OS_NAME="Linux" \  
OS_ARCH="amd64"  
# Set the proper environment variables  
# Symbolic link to /bin/busybox for missing /bin/bash  
# Update wget, tar, and ca-certificates on the base alpine image  
# Install glibc-2.21 which is a hard dependency of Java 8  
# Hotfix /etc/nsswitch.conf, which is apperently required by glibc and isn't
used in Alpine Linux  
# Download the Oracle JRE/JDK through cookie trick  
# Remove spurious folders not needed (like jdk/jre/lib/desktop and others...)  
  
RUN apk add --update --no-cache --virtual=build-dependencies wget tar ca-
certificates && \  
wget -nv -P /tmp https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk && \  
wget -nv -P /tmp https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-
bin-2.21-r2.apk && \  
apk add --allow-untrusted /tmp/glibc-2.21-r2.apk /tmp/glibc-bin-2.21-r2.apk &&
\  
/usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
mkdir /opt && \  
wget -nv --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
-O /opt/jdk.tar.gz && \  
tar -xf /opt/jdk.tar.gz -C /opt && \  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \  
ln -s /bin/busybox /bin/bash && \  
rm -rf /opt/jdk.tar.gz \  
$JAVA_HOME/*src.zip \  
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
$JAVA_HOME/jre/bin/jjs \  
$JAVA_HOME/jre/bin/keytool \  
$JAVA_HOME/jre/bin/orbd \  
$JAVA_HOME/jre/bin/pack200 \  
$JAVA_HOME/jre/bin/policytool \  
$JAVA_HOME/jre/bin/rmid \  
$JAVA_HOME/jre/bin/rmiregistry \  
$JAVA_HOME/jre/bin/servertool \  
$JAVA_HOME/jre/bin/tnameserv \  
$JAVA_HOME/jre/bin/unpack200 \  
$JAVA_HOME/jre/lib/ext/nashorn.jar \  
$JAVA_HOME/jre/lib/jfr.jar \  
$JAVA_HOME/jre/lib/jfr \  
$JAVA_HOME/jre/lib/oblique-fonts  
  
CMD ["/opt/jdk/bin/java","-version"]  

