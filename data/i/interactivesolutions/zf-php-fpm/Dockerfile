FROM php:7.1-fpm  
MAINTAINER Antoine Hedgecock <antoine.hedgecock@gmail.com>  
  
# Get the latest version  
RUN apt-get update && apt-get install -y git zlib1g-dev libcurl4-openssl-dev
libicu-dev postgresql-server-dev-all && apt-get clean  
  
# Download and extract redis  
RUN curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/3.1.5.tar.gz \  
&& tar xfz /tmp/redis.tar.gz \  
&& rm -r /tmp/redis.tar.gz \  
&& mkdir -p /usr/src/php/ext \  
&& mv phpredis-3.1.5 /usr/src/php/ext/redis  
  
# Install the required extensions  
RUN docker-php-ext-install mbstring pdo_pgsql pdo_mysql zip opcache intl
bcmath redis  
  
# Do some basic configuration  
RUN echo "date.timezone = Europe/Stockholm" > /usr/local/etc/php/php.ini  
RUN echo "memory_limit = 512M" >> /usr/local/etc/php/php.ini  
RUN echo "upload_max_filesize = 20M" >> /usr/local/etc/php/php.ini  
  
# Mark as volume  
VOLUME /var/www/html  
  
# Change the work dir to it  
WORKDIR /var/www/html  
  
# Install the entrypoint  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm"]  

