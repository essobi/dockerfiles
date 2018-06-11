FROM alpine:edge  
MAINTAINER Min Yu <yumin9822@gmail.com>  
  
RUN apk update \  
&& apk add python libsodium unzip wget \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir /ssr \  
&& cd /ssr \  
&& wget --no-check-certificate
https://github.com/breakwa11/shadowsocks/archive/manyuser.zip -O
/tmp/manyuser.zip \  
&& unzip -d /tmp /tmp/manyuser.zip \  
&& mv /tmp/shadowsocks-manyuser/shadowsocks /ssr/shadowsocks \  
&& rm -rf /tmp/*  
  
ADD config.json /config.json  
  
WORKDIR /ssr/shadowsocks  
  
CMD python server.py -c /config.json  

