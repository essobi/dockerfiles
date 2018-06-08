FROM gliderlabs/alpine:3.5  
MAINTAINER Bruce Sun <okampfer@gmail.com>  
  
ADD https://github.com/shadowsocks/shadowsocks-
go/releases/download/1.1.5/shadowsocks-local-linux64-1.1.5.gz
/tmp/shadowsocks-client.gz  
  
WORKDIR /tmp/  
  
RUN gunzip shadowsocks-client.gz  
RUN chmod +x ./shadowsocks-client  
  
ENTRYPOINT ["/tmp/shadowsocks-client"]  

