FROM alpine:3.7  
  
ENV LANG=C.UTF-8  
ENV NODE_VERSION 8.9.4  
  
RUN apk --no-cache add nginx=1.14.0-r0 supervisor curl --repository http://dl-
cdn.alpinelinux.org/alpine/edge/main/  
  
ADD nginx /etc/nginx  
  
# Install NodeJS  
RUN addgroup -g 1000 node \  
&& adduser -u 1000 -G node -s /bin/sh -D node \  
&& apk add --no-cache \  
libstdc++ \  
&& apk add --no-cache --virtual .build-deps \  
binutils-gold \  
curl \  
g++ \  
gcc \  
gnupg \  
libgcc \  
linux-headers \  
make \  
python \  
# gpg keys listed at https://github.com/nodejs/node#release-team  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://pgp.mit.edu:80 \--recv-keys "$key" ; \  
done \  
&& curl -SLO
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION.tar.xz\$" SHASUMS256.txt | sha256sum -c - \  
&& tar -xf "node-v$NODE_VERSION.tar.xz" \  
&& cd "node-v$NODE_VERSION" \  
&& ./configure \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& apk del .build-deps \  
&& cd .. \  
&& rm -Rf "node-v$NODE_VERSION" \  
&& rm "node-v$NODE_VERSION.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
# Install glibc  
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
"https://raw.githubusercontent.com/sgerrand/alpine-pkg-
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
"$LANG" || true && \  
echo "export LANG=$LANG" > /etc/profile.d/locale.sh && \  
\  
apk del glibc-i18n && \  
\  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
EXPOSE 80 443

