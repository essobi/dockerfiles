#alpine linux with glibc  
FROM youske/alpine-stdmachine:base  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.stdmachine.description="alpine glibc image" \  
com.stdmachine.vendor="stdmachine" \  
com.stdmachine.role="baseimage"  
  
ENV LANG=C.UTF-8  
WORKDIR /tmp  
RUN GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
GLIBC_VERSION="2.23-r3" && \  
GLIBC_BASE_PACKAGE="glibc-$GLIBC_VERSION.apk" && \  
GLIBC_BIN_PACKAGE="glibc-bin-$GLIBC_VERSION.apk" && \  
GLIBC_I18N_PACKAGE="glibc-i18n-$GLIBC_VERSION.apk" && \  
wget -q \  
"https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
-O "/etc/apk/keys/sgerrand.rsa.pub" && \  
wget -q \  
"$GLIBC_BASE_URL/$GLIBC_VERSION/$GLIBC_BASE_PACKAGE" \  
"$GLIBC_BASE_URL/$GLIBC_VERSION/$GLIBC_BIN_PACKAGE" \  
"$GLIBC_BASE_URL/$GLIBC_VERSION/$GLIBC_I18N_PACKAGE" && \  
apk add --no-cache "$GLIBC_BASE_PACKAGE" "$GLIBC_BIN_PACKAGE"
"$GLIBC_I18N_PACKAGE" && \  
# remove key  
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
#  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
# package remove  
apk del --no-cache glibc-i18n && rm -rf /tmp/* /root/.wget-hsts  
  
WORKDIR /workdir  

