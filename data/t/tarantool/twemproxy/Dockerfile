FROM alpine:3.4  
MAINTAINER mail@racktear.com  
  
RUN addgroup -S twemproxy \  
&& adduser -S -G twemproxy twemproxy \  
&& apk add --no-cache 'su-exec>=0.2'  
  
ENV TWEMPROXY_DOWNLOAD_URL=https://github.com/tarantool/twemproxy.git\  
TWEMPROXY_COMMIT=fe2c817  
  
RUN set -x \  
&& apk add --no-cache --virtual .build-deps \  
perl \  
gcc \  
g++ \  
make \  
git \  
musl-dev \  
autoconf \  
automake \  
libtool \  
&& : "---------- twemproxy ----------" \  
&& mkdir -p /usr/src/twemproxy \  
&& git clone "$TWEMPROXY_DOWNLOAD_URL" /usr/src/twemproxy \  
&& git -C /usr/src/twemproxy checkout "$TWEMPROXY_COMMIT" \  
&& git -C /usr/src/twemproxy submodule update \  
&& (cd /usr/src/twemproxy; \  
autoreconf -fvi; \  
./configure --prefix=/usr; \  
make )\  
&& make -C /usr/src/twemproxy install \  
&& rm -rf /usr/src/twemproxy \  
&& : "---------- remove build deps ----------" \  
&& apk del .build-deps  
  
COPY nutcracker.yml /etc/  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s /usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards
compat  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
  
EXPOSE 3301  
CMD [ "nutcracker", "-c", "/etc/nutcracker.yml"]  

