FROM nimmis/alpine-glibc  
  
MAINTAINER nimmis <kjell.havneskold@gmail.com>  
  
ENV JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=131 \  
JAVA_VERSION_BUILD=11 \  
JAVA_URL_HASH=d54c1d3a095b4ff2b6607d096fa80163 \  
JAVA_HOME=/usr/lib/jvm/default-jvm \  
PATH=${PATH}:/usr/lib/jvm/default-jvm/bin/  
  
RUN apk update && apk upgrade && \  
apk add curl && \  
mkdir -p /usr/lib/jvm/ && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_URL_HASH}/jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz"
| \  
tar xz -C /usr/lib/jvm/ && \  
ln -s jre1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /usr/lib/jvm/default-
jvm && \  
apk del curl && \  
mkdir /tmp/tmprt && \  
cd /tmp/tmprt && \  
unzip -q /usr/lib/jvm/default-jvm/lib/rt.jar && \  
apk add zip && \  
zip -q -r /tmp/rt.zip . && \  
apk del zip && \  
cd /tmp && \  
mv rt.zip /usr/lib/jvm/default-jvm/lib/rt.jar && \  
# thanks to Anastas Dancha <anapsix@random.io> for ideas about files to remove  
cd /usr/lib/jvm/default-jvm/ && \  
rm -rf *src.zip lib/missioncontrol lib/visualvm lib/*javafx* bin/javaws && \  
rm -rf plugin bin/javaws bin/jjs bin/keytool bin/orbd bin/pack200
bin/policytool \  
bin/rmid bin/rmiregistry bin/servertool bin/tnameserv bin/unpack200 \  
lib/javaws.jar lib/deploy* lib/desktop lib/*javafx* lib/*jfx* \  
lib/jfr* lib/amd64/libdecora_sse.so lib/amd64/libprism_*.so \  
lib/amd64/libfxplugins.so lib/amd64/libglass.so \  
lib/amd64/libgstreamer-lite.so lib/amd64/libjavafx*.so \  
lib/amd64/libjfx*.so lib/ext/jfxrt.jar lib/ext/nashorn.jar \  
lib/oblique-fonts lib/plugin.jar /tmp/tmprt /var/cache/apk/*  

