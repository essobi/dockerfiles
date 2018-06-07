FROM alpine:edge  
  
ENV KCP_VER 20170329  
RUN apk update \  
&& apk add python libsodium unzip wget \  
&& rm -rf /var/cache/apk/* \  
&& apk add --no-cache --virtual .build-deps curl \  
&& mkdir -p /opt/kcptun \  
&& cd /opt/kcptun \  
&& curl -fSL
https://github.com/xtaci/kcptun/releases/download/v$KCP_VER/kcptun-linux-
amd64-$KCP_VER.tar.gz | tar xz \  
&& rm client_linux_amd64 \  
&& cd ~ \  
&& apk del .build-deps \  
&& apk add --no-cache supervisor \  
&& mkdir /ssr \  
&& cd /ssr \  
&& wget --no-check-certificate
https://github.com/breakwa11/shadowsocks/archive/manyuser.zip -O
/tmp/manyuser.zip \  
&& unzip -d /tmp /tmp/manyuser.zip \  
&& mv /tmp/shadowsocksr-manyuser/shadowsocks /ssr/shadowsocks \  
&& rm -rf /tmp/*  
  
COPY config.json /config.json  
COPY dns.conf /ssr/shadowsocks/dns.conf  
  
WORKDIR /ssr/shadowsocks  
  
COPY supervisord.conf /etc/supervisord.conf  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 8989/tcp 8999/tcp 29900/udp  
ENTRYPOINT ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]  
  

