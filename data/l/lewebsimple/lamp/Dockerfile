FROM ubuntu:xenial  
MAINTAINER Pascal Martineau <pascal@lewebsimple.ca>  
  
# Copy apt sources list for PHP 5.6  
COPY ondrej-php-xenial.list /etc/apt/sources.list.d/ondrej-php-xenial.list  
  
# Install packages  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C \  
&& apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apache2 \  
git \  
less \  
mysql-server \  
nano \  
openssh-client \  
php5.6 \  
php5.6-cli \  
php5.6-curl \  
php5.6-dev \  
php5.6-gd \  
php5.6-intl \  
php5.6-mbstring \  
php5.6-mcrypt \  
php5.6-mysqli \  
php5.6-xml \  
php5.6-zip \  
php-pear \  
php-xdebug \  
rsync \  
supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
# Apache2 post-installation adjustments  
RUN usermod --non-unique --uid 1000 www-data \  
&& groupmod --non-unique --gid 1000 www-data \  
&& rm -rf /var/www/html && mkdir -p /var/www/html \  
&& chown -R www-data:www-data /var/log/apache2 /var/www/html \  
&& a2enmod headers rewrite  
  
# MySQL post-installation adjustments  
RUN rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
&& chmod 777 /var/run/mysqld \  
&& sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/mysql.conf.d/mysqld.cnf  
  
# Copy configuration and scripts  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
COPY default-vhost.conf /etc/apache2/sites-available/default-vhost.conf  
COPY docker-entrypoint.sh /  
COPY docker-mysqld.cnf /etc/mysql/conf.d/docker-mysqld.cnf  
COPY docker-php.ini /etc/php/5.6/apache2/conf.d/50-docker-php.ini  
COPY magento-php.ini /etc/php/5.6/apache2/conf.d/60-magento-php.ini  
COPY docker-php.ini /etc/php/5.6/cli/conf.d/50-docker-php.ini  
COPY supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
COPY supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
COPY xdebug.ini /etc/php/5.6/mods-available/xdebug.ini  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Install WP-CLI  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp \  
&& echo "alias wp='wp --allow-root'" >> ~/.bashrc  
  
VOLUME ["/var/lib/mysql", "/var/www/html"]  
  
EXPOSE 80 3306  
WORKDIR /var/www/html  
CMD ["/docker-entrypoint.sh"]  

