FROM busybox  
MAINTAINER cloverzrg@gmail.com  
  
#ADD https://github.com/shadowsocks/shadowsocks-
go/releases/download/1.2.1/shadowsocks-server.tar.gz /sserver  
#RUN mv /sserver/shadowsocks-server /shadowsocks-server  
ADD shadowsocks-server /shadowsocks-server  
RUN chmod +x /shadowsocks-server  
COPY run.sh /run.sh  
ENV PASSWORD docker  
ENV METHOD aes-128-cfb  
# aes-128-cfb, aes-192-cfb, aes-256-cfb, bf-cfb, cast5-cfb,  
# des-cfb, rc4-md5, chacha20, salsa20, rc4, table  
EXPOSE 8373  
CMD ["sh","run.sh"]  

