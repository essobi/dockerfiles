# Import base image  
FROM birkof/ubuntu  
  
# PHP5.6 & Java repo & Blackfire.io && latest Node.js package  
RUN export LANG=C.UTF-8 \  
&& add-apt-repository -y ppa:ondrej/php5-5.6 \  
&& wget -O - https://packagecloud.io/gpg.key | sudo apt-key add - \  
&& echo "deb http://packages.blackfire.io/debian any main" | sudo tee
/etc/apt/sources.list.d/blackfire.list \  
&& curl -sL https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get install -yq --no-install-recommends nodejs  
  
# Install nginx & php5.6-fpm package and some dependecies  
RUN apt-get install -yq --no-install-recommends \  
nginx \  
php5-common \  
php5-fpm \  
php5-cli \  
php5-mcrypt \  
php5-mysql \  
php5-apcu \  
php5-gd \  
php5-imagick \  
php5-curl \  
php5-intl \  
php5-memcache \  
php5-memcached \  
php5-xdebug \  
php-pear \  
blackfire-php  
  
# Injecting container assets files  
ADD .docker /  
  
# Set timezone in php.ini  
RUN sed -i".bak" "s@^;date.timezone =.*@date.timezone = $TIMEZONE@"
/etc/php5/*/php.ini  
  
# Tweak php-fpm logging  
RUN mkdir -p /var/log/php5 \  
&& sed -i 's/;log_level = .*/log_level = debug/g' /etc/php5/fpm/php-fpm.conf \  
&& sed -i 's/;daemonize = yes/daemonize = no/g' /etc/php5/fpm/php-fpm.conf \  
&& sed -i -e "s/^\error_log = .*$/error_log = \/var\/log\/php5\/php-fpm.log/g"
/etc/php5/fpm/php-fpm.conf  
  
# Activate CLI extensions  
RUN find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
# Change the UID of www-data for OSX writing permission problem  
RUN usermod -u 1000 www-data  
  
# Install composer  
RUN curl -LsS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer --version  
  
# get PHP CodeSniffer (https://pear.php.net/package/PHP_CodeSniffer)  
RUN curl -LsS https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar -o
/usr/local/bin/phpcs \  
&& chmod a+x /usr/local/bin/phpcs \  
&& phpcs --version  
  
# php-cs-fixer  
RUN curl http://get.sensiolabs.org/php-cs-fixer.phar -o php-cs-fixer \  
&& chmod a+x php-cs-fixer \  
&& mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
# Install phpunit  
RUN curl -LsS https://phar.phpunit.de/phpunit.phar -o /usr/local/bin/phpunit \  
&& chmod a+x /usr/local/bin/phpunit \  
&& phpunit --version  
  
# Clean up the mess  
RUN apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Exposed port/s  
EXPOSE 22 80  
# Working dir  
WORKDIR /var/www  

