FROM alpine:latest  
  
LABEL maintainer "https://github.com/hermsi1337"  
  
ENV GLIBC_VERSION="2.27-r0" \  
LANG=C.UTF-8  
  
RUN GLIBC_DOWNLOAD="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}" \  
&& GLIBC_PACKAGE="glibc-${GLIBC_VERSION}.apk" \  
&& GLIBC_BIN="glibc-bin-${GLIBC_VERSION}.apk" \  
&& GLIBC_I18N="glibc-i18n-${GLIBC_VERSION}.apk" \  
&& PUBKEY_DOWNLOAD="https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
&& WORKDIR="/tmp" \  
&& apk add \--update --no-cache \--virtual=.build-dependencies wget ca-
certificates \  
&& wget -q "${PUBKEY_DOWNLOAD}" -O "/etc/apk/keys/sgerrand.rsa.pub" \  
&& for DL in "${GLIBC_PACKAGE}" "${GLIBC_BIN}" "${GLIBC_I18N}" ; do \  
PACKAGE="${WORKDIR}/${DL}" ; \  
wget -q "${GLIBC_DOWNLOAD}/${DL}" -O "${PACKAGE}" ; \  
apk add \--no-cache "${PACKAGE}" ; \  
done \  
&& /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true \  
&& echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh \  
&& rm -rf "/etc/apk/keys/sgerrand.rsa.pub" "${WORKDIR}/*" "/root/wget.hsts" \  
&& apk del .build-dependencies glibc-i18n  

