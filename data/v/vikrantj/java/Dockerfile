FROM alpine:3.4  
  
MAINTAINER Vikrant Jain <vikrantj.develop@gmail.com>  
  
ARG JDK_MAJOR=8  
ARG JDK_MINOR=101  
ARG JDK_BUILD=13  
ARG JDK_URL=http://download.oracle.com/otn-
pub/java/jdk/${JDK_MAJOR}u${JDK_MINOR}-b${JDK_BUILD}/jdk-${JDK_MAJOR}u${JDK_MINOR}-linux-x64.tar.gz  
  
ENV JAVA_HOME=/opt/jdk \  
PATH=/opt/jdk/bin:${PATH} \  
LANG=C.UTF-8  
  
RUN apk upgrade --update \  
&& apk add --update curl ca-certificates bash \  
&& curl -L -o /tmp/glibc-2.23-r3.apk "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk" \  
&& apk add --allow-untrusted /tmp/glibc-2.23-r3.apk \  
&& /sbin/ldconfig /lib /usr/glibc/usr/lib \  
&& curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" ${JDK_URL}
-o /tmp/jdk.tar.gz \  
&& mkdir -p /opt \  
&& tar zxf /tmp/jdk.tar.gz -C /opt \  
&& ln -s /opt/jdk1.${JDK_MAJOR}.0_${JDK_MINOR} /opt/jdk \  
&& rm -rf /tmp/* /var/cache/apk/* \  
&& echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf \  
&& find /opt/jdk/ -maxdepth 1 -mindepth 1 | grep -v jre | xargs rm -rf \  
&& cd /opt/jdk/ && ln -s ./jre/bin ./bin \  
&& rm -rf /opt/jdk/jre/plugin \  
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
/opt/jdk/jre/lib/plugin.jar  

