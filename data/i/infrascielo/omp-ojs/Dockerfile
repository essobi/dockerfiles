FROM php:5.6-apache  
  
MAINTAINER Rondineli Saad <rondineli.saad@scielo.org>  
  
RUN a2enmod rewrite expires  
  
# install the PHP extensions we need  
RUN apt-get -qqy update \  
&& apt-get install -qqy libpng12-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libxml2-dev \  
libxslt-dev \  
git \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd \  
mysqli \  
mysql \  
opcache \  
mcrypt \  
soap \  
xsl \  
zip  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
WORKDIR /var/www  
  
ENV SERVERNAME omp.scielo.org  
  
# Cloning and Cleaning OJS and PKP-LIB git repositories  
#RUN apt-get install git -y \  
# && git config --global url.https://.insteadOf git:// \  
# && git clone -v --recursive --progress https://github.com/pkp/omp.git
/var/www/omp \  
# && cd /var/www/omp/lib/pkp \  
# && git submodule update --init --recursive \  
# && curl -sS https://getcomposer.org/installer | php \  
# && php composer.phar update \  
# && git merge 0480ac5eafdb22a05b17a01cb821f3cc215561ca \  
# && cd /var/www/omp \  
# && cp config.TEMPLATE.inc.php config.inc.php \  
# && chown -R www-data:www-data /var/www/omp  
# creating a directory to save uploaded files.  
#RUN mkdir /var/www/files \  
# && chown -R www-data:www-data /var/www/files  
# environment to set database params  
ENV OMP_DB_HOST localhost  
ENV OMP_DB_USER omp  
ENV OMP_DB_PASSWORD omp  
ENV OMP_DB_NAME omp  
  
# Site servername  
ENV SERVERNAME=omp.scielo.org  
ENV APACHE_LOG_DIR=/var/log/apache2  
ENV LOG_NAME=omp_scielo_org  
  
# OMP Version  
ENV OMP_VERSION 3.1.0  
COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf  
COPY config/php.ini /usr/local/etc/php/  
  
EXPOSE 80  
# Add startup script to the container.  
COPY omp-startup.sh /omp-startup.sh  
# Execute the containers startup script which will start many
processes/services  
CMD ["/bin/bash", "/omp-startup.sh"]  

