FROM php:7.0.8-fpm-alpine  
  
RUN docker-php-ext-install mysqli  
RUN apk upgrade --update \  
&& apk add coreutils \  
libltdl \  
&& apk add --virtual build-dependencies \  
freetype-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
#&& apk del build-dependencies \  
&& rm -rf /var/cache/apk/*  
  
ENV GLPI_VERSION=0.90.4  
RUN curl -L https://github.com/glpi-
project/glpi/releases/download/${GLPI_VERSION}/glpi-${GLPI_VERSION}.tar.gz -o
/tmp/glpi.tar.gz && \  
mkdir /usr/share/nginx/ && \  
tar xvfz /tmp/glpi.tar.gz -C /usr/share/nginx/ && \  
rm -f /tmp/glpi.tar.gz  
  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/local/sbin/php-fpm"]  
  
WORKDIR /usr/share/nginx/glpi  
  

