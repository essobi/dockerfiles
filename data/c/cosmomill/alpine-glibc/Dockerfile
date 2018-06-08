FROM alpine:3.7  
# Here we install GNU libc (aka glibc) and set C.UTF-8 locale as default.  
  
RUN ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.27-r0" && \  
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \  
wget \  
"https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
-O "/etc/apk/keys/sgerrand.rsa.pub" && \  
wget \  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
&& \  
apk add --no-cache \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
\  
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
\  
apk del glibc-i18n && \  
\  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
ENV LANG=C.UTF-8  
# create symlink for glibc locale  
RUN ln -s /usr/glibc-compat/bin/locale /bin/locale  
  
# glibc ldd is broken, to check libraries on a glibc binary you need to run
gldd  
RUN echo $'#!/bin/sh\n\  
\n\  
LD_TRACE_LOADED_OBJECTS=1 /usr/glibc-compat/lib/ld-linux-x86-64.so.2 $1\n' >
/usr/bin/gldd \  
\  
&& chmod 755 /usr/bin/gldd  

