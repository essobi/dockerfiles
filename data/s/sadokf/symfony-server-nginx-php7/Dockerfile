FROM sadokf/php7-nginx-supervisord  
  
COPY resources/etc/ /etc/  
  
ADD . /var/www/html  
WORKDIR /var/www/html  
  
CMD ["/usr/bin/supervisord"]

