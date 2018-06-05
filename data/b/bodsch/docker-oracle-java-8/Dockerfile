  
FROM alpine:3.6  
  
MAINTAINER Bodo Schulz <bodo@boone-schulz.de>  
  
ENV \  
ALPINE_MIRROR="dl-cdn.alpinelinux.org" \  
ALPINE_VERSION="v3.6" \  
TERM=xterm \  
BUILD_DATE="2017-06-02" \  
JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=131 \  
JAVA_VERSION_BUILD=11 \  
JAVA_ID="d54c1d3a095b4ff2b6607d096fa80163" \  
JAVA_PACKAGE=jdk \  
JAVA_HOME=/opt/jdk \  
PATH=${PATH}:/opt/jdk/bin \  
GLIBC_VERSION=2.23-r3 \  
LANG=C.UTF-8 \  
APK_ADD="ca-certificates curl libstdc++"  
  
LABEL \  
version="1706-01" \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="Oracle Java Docker Image" \  
org.label-schema.description="Inofficial Oracle Java Docker Image" \  
org.label-schema.url="https://www.icinga.org/" \  
org.label-schema.vcs-url="https://github.com/bodsch/docker-docker-oracle-
java-8" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-
schema.version=1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}
\  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="GNU General Public License v3.0"  
#
---------------------------------------------------------------------------------------------------------------------  
  
RUN \  
echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/main" >
/etc/apk/repositories && \  
echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/community" >>
/etc/apk/repositories && \  
apk --quiet --no-cache update && \  
apk --quiet --no-cache upgrade && \  
for apk in ${APK_ADD} ; \  
do \  
apk --quiet --no-cache add ${apk} ; \  
done && \  
for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION}
glibc-i18n-${GLIBC_VERSION} ; \  
do \  
curl \  
\--silent \  
\--insecure \  
\--location \  
\--output /tmp/${pkg}.apk \  
https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk ; \  
done && \  
apk add --allow-untrusted /tmp/*.apk && \  
mkdir /opt && \  
rm -v /tmp/*.apk && \  
( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
${LANG} || true ) && \  
echo "export LANG=${LANG}" > /etc/profile.d/locale.sh && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \  
# http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz  
curl \  
\--location \  
\--retry 3 \  
\--cacert /etc/ssl/certs/ca-certificates.crt \  
\--junk-session-cookies \  
\--insecure \  
\--show-error \  
\--location \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_ID}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
| gunzip \  
| tar x -C /opt/ && \  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \  
sed -i s/#networkaddress.cache.ttl=-1/networkaddress.cache.ttl=30/
${JAVA_HOME}/jre/lib/security/java.security && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
apk --purge del \  
ca-certificates \  
curl && \  
rm -rf /opt/jdk/*src.zip \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/lib/*javafx* \  
/opt/jdk/jre/plugin \  
/opt/jdk/jre/bin/javaws \  
/opt/jdk/jre/bin/jjs \  
/opt/jdk/jre/bin/orbd \  
/opt/jdk/jre/bin/pack200 \  
/opt/jdk/jre/bin/policytool \  
/opt/jdk/jre/bin/rmid \  
/opt/jdk/jre/bin/rmiregistry \  
/opt/jdk/jre/bin/servertool \  
/opt/jdk/jre/bin/tnameserv \  
/opt/jdk/jre/bin/unpack200 \  
/opt/jdk/jre/lib/javaws.jar \  
/opt/jdk/jre/lib/deploy* \  
/opt/jdk/jre/lib/desktop \  
/opt/jdk/jre/lib/*javafx* \  
/opt/jdk/jre/lib/*jfx* \  
/opt/jdk/jre/lib/amd64/libdecora_sse.so \  
/opt/jdk/jre/lib/amd64/libprism_*.so \  
/opt/jdk/jre/lib/amd64/libfxplugins.so \  
/opt/jdk/jre/lib/amd64/libglass.so \  
/opt/jdk/jre/lib/amd64/libgstreamer-lite.so \  
/opt/jdk/jre/lib/amd64/libjavafx*.so \  
/opt/jdk/jre/lib/amd64/libjfx*.so \  
/opt/jdk/jre/lib/oblique-fonts \  
/opt/jdk/jre/lib/plugin.jar \  
/tmp/* \  
/var/cache/apk/*  
  
CMD [ "/bin/sh" ]  
  
#
---------------------------------------------------------------------------------------------------------------------  

