FROM alpine:3.6  
  
ARG VERSION=2.26-r0  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL \  
maintainer="lonly197@qq.com" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="Apache License 2.0" \  
org.label-schema.name="lonly/docker-alpine-glibc" \  
org.label-schema.url="https://github.com/lonly197" \  
org.label-schema.description="Alpine GNU C library (glibc) Docker image." \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/lonly197/docker-alpine-glibc" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vendor="lonly197@qq.com" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
# Define environment  
## At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG=C.UTF-8  
# Install base packages  
RUN set -x \  
## Add alpine repo  
&& echo http://mirrors.aliyun.com/alpine/v3.6/main/ >> /etc/apk/repositories \  
&& echo http://mirrors.aliyun.com/alpine/v3.6/community/ >>
/etc/apk/repositories \  
## Update apk package  
&& apk update \  
## Add base package  
&& apk add --no-cache --upgrade --virtual=build-dependencies bash curl ca-
certificates openssl wget jq tar \  
## Update ca-cert  
&& update-ca-certificates \  
## Define uname  
&& echo -ne "Alpine Linux ${VERSION} image. (`uname -rsv`)\n" >> /root/.built
\  
## Download glibc  
&& wget "https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" -O "/etc/apk/keys/sgerrand.rsa.pub" \  
&& ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" \  
&& ALPINE_GLIBC_PACKAGE_VERSION="${VERSION}" \  
&&
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk" \  
&& ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" \  
&&
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
\  
&& wget \  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
\  
## Install glibc  
&& apk add --no-cache \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" \  
## Cleanup  
&& apk del .build-dependencies \  
&& rm "/etc/apk/keys/sgerrand.rsa.pub" \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true \  
&& echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh \  
&& apk del glibc-i18n \  
&& rm "/root/.wget-hsts" \  
&& rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" \  
&& rm -rf *.tgz \  
*.tar \  
*.zip \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*

