FROM alpine  
  
MAINTAINER fevenor <fevenor@outlook.com>  
  
ENV DEPENDENCIES git build-base autoconf libtool openssl-dev linux-headers  
ENV BASEDIR /tmp/shadowsocks-libev  
ENV PORT 11080  
# Set up building environment  
RUN apk add --update $DEPENDENCIES \  
  
# Get the latest code, build and install  
&& git clone -b $(git ls-remote --tags
https://github.com/shadowsocks/shadowsocks-libev.git | grep -o
'v[0-9]\\+\\.[0-9]\\+\\.[0-9]\\+' | sort -V | tail -1) --depth 1
https://github.com/shadowsocks/shadowsocks-libev.git $BASEDIR \  
&& cd $BASEDIR \  
&& ./configure \  
&& make \  
&& make install \  
  
# Tear down building environment and delete git repository  
&& cd .. \  
&& rm -rf $BASEDIR \  
&& apk del --purge $DEPENDENCIES \  
&& rm -rf /var/cache/apk/*  
  
# Port in the config file won't take affect. Instead we'll use 11080.  
EXPOSE $PORT  
  
# Override the host and port in the config file.  
ENV SERVER_ADDR 0.0.0.0  
ENV PASSWORD=  
ENV METHOD chacha20  
ENV TIMEOUT 300  
ENV DNS 8.8.8.8  
CMD ss-server -s $SERVER_ADDR \  
-p $PORT \  
-k ${PASSWORD:-$(hostname)} \  
-m $METHOD \  
-t $TIMEOUT \  
\--fast-open \  
-d $DNS \  
-u  

