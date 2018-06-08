FROM louisbl/php:5.6-cli  
MAINTAINER louisbl <louis@beltramo.me>  
  
# Set memory limit  
RUN echo "memory_limit=1024M" > /usr/local/etc/php/conf.d/memory-limit.ini  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Display version information  
RUN composer --version  
  
RUN mkdir -p /var/www && chown -R www-data:www-data /var/www  
WORKDIR /var/www/  
  
USER www-data  
  
ENTRYPOINT ["composer"]  
CMD ["--help"]  

