FROM php:5.6-apache  
  
ENV FLICKR_KEY KEY  
ENV FLICKR_SECRET SECRET  
  
# Install gd  
RUN apt-get update && apt-get install -y \  
unzip \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN a2enmod rewrite  
  
COPY ./ /var/www/html/  
  
WORKDIR /var/www/html  
  
RUN \  
curl -o phpflickr.zip -L https://github.com/dan-
coulter/phpflickr/archive/master.zip && \  
unzip phpflickr.zip && \  
rm -rf /var/www/html/includes/phpFlickr && \  
mv phpflickr-master includes/phpFlickr  
  
RUN chown -R www-data /var/www/html/cache/  

