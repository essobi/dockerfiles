FROM php:7.1.14-apache  
EXPOSE 80  
ARG PHPBB_URL=https://www.phpbb.com/files/release/phpBB-3.2.1.zip  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y unzip libpng-dev
imagemagick git netcat \  
&& rm -rf /var/lib/apt/lists/*  
RUN docker-php-ext-install mysqli gd  
RUN a2enmod rewrite  
  
RUN curl $PHPBB_URL -o /tmp/phpbb.zip  
RUN unzip /tmp/phpbb.zip -d /tmp/  
RUN cp -a /tmp/phpBB3/. /var/www/html/  
RUN rm /tmp/phpbb.zip  
RUN rm -rf /tmp/phpBB3/  
RUN mkdir -p /var/www/html/cache/  

