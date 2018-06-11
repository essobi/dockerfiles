FROM debian:jessie  
  
MAINTAINER lulichn <daisuke.develop@gmail.com>  
  
ENV LANG C.UTF-8  
  
ENV JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=72 \  
JAVA_VERSION_BUILD=15 \  
JAVA_CHECKSUM=46e7f96271043009995f39f04a9e711cdc0cc5b6a5b67910451678a3d250ec98
\  
JAVA_PACKAGE=jdk \  
JAVA_HOME=/opt/jdk \  
\  
VERTX_VERSION=3.2.0 \  
VERTX_CHECKSUM=53818b57bbade9129a419bc53618a3be793230e4d4e2fd43137ca2c35d3d68ee
\  
\  
PATH=${PATH}:/opt/jdk/bin:/usr/local/vert.x/bin  
  
# Setup Oracle JDK  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* \  
/var/lib/apt/lists/* \  
&& cd /opt \  
&& curl -O --location --silent --insecure --show-error --junk-session-cookies
\  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
&& echo "${JAVA_CHECKSUM}
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz"
| sha256sum -c - \  
&& tar -xzf
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \  
&& ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk \  
&& rm -rf /tmp/* \  
/opt/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
/opt/jdk/*src.zip \  
/opt/jdk/lib/*javafx* \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/jre/bin/javaws \  
/opt/jdk/jre/lib/amd64/libdecora_sse.so \  
/opt/jdk/jre/lib/amd64/libprism_*.so \  
/opt/jdk/jre/lib/amd64/libfxplugins.so \  
/opt/jdk/jre/lib/amd64/libglass.so \  
/opt/jdk/jre/lib/amd64/libgstreamer-lite.so \  
/opt/jdk/jre/lib/amd64/libjavafx*.so \  
/opt/jdk/jre/lib/amd64/libjfx*.so \  
/opt/jdk/jre/lib/desktop \  
/opt/jdk/jre/lib/deploy* \  
/opt/jdk/jre/lib/ext/jfxrt.jar \  
/opt/jdk/jre/lib/*javafx* \  
/opt/jdk/jre/lib/javaws.jar \  
/opt/jdk/jre/lib/*jfx* \  
/opt/jdk/jre/lib/plugin.jar \  
/opt/jdk/jre/plugin  
  
# Setup Vert.x  
RUN set -ex \  
&& cd /tmp \  
&& curl -O --location --silent --insecure --show-error --junk-session-cookies
\  
https://bintray.com/artifact/download/vertx/downloads/vert.x-${VERTX_VERSION}.tar.gz
\  
&& echo "${VERTX_CHECKSUM} vert.x-${VERTX_VERSION}.tar.gz" | sha256sum -c - \  
&& mkdir /usr/local/vert.x \  
&& tar -xzf vert.x-${VERTX_VERSION}.tar.gz -C /usr/local/vert.x \  
&& rm -rf /tmp/* \  
/usr/local/vert.x/bin/vertx.bat  
  

