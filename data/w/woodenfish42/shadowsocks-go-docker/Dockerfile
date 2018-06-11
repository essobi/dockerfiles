#  
# Dockerfile for shadowsocks-go  
#  
FROM busybox:uclibc AS download-env  
LABEL maintainer="mr.muzea@gmail.com"  
  
ENV SS_VER 1.2.1  
ENV SS_URL https://github.com/shadowsocks/shadowsocks-
go/releases/download/$SS_VER/shadowsocks-server.tar.gz  
  
ADD $SS_URL /  
RUN tar zxf shadowsocks-server.tar.gz  
  
FROM scratch  
COPY \--from=download-env /shadowsocks-server /shadowsocks-server  
  
ENTRYPOINT ["/shadowsocks-server"]  
  

