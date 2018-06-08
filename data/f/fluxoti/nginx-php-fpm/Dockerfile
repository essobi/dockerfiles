FROM phusion/baseimage:0.9.18  
MAINTAINER FluxoTI <lucas.gois@fluxoti.com>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Setting some PHP Env variables  
ENV PHP_ERROR_REPORTING=E_ALL PHP_DISPLAY_ERRORS=On PHP_MEMORY_LIMIT=512M
PHP_TIMEZONE=UTC \  
PHP_UPLOAD_MAX_FILESIZE=100M PHP_POST_MAX_SIZE=100M NR_INSTALL_SILENT=true  
  
COPY build /build  
# Preparing for the installation  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y curl
openssl pkg-config \  
wget vim supervisor git && echo "export TERM=xterm" >> ~/.bashrc  
# Installing nodejs  
RUN curl \--silent \--location https://deb.nodesource.com/setup_5.x | bash -
&& \  
apt-get update && apt-get install -y \--force-yes nodejs && \  
curl -L https://npmjs.org/install.sh | sh && \  
# disabling npm progress bar to speed up installs. See:
https://github.com/npm/npm/issues/11283  
npm set progress=false && npm install gulp -g  
  
# Installing PHP and stuff  
RUN LC_ALL=en_US.UTF-8 apt-add-repository ppa:ondrej/php -y && \  
apt-get update && apt-get install -y \--force-yes php7.0-cli php7.0-dev \  
php-pgsql php-sqlite3 php-gd php-apcu \  
php-curl php7.0-mcrypt \  
php-imap php-mysql php-memcached php7.0-readline php-xdebug \  
php-mbstring php-xml php7.0-fpm && \  
  
# Installing composer  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
  
# Setting some php settings for docker  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.0/fpm/php.ini &&
\  
sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php/7.0/fpm/php-fpm.conf
&& \  
sed -i -e "s/www-data/root/g" /etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/;clear_env = no/clear_env = no/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/listen = \/run\/php\/php7.0-fpm.sock/listen =
\/var\/run\/php\/php7.0-fpm.sock/g" /etc/php/7.0/fpm/pool.d/www.conf && \  
  
# We will disable xdebug for composer and create an alias to use it with the
php comand  
rm /etc/php/7.0/cli/conf.d/20-xdebug.ini && \  
echo "alias php=\"php -dzend_extension=xdebug.so\"" >> ~/.bashrc && \  
  
# Installing the mongodb and zip extension  
pecl install mongodb zip \  
&& echo "extension=mongodb.so" >> /etc/php/7.0/fpm/conf.d/20-mongodb.ini \  
&& echo "extension=mongodb.so" >> /etc/php/7.0/cli/conf.d/20-mongodb.ini \  
&& echo "extension=zip.so" >> /etc/php/7.0/fpm/conf.d/20-zip.ini \  
&& echo "extension=zip.so" >> /etc/php/7.0/cli/conf.d/20-zip.ini  
# Installing NGINX  
RUN apt-get install -y \--force-yes nginx && \  
rm /etc/nginx/nginx.conf && cp /build/templates/nginx.conf
/etc/nginx/nginx.conf && \  
rm /etc/nginx/sites-available/default && \  
cp /build/templates/virtualhost /etc/nginx/sites-available/default  
# Installing new relic monitor agent  
RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | sudo tee
/etc/apt/sources.list.d/newrelic.list && \  
wget -O- https://download.newrelic.com/548C16BF.gpg | sudo apt-key add - && \  
sudo apt-get update \--force-yes -y && \  
sudo apt-get install newrelic-php5 -y \--force-yes && \  
sudo newrelic-install install && \  
rm /etc/php/7.0/cli/conf.d/newrelic.ini && rm
/etc/php/7.0/fpm/conf.d/newrelic.ini  
  
RUN service php7.0-fpm stop && service nginx stop && service supervisor stop
&& \  
  
# Run PHP and Nginx with runit  
mkdir /etc/service/php7.0-fpm && mkdir /run/php && cp /build/run/php-fpm.sh
/etc/service/php7.0-fpm/run \  
&& chmod +x /etc/service/php7.0-fpm/run && \  
mkdir /etc/service/nginx && cp /build/run/nginx.sh /etc/service/nginx/run &&
chmod +x /etc/service/nginx/run && \  
mkdir /etc/service/supervisor && cp /build/run/supervisor.sh
/etc/service/supervisor/run && \  
chmod +x /etc/service/supervisor/run  
  
EXPOSE 80  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && rm -rf
/build

