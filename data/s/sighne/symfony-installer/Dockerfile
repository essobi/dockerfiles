FROM php:7  
MAINTAINER Sighne<sighne@foamyhorn.com>  
  
RUN mkdir -p /usr/local/bin  
WORKDIR /app  
  
# Get Symfony installer  
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony  
RUN chmod a+x /usr/local/bin/symfony  
  
# Configure PHP for Symfony  
RUN echo "date.timezone=UTC" > /usr/local/etc/php/php.ini  
RUN docker-php-ext-install pdo pdo_mysql  
  
ENTRYPOINT ["symfony"]  
CMD ["help"]  

