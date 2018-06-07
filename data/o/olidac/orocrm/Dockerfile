FROM php:5.6-apache  
  
  
ENV OROCRM_GIT_URL https://github.com/orocrm/crm-application.git  
ENV OROCRM_VERSION 1.8.2  
# Install needed software and dependencies  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -qy \  
git \  
libicu-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
nano \  
vim \  
nodejs && \  
apt-get clean  
  
# Install PHP extensions  
RUN docker-php-ext-install \  
gd \  
intl \  
mbstring \  
mcrypt \  
opcache \  
pdo_mysql \  
soap \  
zip  
  
#Install apcu  
RUN pecl install apcu-beta \  
&& echo extension=apcu.so > /usr/local/etc/php/conf.d/apcu.ini  
  
# Install and setup composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
# Download sources  
WORKDIR /var/www/orocrm  
RUN git config --global url.https://github.com/.insteadOf git@github.com:  
RUN git clone -b $OROCRM_VERSION $OROCRM_GIT_URL .  
  
# Copy configs and scripts  
COPY config/php.ini /usr/local/etc/php/  
COPY config/OroRequirements.php app/  
  
# Get dependencies  
RUN composer install  
  
#script for dev  
COPY nocache/app_nocache.php web/  
COPY nocache/console-nocache app/  
  
RUN chown -R www-data:www-data web/app_nocache.php  
  
RUN sed -i 's/database_host: 127.0.0.1/database_host: dborocrm/'
/var/www/orocrm/app/config/parameters.yml  
RUN sed -i "s/database_name: oro_crm/database_name: oro_crm/"
/var/www/orocrm/app/config/parameters.yml  
RUN sed -i "s/database_user: root/database_user: orocrm/"
/var/www/orocrm/app/config/parameters.yml  
RUN sed -i "s/database_password: null/database_password: orocrm/"
/var/www/orocrm/app/config/parameters.yml  
  
RUN chown -R www-data:www-data web app/cache app/config/parameters.yml
app/logs app/attachment  
RUN rm -rf /var/www/html && ln -s /var/www/orocrm/web /var/www/html  
RUN a2enmod rewrite  
  
VOLUME /var/www/orocrm/src  
  
EXPOSE 80  
CMD ["apache2-foreground"]

