#Base image  
FROM ubuntu:16.04  
MAINTAINER Baozisoftware Diklic "https://github.com/Baozisoftware"  
ENV SSVERION 1.2.1  
ENV SSPORT 12345  
ENV SSM aes-256-cfb  
ENV SSKEY 12345678  
#Install Shadowsocks  
ADD https://github.com/shadowsocks/shadowsocks-
go/releases/download/$SSVERION/shadowsocks-server.tar.gz /  
RUN tar zxvf shadowsocks-server.tar.gz  
  
#Other  
EXPOSE $SSPORT  
CMD /shadowsocks-server -p $SSPORT -k $SSKEY -m $SSM -u  

