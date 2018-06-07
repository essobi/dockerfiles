FROM factual/docker-base  
  
RUN apt-get install -y nginx  
RUN rm -rf /usr/share/nginx  
  
  
RUN mkdir -p /var/www/  
  
  
RUN chown -R www-data:www-data /var/www  
  
VOLUME /var/www  
  
ADD nginx-default-site /etc/nginx/sites-disabled/default  
  
ADD start.sh /etc/my_init.d/

