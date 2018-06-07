FROM nginx:stable-alpine  
  
LABEL maintainer="fathershawn"  
  
WORKDIR /var/www/html  
VOLUME /var/www/html  
  
# Ensure www-data user exists.  
RUN addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY symfony.conf /etc/nginx/conf.d/default.conf  
  
ENV DOCROOT="/var/www/html" \  
SERVER_NAME="_"  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

