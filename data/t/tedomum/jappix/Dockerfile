FROM php:apache  
  
WORKDIR /var/www/html  
  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg62-turbo-dev
libfreetype6-dev libmcrypt-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install mysqli mbstring gd  
  
RUN apt-get install -y unzip  
  
ENV JAPPIX_URL https://download.jappix.org/1.1.6/jappix-1.1.6-primo.zip  
  
RUN rm -rf /var/www/html/*  
RUN curl -L -O ${JAPPIX_URL} \  
&& unzip jappix-*.zip \  
&& mv jappix/* ./ \  
&& rm -rf jappix-*.zip jappix/ *.md  
  
COPY config/php.ini /usr/local/etc/php/  
  
EXPOSE 80  
VOLUME /var/www/html/tmp  
VOLUME /var/www/html/log  
VOLUME /var/www/html/store  
  

