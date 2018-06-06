FROM rawmind/hms-base:3.5  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
#Set environment  
ENV JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=112 \  
JAVA_VERSION_BUILD=15 \  
JAVA_PACKAGE=jdk \  
ALPINE_GLIBC_BASE_URL="https://github.com/andyshinn/alpine-pkg-
glibc/releases/download" \  
ALPINE_GLIBC_PACKAGE_VERSION="2.23-r3"  
ENV JAVA_HOME=/opt/${JAVA_PACKAGE} \  
PATH=${PATH}:/opt/${JAVA_PACKAGE}/bin \  
LANG=C.UTF-8  
# Download and install glibc and Java  
RUN cd /tmp \  
&& curl -jksSL
"${ALPINE_GLIBC_BASE_URL}/${ALPINE_GLIBC_PACKAGE_VERSION}/glibc-${ALPINE_GLIBC_PACKAGE_VERSION}.apk"
-O \  
&& curl -jksSL
"${ALPINE_GLIBC_BASE_URL}/${ALPINE_GLIBC_PACKAGE_VERSION}/glibc-
bin-${ALPINE_GLIBC_PACKAGE_VERSION}.apk" -O \  
&& curl -jksSL
"${ALPINE_GLIBC_BASE_URL}/${ALPINE_GLIBC_PACKAGE_VERSION}/glibc-i18n-${ALPINE_GLIBC_PACKAGE_VERSION}.apk"
-O \  
&& apk add --update --no-cache --virtual=build-dependencies \  
&& apk add --allow-untrusted glibc-${ALPINE_GLIBC_PACKAGE_VERSION}.apk glibc-
bin-${ALPINE_GLIBC_PACKAGE_VERSION}.apk
glibc-i18n-${ALPINE_GLIBC_PACKAGE_VERSION}.apk \  
&& /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true \  
&& echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh \  
&& echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf \  
&& apk del glibc-i18n && apk del build-dependencies \  
&& curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie"\  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
| gunzip -c - | tar -xf - -C /opt \  
&& ln -s /opt/${JAVA_PACKAGE}1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}
${JAVA_HOME} \  
&& rm -rf ${JAVA_HOME}/*src.zip \  
${JAVA_HOME}/THIRDPARTYLICENSEREADME* \  
${JAVA_HOME}/lib/missioncontrol \  
${JAVA_HOME}/lib/visualvm \  
${JAVA_HOME}/lib/*javafx* \  
${JAVA_HOME}/lib/plugin.jar \  
${JAVA_HOME}/lib/ext/jfxrt.jar \  
${JAVA_HOME}/bin/javaws \  
${JAVA_HOME}/lib/javaws.jar \  
${JAVA_HOME}/lib/desktop \  
${JAVA_HOME}/plugin \  
${JAVA_HOME}/lib/deploy* \  
${JAVA_HOME}/lib/*javafx* \  
${JAVA_HOME}/lib/*jfx* \  
${JAVA_HOME}/lib/amd64/libdecora_sse.so \  
${JAVA_HOME}/lib/amd64/libprism_*.so \  
${JAVA_HOME}/lib/amd64/libfxplugins.so \  
${JAVA_HOME}/lib/amd64/libglass.so \  
${JAVA_HOME}/lib/amd64/libgstreamer-lite.so \  
${JAVA_HOME}/lib/amd64/libjavafx*.so \  
${JAVA_HOME}/lib/amd64/libjfx*.so \  
/var/cache/apk/* \  
/tmp/*  

