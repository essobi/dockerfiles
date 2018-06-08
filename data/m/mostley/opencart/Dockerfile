FROM php:5.6-apache  
MAINTAINER Sven Hecht <sven@shdev.de>  
  
RUN a2enmod rewrite  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y libpng12-dev libjpeg-dev libmcrypt-dev unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mcrypt mbstring mysqli zip  
  
WORKDIR /var/www/html  
  
ENV OPENCART_VER 2.2.0.0  
ENV OPENCART_MD5 a9219f14b3483f867ea48218a0bf215d  
ENV OPENCART_URL
https://github.com/opencart/opencart/archive/${OPENCART_VER}.tar.gz  
ENV OPENCART_FILE opencart.tar.gz  
ENV OPENCART_GERMAN_URL
https://github.com/mostley/dockerfiles/raw/master/opencart/Translation-German-
de-DE-Complete-v.1.2.0-OpenCart-2.x-by-OSWorX.net.ocmod.zip  
ENV OPENCART_GERMAN_FILE opencart_german.zip  
ENV OPENCART_GERMAN_MD5 67c603e4c22ff31d56c9bc640a0f9a99  
  
RUN set -xe \  
&& curl -sSL ${OPENCART_URL} -o ${OPENCART_FILE} \  
&& echo "${OPENCART_MD5} ${OPENCART_FILE}" | md5sum -c \  
&& tar xzf ${OPENCART_FILE} \--strip 2 --wildcards '*/upload/' \  
&& mv config-dist.php config.php \  
&& mv admin/config-dist.php admin/config.php \  
&& rm ${OPENCART_FILE}  
  
RUN set -xe \  
&& curl -sSL ${OPENCART_GERMAN_URL} -o ${OPENCART_GERMAN_FILE} \  
&& echo "${OPENCART_GERMAN_MD5} ${OPENCART_GERMAN_FILE}" | md5sum -c \  
&& unzip ${OPENCART_GERMAN_FILE} -d german \  
&& rm ${OPENCART_GERMAN_FILE} \  
&& cp -r german/upload/* .  
  
RUN set -xe \  
&& chown -R www-data:www-data .  
  

