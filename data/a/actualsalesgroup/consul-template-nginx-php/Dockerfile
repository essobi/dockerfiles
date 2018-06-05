FROM actualsalesgroup/consul-template-php:develop  
MAINTAINER devops@actualsalesgroup.com  
#  
# Ensure that the server has the correct timezone installed  
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime  
#  
# Ensure that we have the latest packages associated with the image  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qq libssl1.0.0 php7.0-fpm
php7.0-apcu php7.0-apcu-bc -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -qq  
#  
# Install the openresty package provided with the container for improved  
# usage of the nginx http server (see https://openresty.org/en/)  
ADD debs/openresty_1.11.2.2_amd64.deb /tmp/  
RUN dpkg -i /tmp/openresty_1.11.2.2_amd64.deb  
#  
# Add the required service configuration to runit and ensure that they  
# have execution permissions associated  
ADD services/openresty.service /etc/service/openresty/run  
ADD services/php7-fpm.service /etc/service/php7-fpm/run  
ADD services/consul-template.service /etc/service/consul-template/run  
#  
# Add the nginx template to be parsed to the configuration folder  
ADD consul-templates/nginx.conf /etc/consul-templates/  
  
# To enable maxminddb module, please uncomment the line below  
#RUN phpenmod -s ALL maxminddb  
#  
# Create the required directories for the modules we are going to use  
RUN mkdir -p /opt/openresty/nginx/lua  
RUN mkdir -p /opt/openresty/nginx/conf/conf.d  
RUN mkdir -p /var/run/php  
#  
# Move the UUID4 lua script to openresty configuration folder to be enabled  
ADD conf/nginx/lua/uuid4.lua /opt/openresty/nginx/lua/uuid4.lua  
ADD conf/nginx/conf/conf.d/default.conf
/opt/openresty/nginx/conf/conf.d/default.conf  
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
RUN sed -i -e "s/;opcache.revalidate_freq=2/opcache.revalidate_freq=60/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/;opcache.fast_shutdown=0/opcache.fast_shutdown=1/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize=no/g" /etc/php/7.0/fpm/php-
fpm.conf  
RUN sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php/7.0/fpm/pool.d/www.conf  
#  
# We need to remove the modules we do not want to be available on PHP when
running  
# on CLI  
RUN rm -rf /etc/php5/cli/conf.d/20-apcu.ini  
#  
# Remove the packages that are no longer required after the package has been
installed  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -q -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean -y -q  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean -y  
#  
# Remove all non-required information from the system to have the smallest  
# image size as possible  
RUN rm -rf /usr/share/doc/* /usr/share/man/?? /usr/share/man/??_*
/usr/share/locale/* /var/cache/debconf/*-old /var/lib/apt/lists/* /tmp/*  
#  
# And we start the container...  

