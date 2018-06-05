FROM alpine:latest  
  
RUN apk add haproxy --no-cache \  
&& apk add 3proxy --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \  
&& apk add tor --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/community/ --allow-untrusted  
  
ADD 3proxy.cfg haproxy.cfg /etc/  
ADD tor-pool /usr/bin/tor-pool  
  
ENTRYPOINT /usr/bin/tor-pool  
ENV TOR_NUM=5 TOR_RELOAD_MINUTES=5  
EXPOSE 8118 9050  

