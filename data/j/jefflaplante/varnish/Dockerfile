FROM alpine:3.4  
MAINTAINER Jeff LaPlante <jeff.laplante@disney.com>  
  
ENV VARNISH_CACHE_SIZE=256M  
  
RUN apk add --no-cache varnish bash  
  
COPY start.sh /start.sh  
  
EXPOSE 6081  
CMD ["/start.sh"]  
  
COPY default.vcl /etc/varnish/default.vcl  

