# Docker baseimage with jdk8 on alpine 3.3 and S6+dnsmasq and Timezone CET  
FROM alpine:3.3  
  
ENV S6_VERSION=v1.17.1.1 \  
GODNSMASQ_VERSION=0.9.8  
# Java Version and other ENV  
ENV JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=72 \  
JAVA_VERSION_BUILD=15 \  
JAVA_PACKAGE=jdk \  
JAVA_HOME=/opt/jdk \  
PATH=${PATH}:/opt/jdk/bin \  
LANG=C.UTF-8  
  
RUN apk add --update wget \  
&& wget https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz
--no-check-certificate --quiet -O /tmp/s6-overlay.tar.gz \  
&& wget https://github.com/janeczku/go-
dnsmasq/releases/download/${GODNSMASQ_VERSION}/go-dnsmasq-min_linux-amd64
--no-check-certificate --quiet -O /usr/sbin/go-dnsmasq \  
&& chmod +x /usr/sbin/go-dnsmasq \  
&& tar xvfz /tmp/s6-overlay.tar.gz -C / \  
&& rm -f /tmp/s6-overlay.tar.gz \  
&& apk del wget \  
&& rm -rf /var/cache/apk/*  
  
  
COPY rootfs /  
  
# do all in one step  
RUN apk upgrade --update && \  
apk add --update curl ca-certificates bash && \  
curl -L -o /tmp/glibc-2.21-r2.apk "https://circle-
artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-
pkg-glibc/packages/x86_64/glibc-2.21-r2.apk" && \  
apk add --allow-untrusted /tmp/glibc-2.21-r2.apk && \  
curl -L -o /tmp/glibc-bin-2.21-r2.apk "https://circle-
artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-
pkg-glibc/packages/x86_64/glibc-bin-2.21-r2.apk" && \  
apk add --allow-untrusted /tmp/glibc-bin-2.21-r2.apk && \  
/usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \  
mkdir /opt && curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie"
-o /tmp/java.tar.gz \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
&& \  
gunzip /tmp/java.tar.gz && \  
tar -C /opt -xf /tmp/java.tar && \  
apk del curl && \  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \  
rm -rf /opt/jdk/*src.zip \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/lib/*javafx* \  
/opt/jdk/jre/plugin \  
/opt/jdk/jre/bin/javaws \  
/opt/jdk/jre/bin/jjs \  
/opt/jdk/jre/bin/keytool \  
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
/opt/jdk/jre/lib/jfr* \  
/opt/jdk/jre/lib/amd64/libdecora_sse.so \  
/opt/jdk/jre/lib/amd64/libprism_*.so \  
/opt/jdk/jre/lib/amd64/libfxplugins.so \  
/opt/jdk/jre/lib/amd64/libglass.so \  
/opt/jdk/jre/lib/amd64/libgstreamer-lite.so \  
/opt/jdk/jre/lib/amd64/libjavafx*.so \  
/opt/jdk/jre/lib/amd64/libjfx*.so \  
/opt/jdk/jre/lib/ext/jfxrt.jar \  
/opt/jdk/jre/lib/ext/nashorn.jar \  
/opt/jdk/jre/lib/oblique-fonts \  
/opt/jdk/jre/lib/plugin.jar \  
/tmp/* /var/cache/apk/* && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
  
# Set Timezone to CET  
RUN apk add --update tzdata && \  
cp /usr/share/zoneinfo/CET /etc/localtime && \  
rm -rf /usr/share/zoneinfo  
  
ENTRYPOINT ["/init"]  

