# Quagga based on Alpine  
FROM alpine  
  
MAINTAINER IWASE Yusuke <iwase.yusuke0@gmail.com>  
ARG user=iwaseyusuke  
  
USER root  
WORKDIR /root  
  
COPY ENTRYPOINT.sh /ENTRYPOINT.sh  
  
RUN apk add --no-cache quagga \  
&& touch /etc/quagga/zebra.conf \  
&& touch /etc/quagga/vtysh.conf \  
&& chmod +x /ENTRYPOINT.sh  
  
ENTRYPOINT ["/ENTRYPOINT.sh"]  

