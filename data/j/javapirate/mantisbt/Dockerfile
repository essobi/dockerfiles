FROM php:7.1-apache  
  
RUN a2enmod rewrite  
  
RUN apt-get update \  
&& apt-get install -y libpng12-dev libjpeg-dev libpq-dev libxml2-dev  
  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring mysqli pgsql soap \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV MANTIS_VER 2.5.1  
ENV MANTIS_MD5 b09bae83c8f0790056b5076b9f805c81  
ENV MANTIS_URL http://jaist.dl.sourceforge.net/project/mantisbt/mantis-
stable/${MANTIS_VER}/mantisbt-${MANTIS_VER}.tar.gz  
ENV MANTIS_FILE mantisbt.tar.gz  
  
  
  
RUN curl -fSL ${MANTIS_URL} -o ${MANTIS_FILE} \  
&& echo "${MANTIS_MD5} ${MANTIS_FILE}" | md5sum -c \  
&& mkdir -p /var/www/mantisbt \  
&& tar -xz --strip-components=1 -f ${MANTIS_FILE} -C /var/www/mantisbt \  
&& rm ${MANTIS_FILE} \  
&& chown -R www-data:www-data /var/www/mantisbt  
  
COPY mantisbt.conf /etc/apache2/sites-enabled/mantisbt.conf  
COPY index.php /var/www/html/index.php  
CMD ["apache2-foreground"]

