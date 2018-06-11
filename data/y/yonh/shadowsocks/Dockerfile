FROM alpine:3.4  
MAINTAINER yonh "azssjli@163.com"  
ENV REFERSHED_AT 2017-02-10  
#replace default sources.list  
ADD sources.list /etc/apk/repositories  
ADD run.sh /run.sh  
ADD config.example /opt/config.example  
  
RUN apk update && \  
apk add --no-cache py-pip && \  
pip install shadowsocks && \  
chmod +x /run.sh  
  
ENV ENV_PASS shadowsocks  
ENV ENV_TIMEOUT 300  
ENV ENV_METHOD rc4-md5  
  
  
CMD ["/run.sh"]  
  

