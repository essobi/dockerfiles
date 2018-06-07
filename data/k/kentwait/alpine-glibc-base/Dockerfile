# kentwait/alpine-glibc-base  
FROM kentwait/alpine-base  
MAINTAINER Kent Kawashima <kentkawashima@gmail.com>  
  
ENV GLIBC_BASE_URL "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download"  
ENV GLIBC_VERSION 2.23-r3  
ENV GLIBC_BASE_PACKAGE glibc-${GLIBC_VERSION}.apk  
ENV GLIBC_BIN_PACKAGE glibc-bin-${GLIBC_VERSION}.apk  
ENV GLIBC_I18N_PACKAGE glibc-i18n-${GLIBC_VERSION}.apk  
  
ENV GLIBC_RSA_KEY /etc/apk/keys/sgerrand.rsa.pub  
  
WORKDIR /tmp  
RUN apk update && apk upgrade \  
&& apk add --no-cache --virtual temp-pkgs \  
build-base \  
wget \  
ca-certificates \  
&& wget -q \  
"https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
-O ${GLIBC_RSA_KEY} \  
&& wget -q \  
"$GLIBC_BASE_URL/$GLIBC_VERSION/$GLIBC_BASE_PACKAGE" \  
"$GLIBC_BASE_URL/$GLIBC_VERSION/$GLIBC_BIN_PACKAGE" \  
"$GLIBC_BASE_URL/$GLIBC_VERSION/$GLIBC_I18N_PACKAGE" \  
&& apk add --no-cache \  
"$GLIBC_BASE_PACKAGE" \  
"$GLIBC_BIN_PACKAGE" \  
"$GLIBC_I18N_PACKAGE" \  
# remove key  
&& rm ${GLIBC_RSA_KEY} \  
&& /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true \  
&& echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh \  
# remove packages and clean up  
&& apk del glibc-i18n \  
&& apk del temp-pkgs \  
&& rm -rf /tmp/* \  
/root/.wget-hsts  
  
WORKDIR /  

