FROM wordpress:php7.0-apache  
  
RUN ln -sf /usr/share/zoneinfo/EST5EDT /etc/localtime  
  
COPY .htaccess /var/www/html  
  
## Expose ports  
EXPOSE 80  

