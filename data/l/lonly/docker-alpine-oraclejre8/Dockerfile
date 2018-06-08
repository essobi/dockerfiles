FROM lonly/docker-alpine-glibc  
  
ARG VERSION=8u152  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL \  
maintainer="lonly197@qq.com" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="Apache License 2.0" \  
org.label-schema.name="lonly/docker-alpine" \  
org.label-schema.url="https://github.com/lonly197" \  
org.label-schema.description="Minified Docker image with OracleJRE 8 to run
Java applications." \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/lonly197/docker-alpine-
oraclejre8" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vendor="lonly197@qq.com" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
# Define environment  
ENV JAVA_HOME=/usr/lib/jvm/default-jvm/jre \  
PATH=$PATH:${JAVA_HOME}:${JAVA_HOME}/bin  
  
# Install packages  
RUN set -x \  
## Install jdk  
&& JAVA_UPDATE=152 \  
&& JAVA_BUILD=16 \  
&& JAVA_PATH=aa0333dd3019491ca4f6ddbe78cdb6d0 \  
&& cd /tmp/ \  
&& wget --no-check-certificate -c -q --header "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/${VERSION}-b${JAVA_BUILD}/${JAVA_PATH}/jre-${VERSION}-linux-x64.tar.gz
\  
&& tar -zxvf jre-${VERSION}-linux-x64.tar.gz \  
&& mkdir -p ${JAVA_HOME} \  
&& mv /tmp/jre1.8.0_${JAVA_UPDATE} ${JAVA_HOME} \  
## Cleanup  
&& rm -rf "$JAVA_HOME/lib/plugin.jar" \  
"$JAVA_HOME/lib/ext/jfxrt.jar" \  
"$JAVA_HOME/bin/javaws" \  
"$JAVA_HOME/lib/javaws.jar" \  
"$JAVA_HOME/lib/desktop" \  
"$JAVA_HOME/plugin" \  
"$JAVA_HOME/lib/"deploy* \  
"$JAVA_HOME/lib/"*javafx* \  
"$JAVA_HOME/lib/"*jfx* \  
"$JAVA_HOME/lib/amd64/libdecora_sse.so" \  
"$JAVA_HOME/lib/amd64/"libprism_*.so \  
"$JAVA_HOME/lib/amd64/libfxplugins.so" \  
"$JAVA_HOME/lib/amd64/libglass.so" \  
"$JAVA_HOME/lib/amd64/libgstreamer-lite.so" \  
"$JAVA_HOME/lib/amd64/"libjavafx*.so \  
"$JAVA_HOME/lib/amd64/"libjfx*.so \  
"$JAVA_HOME/bin/jjs" \  
"$JAVA_HOME/bin/keytool" \  
"$JAVA_HOME/bin/orbd" \  
"$JAVA_HOME/bin/pack200" \  
"$JAVA_HOME/bin/policytool" \  
"$JAVA_HOME/bin/rmid" \  
"$JAVA_HOME/bin/rmiregistry" \  
"$JAVA_HOME/bin/servertool" \  
"$JAVA_HOME/bin/tnameserv" \  
"$JAVA_HOME/bin/unpack200" \  
"$JAVA_HOME/lib/ext/nashorn.jar" \  
"$JAVA_HOME/lib/jfr.jar" \  
"$JAVA_HOME/lib/jfr" \  
"$JAVA_HOME/lib/oblique-fonts" \  
&& rm -rf *.tgz \  
*.tar \  
*.zip \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*

