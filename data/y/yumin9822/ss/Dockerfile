FROM alpine  
MAINTAINER yumin9822@gmail.com  
  
RUN echo 'http://nl.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories
\  
&& apk add -U curl libsodium python \  
&& curl -sSL https://bootstrap.pypa.io/get-pip.py | python \  
&& pip install shadowsocks \  
&& apk del curl \  
&& rm -rf /var/cache/apk/*  
  
ADD config.json /config.json  
  
EXPOSE 8388  
ENTRYPOINT ["ssserver", "-c", "/config.json"]  

