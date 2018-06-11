FROM alpine:3.4  
MAINTAINER benya <benya.drupal@gmail.com>  
  
RUN apk add --no-cache varnish  
  
COPY default.vcl /etc/varnish/  
WORKDIR /etc/varnish  
  
EXPOSE 6081 6082  
COPY docker-entrypoint.sh /usr/local/bin/  
CMD "docker-entrypoint.sh"  

