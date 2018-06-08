# shadowsocks  
#  
# VERSION 0.0.1  
FROM alpine:3.4  
MAINTAINER jzdxeb <w@jzdxeb.com>  
RUN apk add --no-cache py-pip bash  
  
RUN pip install shadowsocks==2.8.2  
  
# Configure container to run as an executable  
ENTRYPOINT ["/usr/bin/ssserver"]  

