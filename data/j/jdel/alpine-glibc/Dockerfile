FROM jdel/alpine:edge  
  
USER root  
  
RUN apk update \  
&& apk upgrade \  
&& ALPINE_GLIBC_PACKAGE_VERSION="2.26-r0" \  
&& ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" \  
&&
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk" \  
&& ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" \  
&&
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
\  
&& apk add --no-cache --virtual=.build-deps wget \  
&& wget --retry-connrefused --waitretry=5 --read-timeout=10 --timeout=5 -t 5 \  
"https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" -O "/etc/apk/keys/sgerrand.rsa.pub" \  
&& wget --retry-connrefused --waitretry=5 --read-timeout=10 --timeout=5 -t 5 \  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
\  
&& apk add --no-cache "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" \  
&& rm "/etc/apk/keys/sgerrand.rsa.pub" \  
&& /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true \  
&& echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh \  
&& apk del glibc-i18n \  
&& apk del .build-deps \  
&& rm "/root/.wget-hsts" \  
&& rm "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" \  
&& rm -rf /var/cache/apk/*  
  
ENV LANG=C.UTF-8  
USER user

