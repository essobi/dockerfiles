FROM ubuntu:16.04  
MAINTAINER Jaeger <JaegerCode@gmail.com>  
ADD shadowsocksR.sh /root/  
USER root  
RUN bash /root/shadowsocksR.sh 2>&1 | tee /root/shadowsocksR.log  
  
EXPOSE 8388  
  
CMD ["/usr/local/shadowsocks/server.py","-c","/etc/shadowsocks.json"]  

