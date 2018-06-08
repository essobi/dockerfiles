FROM alpine  
  
MAINTAINER littleqz <littleqz@gmail.com>  
  
RUN echo 'http://nl.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories
\  
&& apk add -U curl libsodium python \  
&& curl -sSL https://bootstrap.pypa.io/get-pip.py | python \  
&& pip install shadowsocks \  
&& apk del curl \  
&& rm -rf /var/cache/apk/*  
  
ENV SERVER 0.0.0.0  
ENV SERVER_PORT 998  
ENV PASSWORD default  
ENV METHOD aes-256-cfb  
ENV TIMEOUT 300  
ENV WORKERS 10  
EXPOSE $SERVER_PORT  
  
cmd ssserver -s "$SERVER" \  
-p "$SERVER_PORT" \  
-k "$PASSWORD" \  
-m "$METHOD" \  
-t "$TIMEOUT" \  
\--workers "$WORKERS" -v  

