#  
# Dockerfile for aria2  
#  
  
FROM alpine:latest  
  
RUN buildDeps=" \  
curl \  
g++ \  
make \  
tar \  
xz \  
gnutls-dev \  
nettle-dev \  
gmp-dev \  
libssh2-dev \  
c-ares-dev \  
libxml2-dev \  
zlib-dev \  
sqlite-dev \  
pkgconf \  
linux-headers \  
"; \  
set -xe \  
&& apk add --update ca-certificates musl c-ares libgcc gmp gnutls nettle
sqlite-libs libstdc++ zlib libxml2 libssh2 \  
&& apk add $buildDeps \  
&& cd ~ \  
&& ARIA2_VERSION=`curl -s "https://github.com/aria2/aria2/releases/latest" |
sed -n 's/^.*tag\/release-\(.*\)".*/\1/p'` \  
&& curl -SL
"https://github.com/aria2/aria2/releases/download/release-$ARIA2_VERSION/aria2-$ARIA2_VERSION.tar.gz"
-o aria2.tar.gz \  
&& mkdir -p /usr/src/aria2 \  
&& tar -xf aria2.tar.gz -C /usr/src/aria2 --strip-components=1 \  
&& rm aria2.tar.gz \  
&& cd /usr/src/aria2 \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /usr/src/aria2 \  
&& apk del $buildDeps \  
&& rm -rf /var/cache/apk/* \  
&& aria2c https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 -d
/usr/local/bin -o gosu \  
&& chmod +x /usr/local/bin/gosu  
  
VOLUME /home/aria2 /etc/aria2  
  
EXPOSE 6800  
CMD set -xe \  
&& gosu nobody aria2c --conf-path=/etc/aria2/aria2.conf  

