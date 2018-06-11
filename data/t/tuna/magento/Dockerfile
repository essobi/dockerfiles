FROM tuna/php:5.6-apache2  
  
# Install git  
RUN apt-get update && apt-get install -y git  
  
# copy php.ini  
COPY php.ini /usr/local/etc/php/  
  
# download magento2  
RUN git clone -b master https://tuna7_fsoft@bitbucket.org/gkanters/magento.git
/var/www/magento2  
  
# enable gd extension  
RUN apt-get install -y libvpx-dev libfreetype6-dev libjpeg62-turbo-dev
libpng12-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ --with-vpx-dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
# enable mcrypt xsl intl mbstring zip extensions  
RUN apt-get install -y libxslt-dev libmcrypt-dev libicu-dev  
RUN docker-php-ext-install mcrypt xsl intl mbstring zip  
  
# install composer & magento2  
WORKDIR /var/www/magento2  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN composer install  
  
# enable apache Expires module  
RUN ln -s /etc/apache2/mods-available/expires.load /etc/apache2/mods-enabled/  
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/  
# Add magento2 to httpd.conf  
RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist  
COPY apache2.conf /etc/apache2/apache2.conf  
  
EXPOSE 80  
CMD ["apache2-foreground"]  

