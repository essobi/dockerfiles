FROM composer:1.5.1  
MAINTAINER Irvin Capagcuan <irvin@capagcuan.org>  
RUN composer global require hirak/prestissimo  
RUN docker-php-ext-install sockets  
RUN mkdir -p /tmp/cache  
RUN chmod -R 777 /tmp  
VOLUME ["/var/www/html/app"]  
WORKDIR /var/www/html/app  
ENV PATH="/tmp/vendor/bin:${PATH}"  
ENTRYPOINT ["composer"]  
CMD ["list"]  

