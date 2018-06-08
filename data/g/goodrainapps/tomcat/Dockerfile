FROM goodrainapps/openjdk:8u131-jre-alpine  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# let "Tomcat Native" live somewhere isolated  
ENV TOMCAT_NATIVE_LIBDIR $CATALINA_HOME/native-jni-lib  
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}$TOMCAT_NATIVE_LIBDIR  
  
RUN apk add --no-cache gnupg  
  
# see https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/KEYS  
# see also "update.sh" (https://github.com/docker-
library/tomcat/blob/master/update.sh)  
ENV GPG_KEYS 05AB33110949707C93A279E3D3EFE6B686867BA6
07E48665A34DCAFAE522E5E6266191C37C037D42
47309207D818FFD8DCD3F83F1931D684307A10A5
541FBE7D8F78B25E055DDEE13C370389288584E7
61B832AC2F1C5A90F0F9B00A1C506407564C17A3
713DA88BE50911535FE716F5208B0AB1D63011C7
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED
9BA44C2621385CB966EBA586F72C284D731FABEE
A27677289986DB50844682F8ACB77FC2E86E29AC
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
RUN set -ex; \  
for key in $GPG_KEYS; do \  
{ \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "$key"; \  
} \  
done  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.5.20  
ENV TOMCAT_TGZ_URL http://pkg.goodrain.com/apps/tomcat/8.5/apache-
tomcat-8.5.20.tar.gz  
ENV TOMCAT_ASC_URL http://pkg.goodrain.com/apps/tomcat/8.5/apache-
tomcat-8.5.20.tar.gz.asc  
  
RUN set -x \  
\  
&& apk add --no-cache --virtual .fetch-deps \  
ca-certificates \  
tar \  
openssl \  
&& wget -O tomcat.tar.gz "$TOMCAT_TGZ_URL" \  
&& wget -O tomcat.tar.gz.asc "$TOMCAT_ASC_URL" \  
&& gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz* \  
\  
&& nativeBuildDir="$(mktemp -d)" \  
&& tar -xvf bin/tomcat-native.tar.gz -C "$nativeBuildDir" \--strip-
components=1 \  
&& apk add --no-cache --virtual .native-build-deps \  
apr-dev \  
coreutils \  
dpkg-dev dpkg \  
gcc \  
libc-dev \  
make \  
"openjdk${JAVA_VERSION%%[-~bu]*}"="$JAVA_ALPINE_VERSION" \  
openssl-dev \  
&& ( \  
export CATALINA_HOME="$PWD" \  
&& cd "$nativeBuildDir/native" \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--libdir="$TOMCAT_NATIVE_LIBDIR" \  
\--prefix="$CATALINA_HOME" \  
\--with-apr="$(which apr-1-config)" \  
\--with-java-home="$(docker-java-home)" \  
\--with-ssl=yes \  
&& make -j "$(nproc)" \  
&& make install \  
) \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive "$TOMCAT_NATIVE_LIBDIR" \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .tomcat-native-rundeps $runDeps \  
&& apk del .fetch-deps .native-build-deps \  
&& rm -rf "$nativeBuildDir" \  
&& rm bin/tomcat-native.tar.gz \  
# sh removes env vars it doesn't support (ones with periods)  
# https://github.com/docker-library/tomcat/issues/77  
&& apk add \--no-cache bash \  
&& find ./bin/ -name '*.sh' -exec sed -ri 's|^#!/bin/sh$|#!/usr/bin/env bash|'
'{}' +  
  
# verify Tomcat Native is working properly  
RUN set -e \  
&& nativeLines="$(catalina.sh configtest 2>&1)" \  
&& nativeLines="$(echo "$nativeLines" | grep 'Apache Tomcat Native')" \  
&& nativeLines="$(echo "$nativeLines" | sort -u)" \  
&& if ! echo "$nativeLines" | grep 'INFO: Loaded APR based Apache Tomcat
Native library' >&2; then \  
echo >&2 "$nativeLines"; \  
exit 1; \  
fi  
  
# set JAVA_OPTS  
RUN sed -i "2 a. /opt/goodrain/java/setmem.sh"
/usr/local/tomcat/bin/catalina.sh  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
# add redis session lib  
ENV REDIS_SESSION_VER=2.2.2  
ENV REDIS_SESSION_URL=https://pkg.goodrain.com/apps/java/session  
RUN wget -O $CATALINA_HOME/lib/redis-session-manager.jar
$REDIS_SESSION_URL/redis-session-manager-${REDIS_SESSION_VER}-SNAPSHOT.jar  
  
# add pinpoint apm agent  
COPY pinpoint/pinpoint-agent.sh /usr/local/tomcat/bin  
  
EXPOSE 8080  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["catalina.sh", "run"]  

