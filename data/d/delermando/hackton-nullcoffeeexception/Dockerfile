FROM nginx:1.9.9  
MAINTAINER Delermando  
  
RUN apt-get update && apt-get install -y \  
php5 \  
php5-fpm \  
php5-mcrypt \  
php5-curl \  
php5-gd \  
php5-mysql \  
php5-pgsql \  
php5-cli \  
memcached \  
php5-memcache \  
curl  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN touch /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
RUN mkdir /app  
  
WORKDIR /app  
  
EXPOSE 80 443  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

