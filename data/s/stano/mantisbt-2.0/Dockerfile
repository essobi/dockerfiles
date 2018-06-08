FROM php:5.6-apache  
MAINTAINER Stano M.  
  
RUN a2enmod rewrite  
  
RUN apt-get update && apt-get install -y \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
libxml2-dev \  
vim-tiny \  
ssmtp \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring mysql mysqli pgsql soap \  
&& rm -rf /var/lib/apt/lists/* /var/www/html/index.html  
  
ENV MANTIS_VER 2.0.0  
ENV MANTIS_URL https://sourceforge.net/projects/mantisbt/files/mantis-
stable/${MANTIS_VER}/mantisbt-${MANTIS_VER}.tar.gz  
ENV MANTIS_FILE mantisbt.tar.gz  
  
RUN mkdir -p /var/lib/mantisbt \  
&& cd /var/lib/mantisbt \  
&& curl -fSL ${MANTIS_URL} -o ${MANTIS_FILE} \  
&& tar -xz --strip-components=1 -f ${MANTIS_FILE} \  
&& rm ${MANTIS_FILE} \  
&& chown -R www-data:www-data .  
  
ADD ./entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  

