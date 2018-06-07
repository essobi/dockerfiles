FROM nginx:1.13-alpine  
  
# ensure www-data user exists  
RUN set -x \  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data  
  
COPY nginx.conf.template /etc/nginx/nginx.conf.template  

