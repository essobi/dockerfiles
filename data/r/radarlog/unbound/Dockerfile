FROM alpine:3.7  
MAINTAINER Ilian Ranguelov <me@radarlog.net>  
  
ENV BUILD_DEPS make gcc musl-dev ldns-dev libevent-dev expat-dev shadow  
ENV RUNTIME_DEPS bash libevent libressl expat curl  
  
ENV UNBOUND_VERSION 1.7.0  
ENV UNBOUND_SHA1 d90b09315c75ad2843b868785b3d12a2c4f27b28  
ENV UNBOUND_DOWNLOAD_URL
https://www.unbound.net/downloads/unbound-${UNBOUND_VERSION}.tar.gz  
  
ENV LIBSODIUM_VERSION 1.0.16  
ENV LIBSODIUM_SHA1 c7ea321d7b8534e51c5e3d86055f6c1aa1e48ee9  
ENV LIBSODIUM_DOWNLOAD_URL
https://download.libsodium.org/libsodium/releases/libsodium-${LIBSODIUM_VERSION}.tar.gz  
  
RUN set -e \  
&& cd /tmp \  
#  
# Install dependencies  
&& apk --no-cache add \--update $RUNTIME_DEPS $BUILD_DEPS \  
#  
# Download and extract libsodium  
&& curl -o libsodium.tar.gz $LIBSODIUM_DOWNLOAD_URL \  
&& echo "${LIBSODIUM_SHA1} *libsodium.tar.gz" | sha1sum -c - \  
&& tar xzf libsodium.tar.gz \  
&& cd libsodium-${LIBSODIUM_VERSION} \  
#  
# Build libsodium  
&& env CFLAGS=-Ofast ./configure --disable-dependency-tracking \  
&& make check \  
&& make install \  
&& ldconfig /usr/local/lib \  
#  
# Download and extract unbound  
&& curl -o unbound.tar.gz -fSL ${UNBOUND_DOWNLOAD_URL} \  
&& echo "${UNBOUND_SHA1} *unbound.tar.gz" | sha1sum -c - \  
&& tar zxvf unbound.tar.gz \  
&& cd unbound-${UNBOUND_VERSION} \  
#  
# Build unbound  
&& ./configure \  
\--with-libevent \  
\--enable-event-api \  
\--enable-dnscrypt \  
&& make install \  
#  
# Create custom user  
&& groupadd unbound \  
&& useradd -g unbound -d /dev/null unbound \  
#  
# Clean up  
&& apk del --purge $BUILD_DEPS \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
COPY entrypoint.sh /bin/entrypoint.sh  
COPY unbound.conf /usr/local/etc/unbound/  
  
EXPOSE 53/udp 53/tcp  
EXPOSE 443/udp 443/tcp  
  
VOLUME /usr/local/etc/unbound/keys  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["unbound", "-d"]  

