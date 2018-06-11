# https://github.com/rdsubhas/docker-tor-privoxy-alpine  
FROM hbrls/shadowsocks:latest  
  
  
COPY privoxy.ini /etc/supervisor.d/  
  
RUN \  
apk add --update privoxy supervisor && rm -rf /var/cache/apk/* && \  
sed -i 's/ssserver/sslocal/' /etc/supervisor.d/shadowsocks.ini && \  
sed -i 's/^listen-address/#listen-address/' /etc/privoxy/config && \  
echo -e "listen-address 0.0.0.0:3108\nforward-socks5 / 127.0.0.1:1080 ." >>
/etc/privoxy/config && \  
rm /run.sh  
  
ENTRYPOINT ["/bin/sh", "-c", "/usr/bin/supervisord -c /etc/supervisord.conf"]  
  

