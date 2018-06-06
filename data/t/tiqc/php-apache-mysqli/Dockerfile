FROM navysu/php-apache-ssmtp  
  
MAINTAINER Haijun (Navy) Su <navysu@gmail.com>  
  
RUN mkdir -p /storage/wwwroot \  
&& docker-php-ext-install mysqli  
  
WORKDIR /var/www/html  
  
EXPOSE 80  

