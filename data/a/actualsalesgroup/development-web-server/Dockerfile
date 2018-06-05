FROM actualsalesgroup/cleaned-docker-image:latest  
MAINTAINER Miguel Simões <miguel.simoes@actualsalesgroup.com>  
#  
# Ensure that we have the latest packages associated with the image  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -qq libssl1.0.0
php7.0-fpm php7.0-apcu-bc php7.0-apcu php7.0-bcmath php7.0-curl php7.0-cli
php7.0-json php7.0-mbstring php7.0-mcrypt php7.0-memcached php7.0-mysql
php7.0-soap php7.0-sqlite3 php7.0-xdebug php7.0-xmlrpc php7.0-xsl runit wget  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -qq  
#  
# We need to ensure that the opcache directory is available for  
# the cli scripts  
RUN mkdir -p /var/tmp/php/opcache  
RUN chown -Rf www-data:www-data /var/tmp/php  
#  
# Add the external packages that are required to be installed  
RUN wget --quiet https://getcomposer.org/installer -O /tmp/composer-setup.php  
#  
# Install the composer phar on a global scale of the container  
RUN php /tmp/composer-setup.php --install-dir=/usr/local/bin
--filename=composer  
RUN chmod a+x /usr/local/bin/*  
#  
# Ensure that the PHP CLI configuration is optimized for the environment  
RUN sed -i -e "s/;opcache.enable=0/opcache.enable=1/g"
/etc/php/7.0/cli/php.ini  
RUN sed -i -e "s/;opcache.enable_cli=0/opcache.enable_cli=0/g"
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
# Ensure that the PHP-FPM configuration is optimized for the environment  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/session.hash_function\s*=\s*0/session.hash_function=1/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/memory_limit\s*=\s*128M/memory_limit=32M/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/;opcache.enable=0/opcache.enable=1/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e
"s/;opcache.max_accelerated_files=2000/;opcache.max_accelerated_files=4000/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e
"s/;opcache.interned_strings_buffer=4/opcache.interned_strings_buffer=8/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/;opcache.revalidate_freq=2/opcache.revalidate_freq=0/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/;opcache.fast_shutdown=0/opcache.fast_shutdown=1/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize=no/g" /etc/php/7.0/fpm/php-
fpm.conf  
RUN sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php/7.0/fpm/pool.d/www.conf  
RUN sed -i -e "s/;clear_env\s*=\s*no/clear_env=no/g"
/etc/php/7.0/fpm/pool.d/www.conf  
#  
# We need to remove the modules we do not want to be available on PHP when
running  
# on CLI  
RUN phpdismod -s cli apcu_bc  
RUN phpdismod -s cli apcu  
#  
# Install the openresty package provided with the container for improved  
# usage of the nginx http server (see https://openresty.org/en/)  
ADD debs/openresty_1.11.2.2rc1_amd64.deb /tmp/  
RUN dpkg -i /tmp/openresty_1.11.2.2rc1_amd64.deb  
#  
# Add the required service configuration to runit and ensure that they  
# have execution permissions associated  
ADD services/openresty.service /etc/service/openresty/run  
ADD services/php7-fpm.service /etc/service/php7-fpm/run  
#  
# Create the required directories for the openresty modules we are going  
# to use  
RUN mkdir -p /opt/openresty/nginx/lua  
RUN mkdir -p /opt/openresty/nginx/conf/conf.d  
RUN mkdir -p /opt/openresty/nginx/conf/sites-available  
RUN mkdir -p /opt/openresty/nginx/conf/sites-enabled  
RUN mkdir -p /var/run/php  
#  
# Move the UUID4 lua script to openresty configuration folder to be enabled  
ADD conf/nginx/lua/uuid4.lua /opt/openresty/nginx/lua/uuid4.lua  
ADD conf/nginx/nginx.conf /opt/openresty/nginx/conf/nginx.conf  
#  
# Remove the packages that are no longer required after the package has been
installed  
RUN DEBIAN_FRONTEND=noninteractive apt-get purge wget -y -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -qq -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean -y -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean -y -qq  
#  
# Remove all non-required information from the system to have the smallest  
# image size as possible  
RUN rm -rf /usr/share/doc/* /usr/share/man/?? /usr/share/man/??_*
/usr/share/locale/* /var/cache/debconf/*-old /var/lib/apt/lists/* /tmp/*  
#  
# Make the volumes available on the container  
VOLUME [ "/var/www/html" ]  
#  
# Expore the ports that are going to be available on the container  
EXPOSE 80 443  
#  
# And we start the container...  
CMD ["/usr/bin/runsvdir", "/etc/service"]  
  

