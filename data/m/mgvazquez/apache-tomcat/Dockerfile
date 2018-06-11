FROM mgvazquez/oracle-jdk:8-1.0  
ARG BUILD_DATE  
ARG BUILD_VCS_REF  
ARG BUILD_VERSION  
  
ENV DUMB_INIT_VERSION 1.2.1  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.0.48  
ENV TOMCAT_SHA1 d2446c127c9b11f88def11e542af98998071d91d  
  
##################################################  
EXPOSE 8080  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# let "Tomcat Native" live somewhere isolated  
ENV TOMCAT_NATIVE_LIBDIR $CATALINA_HOME/native-jni-lib  
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}$TOMCAT_NATIVE_LIBDIR  
  
## ------ https://github.com/Yelp/dumb-init ------  
ADD https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 /bin/dumb-init  
## -----------------------------------------------  
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
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV TOMCAT_TGZ_URLS \  
#
https://issues.apache.org/jira/browse/INFRA-8753?focusedCommentId=14735394#comment-14735394  
https://www.apache.org/dyn/closer.cgi?action=download&filename=tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz \  
# if the version is outdated, we might have to pull from the dist/archive :/  
https://www-
us.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz \  
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz \  
https://archive.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
ENV TOMCAT_ASC_URLS \  
https://www.apache.org/dyn/closer.cgi?action=download&filename=tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz.asc \  
# not all the mirrors actually carry the .asc files :'(  
https://www-
us.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz.asc \  
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz.asc \  
https://archive.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz.asc  
  
RUN set -eux; \  
\  
apk add --no-cache --virtual .fetch-deps \  
ca-certificates \  
openssl \  
; \  
\  
success=; \  
for url in $TOMCAT_TGZ_URLS; do \  
if wget -O tomcat.tar.gz "$url"; then \  
success=1; \  
break; \  
fi; \  
done; \  
[ -n "$success" ]; \  
\  
echo "$TOMCAT_SHA1 *tomcat.tar.gz" | sha1sum -c -; \  
\  
success=; \  
for url in $TOMCAT_ASC_URLS; do \  
if wget -O tomcat.tar.gz.asc "$url"; then \  
success=1; \  
break; \  
fi; \  
done; \  
[ -n "$success" ]; \  
\  
gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz; \  
tar -xvf tomcat.tar.gz --strip-components=1; \  
rm bin/*.bat; \  
rm tomcat.tar.gz*; \  
\  
nativeBuildDir="$(mktemp -d)"; \  
tar -xvf bin/tomcat-native.tar.gz -C "$nativeBuildDir" \--strip-components=1;
\  
apk add --no-cache --virtual .native-build-deps \  
apr-dev \  
coreutils \  
dpkg-dev dpkg \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
sudo \  
; \  
( \  
export CATALINA_HOME="$PWD"; \  
cd "$nativeBuildDir/native"; \  
gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)"; \  
./configure \  
\--build="$gnuArch" \  
\--libdir="$TOMCAT_NATIVE_LIBDIR" \  
\--prefix="$CATALINA_HOME" \  
\--with-apr="$(which apr-1-config)" \  
\--with-java-home="$JAVA_HOME" \  
\--with-ssl=yes; \  
make -j "$(nproc)"; \  
make install; \  
); \  
runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive
"$TOMCAT_NATIVE_LIBDIR" \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)"; \  
apk add --virtual .tomcat-native-rundeps $runDeps; \  
apk del .fetch-deps .native-build-deps; \  
rm -rf "$nativeBuildDir"; \  
rm bin/tomcat-native.tar.gz; \  
\  
# sh removes env vars it doesn't support (ones with periods)  
# https://github.com/docker-library/tomcat/issues/77  
apk add \--no-cache bash sudo; \  
chmod a+x /bin/dumb-init; \  
find ./bin/ -name '*.sh' -exec sed -ri 's|^#!/bin/sh$|#!/usr/bin/env bash|'
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
  
#
------------------------------------------------------------------------------------------------------------------------------------------------------  
ENTRYPOINT ["/bin/dumb-init"]  
CMD ["catalina.sh", "run"]  
  
################### Don't move ###################  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/mgvazquez/docker-apache-
tomcat.git" \  
org.label-schema.vcs-ref=$BUILD_VCS_REF \  
org.label-schema.version=$BUILD_VERSION \  
org.label-schema.maintainer="Manuel Andres Garcia Vazquez <mvazquez@scabb-
island.com.ar>" \  
org.label-schema.apache.tomcat.version=$TOMCAT_VERSION \  
com.microscaling.license=GPL-3.0  
##################################################  

