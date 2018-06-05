FROM handcraftedbits/nginx-unit:1.1.0  
MAINTAINER HandcraftedBits <opensource@handcraftedbits.com>  
  
ARG GLIBC_VERSION=2.23-r3  
ARG JAVA_VERSION_MAJOR=8  
ARG JAVA_VERSION_MINOR=121  
ARG JAVA_VERSION_BUILD=13  
  
ENV JAVA_HOME /opt/jdk  
ENV LANG C.UTF-8  
ENV PATH ${PATH}:/opt/jdk/bin  
  
RUN apk update && \  
apk add bash ca-certificates curl && \  
  
for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION}
glibc-i18n-${GLIBC_VERSION}; do \  
curl -sSL https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done
&& \  
apk add --allow-untrusted /tmp/*.apk && \  
  
( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true ) && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \  
echo "hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4" >>
/etc/nsswitch.conf && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/java.tar.gz \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/e9e7ea248e2c4826b92b3f075a80e441/jdk-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
&& \  
tar -C /opt -xzvf /tmp/java.tar.gz && \  
mv /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \  
  
apk del ca-certificates curl glibc-i18n && \  
rm -rf ${JAVA_HOME}/*src.zip \  
${JAVA_HOME}/lib/missioncontrol \  
${JAVA_HOME}/lib/visualvm \  
${JAVA_HOME}/lib/*javafx* \  
${JAVA_HOME}/jre/plugin \  
${JAVA_HOME}/jre/bin/javaws \  
${JAVA_HOME}/jre/bin/jjs \  
${JAVA_HOME}/jre/bin/orbd \  
${JAVA_HOME}/jre/bin/pack200 \  
${JAVA_HOME}/jre/bin/policytool \  
${JAVA_HOME}/jre/bin/rmid \  
${JAVA_HOME}/jre/bin/rmiregistry \  
${JAVA_HOME}/jre/bin/servertool \  
${JAVA_HOME}/jre/bin/tnameserv \  
${JAVA_HOME}/jre/bin/unpack200 \  
${JAVA_HOME}/jre/lib/javaws.jar \  
${JAVA_HOME}/jre/lib/deploy* \  
${JAVA_HOME}/jre/lib/desktop \  
${JAVA_HOME}/jre/lib/*javafx* \  
${JAVA_HOME}/jre/lib/*jfx* \  
${JAVA_HOME}/jre/lib/amd64/libdecora_sse.so \  
${JAVA_HOME}/jre/lib/amd64/libprism_*.so \  
${JAVA_HOME}/jre/lib/amd64/libfxplugins.so \  
${JAVA_HOME}/jre/lib/amd64/libglass.so \  
${JAVA_HOME}/jre/lib/amd64/libgstreamer-lite.so \  
${JAVA_HOME}/jre/lib/amd64/libjavafx*.so \  
${JAVA_HOME}/jre/lib/amd64/libjfx*.so \  
${JAVA_HOME}/jre/lib/oblique-fonts \  
${JAVA_HOME}/jre/lib/plugin.jar \  
/tmp/*  

