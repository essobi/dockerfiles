FROM debian:jessie  
  
MAINTAINER Jie Lu <764664@gmail.com>  
  
RUN apt update  
RUN apt install -y wget  
RUN wget -O /tmp/shadowsocks-server-linux64-1.1.5.gz
https://github.com/shadowsocks/shadowsocks-
go/releases/download/1.1.5/shadowsocks-server-linux64-1.1.5.gz  
RUN gunzip -d /tmp/shadowsocks-server-linux64-1.1.5.gz  
RUN mv /tmp/shadowsocks-server-linux64-1.1.5 /usr/bin/shadowsocks-server  
RUN chmod +x /usr/bin/shadowsocks-server  
  
ENV SS_SERVER_PORT 8388  
ENV SS_PASSWORD password  
ENV SS_METHOD aes-256-cfb  
ENV SS_TIMEOUT 300  
CMD /usr/bin/shadowsocks-server -d -p ${SS_SERVER_PORT} -k ${SS_PASSWORD} -m
${SS_METHOD} -t ${SS_TIMEOUT}

