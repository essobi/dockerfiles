FROM alpine:latest  
MAINTAINER Apricity  
  
RUN apk --no-cache add python libsodium wget unzip  
  
ENV ssr_url=https://github.com/shadowsocksr/shadowsocksr/archive/manyuser.zip  
  
RUN wget --no-check-certificate $ssr_url -O /tmp/manyuser.zip \  
&& unzip -d /tmp /tmp/manyuser.zip \  
&& mv /tmp/shadowsocksr-manyuser/shadowsocks /shadowsocks \  
&& rm -rf /tmp/*  
  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 8388  
ENV PASSWORD=p@ssw0rd \  
METHOD=aes-256-cfb \  
PROTOCOL=auth_aes128_md5 \  
OBFS=tls1.2_ticket_auth \  
TIMEOUT=300  
EXPOSE $SERVER_PORT  
  
WORKDIR /shadowsocks  
  
CMD python /shadowsocks/server.py \  
-s $SERVER_ADDR \  
-p $SERVER_PORT \  
-k $PASSWORD \  
-m $METHOD \  
-O $PROTOCOL \  
-o $OBFS \  
-t $TIMEOUT  

