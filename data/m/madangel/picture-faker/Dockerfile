FROM tutum/apache-php  
  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
ADD app/ /app  
  
RUN php -v  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

