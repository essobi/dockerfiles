# Set the base image to latest nginx image  
FROM nginx:latest  
  
# Image author/maintainer  
MAINTAINER Randy Lowe <randy@weblogix.ca>  
  
RUN apt-get update  
RUN apt-get install -y openssl bash nano wget letsencrypt  
  
# nginx configuration  
RUN mkdir -p /etc/nginx/modules  
COPY conf/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY conf/nginx/modules /etc/nginx/modules  
COPY conf/nginx/conf.d /etc/nginx/conf.d  
  
# nginx default host  
RUN mkdir -p /var/www/html  
COPY www/ /var/www/html  
  
# PHP stuff  
RUN mkdir -p /var/lib/php/session  
RUN chown -Rf nginx:nginx /var/lib/php/session  
  
# temp stuff  
RUN mkdir -p /var/lib/nginx/cache/client_body  
  
# php session  
RUN mkdir -p /var/lib/php/session  
RUN chown -Rf nginx:nginx /var/lib/php/session  
RUN chmod -Rf 755 /var/lib/php/session  
  
# Update Diffie-Hellman Parameters  
RUN openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048  
  
# Expose ports  
EXPOSE 80  
EXPOSE 443  

