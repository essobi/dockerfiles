FROM alpine:latest  
  
RUN set -ex \  
&& apk add --no-cache libsodium py2-pip \  
&& pip --no-cache-dir install
https://github.com/shadowsocks/shadowsocks/archive/master.zip  
  
ADD config.json /config.json  
  
EXPOSE 443  
EXPOSE 1080  
ENTRYPOINT ["/usr/bin/sslocal", "-c", "/config.json"]

