FROM php:5.6-apache  
  
ENV KATANA_VERSION 0.3.2  
WORKDIR /var/www/html  
  
# necessary tools  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
# custom PHP configuration  
COPY config/php.ini /usr/local/etc/php/  
  
# custom apache vhost  
COPY config/vhost.conf /etc/apache2/sites-enabled/  
  
# some usefull PHP extensions  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends zlib1g-dev \  
&& docker-php-ext-install mbstring pdo_mysql \  
&& rm -rf /var/lib/apt/lists/*  
  
# install Katana  
RUN curl -L -o katana.zip https://github.com/fruux/sabre-
katana/releases/download/$KATANA_VERSION/katana_v$KATANA_VERSION.zip \  
&& unzip katana.zip \  
&& rm katana.zip \  
&& chmod -R a+rw data/ \  
&& chown -R www-data:www-data .  
  
VOLUME /var/www/html/data  

