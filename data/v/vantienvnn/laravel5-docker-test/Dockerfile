FROM vantienvnn/laravel5-docker-build:latest  
  
# Apply Nginx configuration  
RUN apt-get update \  
&& apt-get install -y nginx vim openssh-server php5.6-xdebug \  
&& mkdir -p "/var/www/laravel" \  
&& chown jenkins:jenkins "/var/www/laravel" \  
&& chmod 0777 "/var/www/laravel" \  
&& touch /init-start.sh && rm -f /init-start.sh \  
&& phpdismod xdebug  
&& chsh -s /bin/bash jenkins  
  
ADD config/nginx.conf /etc/nginx/nginx.conf  
ADD config/laravel.conf /etc/nginx/sites-available/laravel.conf  
RUN ln -s /etc/nginx/sites-available/laravel.conf /etc/nginx/sites-
enabled/laravel.conf \  
&& rm -f /etc/nginx/sites-enabled/default  
  
VOLUME /var/www/laravel  
  
# Standard SSH port  
EXPOSE 22  
# Standard HTTP port  
EXPOSE 80  
ADD config/init-start.sh /init-start.sh  
RUN chmod +x /init-start.sh  
# Default command  
ENTRYPOINT ["/init-start.sh"]  

