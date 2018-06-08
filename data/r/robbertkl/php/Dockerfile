FROM robbertkl/base-s6  
MAINTAINER Robbert Klarenbeek <robbertkl@renbeek.nl>  
  
# Install packages and clean up after apt  
RUN cleaninstall \  
nginx \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-mcrypt \  
php5-mysql \  
php5-sqlite \  
php5-xsl  
  
# Install composer  
RUN php -r "readfile('https://getcomposer.org/installer');" | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Configure services  
COPY etc /etc  
RUN rm -rf /etc/php5/fpm/pool.d  
  
# Development workaround (boot2docker)  
RUN usermod -u 1000 -G staff www-data  
  
# Overridable environment variables  
ENV DOCUMENT_ROOT=/var/www \  
PHP_MEMORY_LIMIT=128M \  
PHP_ERROR_REPORTING="E_ALL & ~E_DEPRECATED & ~E_STRICT"  
# Add a default (phpinfo) website  
WORKDIR ${DOCUMENT_ROOT}  
RUN rm -rf *  
COPY index.php ./  
  
# Expose HTTP  
EXPOSE 80  

