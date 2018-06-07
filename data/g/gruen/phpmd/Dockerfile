#################################################################################  
# PHPMD Task Runner  
# Use docker run -it --rm -v $(pwd):/app gruen/phpmd:php-5.6 [ phpmd options ]  
#################################################################################  
FROM php:5.6-cli  
MAINTAINER Darren Green <darrensgreen@gmail.com>  
  
WORKDIR /  
COPY phpmd/2.4.3.phar /usr/bin/phpmd  
RUN chmod 700 /usr/bin/phpmd  
RUN apt-get update  
RUN apt-get install bzip2  
RUN apt-get install -y libbz2-dev  
RUN which bzip2  
RUN docker-php-ext-configure bz2 --with-bz2=/bin/bzip2  
RUN docker-php-ext-install -j$(nproc) bz2  
RUN pecl install phar  
  
WORKDIR /app  
  
ENTRYPOINT ["phpmd"]  

