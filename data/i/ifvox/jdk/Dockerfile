FROM alpine:3.5  
  
# combine work from delitescere/jdk, frol/docker-alpine-glibc and shinyproxy  
  
ENV LANG=C.UTF-8  
  
ENV JAVA_HOME /usr/local/java  
ENV JRE ${JAVA_HOME}/jre  
ENV JAVA_OPTS=-Djava.awt.headless=true
PATH=${PATH}:${JRE}/bin:${JAVA_HOME}/bin  
ENV ENV=/etc/shinit.sh  
  
COPY shinit.sh /etc/  
  
WORKDIR /tmp  
  
RUN \  
################################################################################  
# 1. SETUP GLIBC  
#  
################################################################################  
# blatantly stolen from: https://github.com/frol/docker-alpine-glibc  
# Here we install GNU libc (aka glibc) and set C.UTF-8 locale as default.  
################################################################################  
ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.25-r0" && \  
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
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
  
################################################################################  
# 2. SETUP Zuul OpenJDK  
#  
# blatantly stolen from: https://github.com/delitescere/docker-zulu  
################################################################################  
echo ipv6 >> /etc/modules && \  
echo 'http://dl-2.alpinelinux.org/alpine/v3.3/main/' > /etc/apk/repositories
&& \  
sed -i -e 's#:/bin/[^:].*$#:/sbin/nologin#' /etc/passwd && \  
chmod a=rx /etc/shinit.sh && \  
checksum="3f95d82bf8ece272497ae2d3c5b56c3b" && \  
url="https://cdn.azul.com/zulu/bin/zulu8.19.0.1-jdk8.0.112-linux_x64.tar.gz"
&& \  
referer="http://zulu.org/download/" && \  
wget --referer "${referer}" "${url}" && \  
md5=$(md5sum *.tar.gz | cut -f1 -d' ') && \  
if [ ${checksum} != ${md5} ]; then \  
echo "[FATAL] File md5 ${md5} doesn't match published checksum ${checksum}.
Exiting." >&2 && \  
exit 1; \  
fi && \  
tar -xzf *.tar.gz && \  
rm *.tar.gz && \  
mkdir -p $(dirname ${JAVA_HOME}) && \  
mv * ${JAVA_HOME} && \  
cd ${JAVA_HOME} && \  
rm -rf *.zip demo man sample && \  
for ff in ${JAVA_HOME}/bin/*; do f=$(basename $ff); if [ -e ${JRE}/bin/$f ];
then ln -snf ${JRE}/bin/$f $ff; fi; done && \  
chmod a+w ${JRE}/lib ${JRE}/lib/net.properties && \  
apk del .build-dependencies && \  
apk del openssl && \  
rm -rf /tmp/* /var/cache/apk/* && \  
java -version  
  
WORKDIR /root  
  
# java -jar /root/shinyproxy.jar  

