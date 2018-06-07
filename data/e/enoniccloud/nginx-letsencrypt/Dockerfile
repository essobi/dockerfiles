FROM nginx:stable-alpine  
  
MAINTAINER Erik Kaareng-Sunde <esu@enonic.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apk update && apk add ca-certificates openssl certbot  
  
RUN cd /etc/ssl/certs && openssl dhparam -out dhparam.pem 2048  
  
COPY launcher.sh /usr/local/bin/launcher.sh  
RUN chmod +x /usr/local/bin/launcher.sh  
COPY nginx-default.conf /etc/nginx/conf.d/default.conf  
  
CMD /usr/local/bin/launcher.sh  
  
# TODO: HArden nginx: https://www.scalescale.com/tips/nginx/hardening-nginx-
ssl-tsl-configuration/  

