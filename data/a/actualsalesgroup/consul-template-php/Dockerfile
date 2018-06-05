FROM actualsalesgroup/consul-template:latest  
MAINTAINER devops@actualsalesgroup.com  
#  
# Ensure that we have the latest packages associated with the image  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ca-certificates
php7.0-bcmath php7.0-curl php7.0-cli php7.0-json php7.0-mbstring php7.0-mcrypt
php7.0-memcached php7.0-mysql php7.0-xmlrpc php7.0-xsl php7.0-dev php-pear
unzip wget  
#  
# We need to ensure that the opcache directory is available  
RUN mkdir -p /var/tmp/php/opcache  
RUN chown -Rf www-data:www-data /var/tmp/php  
#  
# Add the external packages that are required to be installed-  
RUN wget --quiet https://getcomposer.org/installer -O /tmp/composer-setup.php  
#  
# Install the composer phar on a global scale of the container  
RUN php /tmp/composer-setup.php --install-dir=/usr/local/bin
--filename=composer  
RUN chmod a+x /usr/local/bin/composer  
#  
# Install the elasticache module  
ADD lib/php/amazon-elasticache-cluster-client.so /usr/lib/php/20151012/amazon-
elasticache-cluster-client.so  
RUN chmod 644 /usr/lib/php/20151012/amazon-elasticache-cluster-client.so  
#  
# Install the libmaxminddb module and the maxminddb php extension  
ADD lib/php/maxminddb.so /usr/lib/php/20151012/maxminddb.so  
ADD lib/libmaxminddb.la /usr/lib/libmaxminddb.la  
ADD lib/libmaxminddb.so.0.0.7 /usr/lib/libmaxminddb.so.0.0.7  
RUN ln -sf /usr/lib/libmaxminddb.so.0.0.7 /usr/lib/libmaxminddb.so.0  
RUN ln -sf /usr/lib/libmaxminddb.so.0.0.7 /usr/lib/libmaxminddb.so  
ADD conf/php/7.0/mods-available/maxminddb.ini /etc/php/7.0/mods-
available/maxminddb.ini  
#  
# To enable maxminddb module, please uncomment the line below  
#RUN phpenmod -s ALL maxminddb  
#  
# Add the required configuration files to their locations before  
# we can start the container  
ADD conf/php/7.0/mods-available/memcached.ini /etc/php/7.0/mods-
available/memcached.ini  
#  
# Ensure that the PHP CLI configuration is optimized for the environment  
RUN sed -i -e "s/;opcache.enable=0/opcache.enable=1/g"
/etc/php/7.0/cli/php.ini  
RUN sed -i -e "s/;opcache.enable_cli=0/opcache.enable_cli=1/g"
/etc/php/7.0/cli/php.ini  
RUN sed -i -e
"s/;opcache.file_cache=/opcache.file_cache=\"\/var\/tmp\/php\/opcache\"/g"
/etc/php/7.0/cli/php.ini  
RUN sed -i -e "s/;opcache.file_cache_only=0/opcache.file_cache_only=1/g"
/etc/php/7.0/cli/php.ini  
RUN sed -i -e
"s/;opcache.file_cache_consistency_checks=1/opcache.file_cache_consistency_checks=1/g"
/etc/php/7.0/cli/php.ini  
#  
# Remove the packages that are no longer required after the package has been
installed  
RUN DEBIAN_FRONTEND=noninteractive apt-get purge php7.0-dev php-pear wget
unzip -y -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -qq -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean -y -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean -y -qq  
#  
# Remove all non-required information from the system to have the smallest  
# image size as possible  
RUN rm -rf /usr/share/doc/* /usr/share/man/?? /usr/share/man/??_*
/usr/share/locale/* /var/cache/debconf/*-old /var/lib/apt/lists/* /tmp/*  
#  
# And we start the container...  
CMD ["/usr/bin/runsvdir", "/etc/service"]  

