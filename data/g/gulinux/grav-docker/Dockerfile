FROM php:7-apache  
WORKDIR /var/www/  
ENV GRAV_VERSION=1.0.10  
RUN apt-get update && \  
apt-get install -y unzip libjpeg62-turbo-dev libpng12-dev libfreetype6-dev
zlib1g-dev && \  
apt-get clean && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd && \  
docker-php-ext-install zip  
RUN curl -O -L
https://github.com/getgrav/grav/releases/download/${GRAV_VERSION}/grav-
admin-v${GRAV_VERSION}.zip && \  
unzip grav-admin-v${GRAV_VERSION}.zip && \  
rm -f grav-admin-v${GRAV_VERSION}.zip && \  
rmdir html && \  
chown -R -v www-data:www-data grav-admin && \  
mv grav-admin grav  
ENV PATH="/var/www/grav/bin:${PATH}"  
VOLUME /var/www/grav  
RUN rm -rf html && ln -s grav html && a2enmod rewrite  
WORKDIR /var/www/grav  

