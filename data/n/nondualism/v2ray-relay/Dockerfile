FROM alpine:latest  
  
MAINTAINER admin@v2ray.com  
  
COPY v2ray /usr/bin/v2ray/  
COPY config.json /etc/v2ray/config.json  
  
RUN mkdir /var/log/v2ray/ \  
&& chmod +x /usr/bin/v2ray/v2ray  
  
ENV PATH /usr/bin/v2ray:$PATH  
  
CMD ["v2ray", "-config=/etc/v2ray/config.json"]  

