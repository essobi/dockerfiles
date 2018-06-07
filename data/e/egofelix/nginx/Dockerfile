FROM alpine  
  
MAINTAINER EgoFelix <docker@egofelix.de>  
  
# Install nginx  
RUN apk --no-cache add \  
nginx \  
&& \  
mkdir -p /run/nginx/ /etc/nginx/sites-enabled/ /var/log/nginx/  
  
# Install config  
COPY nginx.conf /etc/nginx  
  
# Entry  
ENTRYPOINT /usr/sbin/nginx -g 'daemon off;'

