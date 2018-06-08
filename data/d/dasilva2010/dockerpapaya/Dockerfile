FROM php:5.6-apache  
MAINTAINER Jan Boerner <jan@boerner.xyz>  
  
# install needed tools  
RUN apt-get update; \  
apt-get -y install git wget libxslt-dev libmcrypt-dev libpng12-dev libjpeg-dev
zip; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/*; \  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install xsl mcrypt mysql mysqli gd; \  
echo [Date] > $PHP_INI_DIR/conf.d/docker-php-ext-date.ini; \  
echo date.timezone = UTC >> $PHP_INI_DIR/conf.d/docker-php-ext-date.ini  
  
# installing composer  
ADD install-composer.sh /install-composer.sh  
RUN chmod +x /install-composer.sh; \  
/install-composer.sh; \  
rm /install-composer.sh  
  
# install phing and xhprof  
RUN pear channel-discover pear.phing.info; \  
pear install --alldeps phing/phing; pecl install -f xhprof; \  
echo extension=xhprof.so >> $PHP_INI_DIR/conf.d/docker-php-ext-xhprof.ini  
  
WORKDIR /var/www  
RUN chown -R www-data:www-data /var/www  
  
USER www-data  
# load and install papaya core system  
RUN wget https://github.com/papayaCMS/papayacms-core/archive/master.zip -O
papaya-core.zip; \  
unzip papaya-core.zip; \  
rm papaya-core.zip; \  
cd papayacms-core-master; \  
composer install  
  
# create and setup a new project  
RUN composer --ansi create-project papaya/cms-project dockerpapaya; \  
cd /var/www/dockerpapaya; \  
composer require papaya/theme-dynamic; \  
composer require papaya/module-mail  
  
EXPOSE 80 443  
VOLUME /var/www/dockerpapaya/papaya-data  
  
USER root  
ADD papayacms.conf /etc/apache2/sites-available/  
RUN rm /etc/apache2/sites-enabled/*.conf; ln -s /etc/apache2/sites-
available/papayacms.conf /etc/apache2/sites-enabled/papayacms.conf; ln -s
/etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

