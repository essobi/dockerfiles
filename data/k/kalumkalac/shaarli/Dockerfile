FROM richarvey/nginx-php-fpm:php5  
RUN sed "s#/var/www/html#/usr/share/shaarli#" -i /etc/nginx/sites-
enabled/default.conf  
RUN sed '/server_name/d' -i /etc/nginx/sites-enabled/default.conf  
RUN sed "s#display_errors = On#display_errors = Off#" -i /etc/php5/php.ini  
ADD shaarli.sh /shaarli.sh  
  
WORKDIR /usr/share/  
RUN git clone https://github.com/shaarli/Shaarli.git -b v0.7.0 shaarli  
WORKDIR /usr/share/shaarli  
RUN chmod -R a+wx cache data pagecache tmp  
  
# Expose Ports  
EXPOSE 443  
EXPOSE 80  
VOLUME ["/usr/share/shaarli/data"]  
CMD ["/bin/bash", "/shaarli.sh"]  

