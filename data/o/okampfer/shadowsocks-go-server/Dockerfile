FROM gliderlabs/alpine:3.5  
MAINTAINER Bruce Sun <okampfer@gmail.com>  
  
ADD https://github.com/shadowsocks/shadowsocks-
go/releases/download/1.2.1/shadowsocks-server.tar.gz /tmp/shadowsocks-
server.tar.gz  
  
WORKDIR /tmp/  
  
RUN tar xf shadowsocks-server.tar.gz  
RUN rm shadowsocks-server.tar.gz  
RUN chmod +x ./shadowsocks-server  
  
ENTRYPOINT ["/tmp/shadowsocks-server"]  

