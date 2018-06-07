FROM ubuntu:14.04.2  
ENV DEBIAN_FRONTEND noninteractive  
  
# ADD BASHRC CONFIG  
COPY config/bashrc /root/  
RUN mv /root/bashrc /root/.bashrc  
  
# PHP 5.6 repository  
RUN apt-get clean && apt-get update && apt-get install --fix-missing -y
python-software-properties software-properties-common language-pack-en-base  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php5-5.6  
  
# add sources for latest nginx, install software requirements  
RUN apt-get clean && apt-get update && \  
apt-get install --fix-missing -y software-properties-common && \  
nginx=stable && \  
add-apt-repository ppa:nginx/$nginx && \  
apt-get clean && apt-get update && \  
apt-get upgrade -y && \  
BUILD_PACKAGES="apt-transport-https curl ruby-dev imagemagick graphviz sudo
vim memcached libmemcached-tools php5-cli php5-memcached php5-dev php5-mysqlnd
libpng12-dev libmcrypt-dev libxml2-dev libxslt1-dev mysql-client zip wget
supervisor nginx php5-fpm git php-apc php5-curl php5-gd php5-intl php5-mcrypt
php5-memcache php5-sqlite php5-tidy php5-xmlrpc php5-xsl php5-pgsql php5-mongo
pwgen linux-libc-dev libyaml-dev" && \  
apt-get -y install $BUILD_PACKAGES && \  
apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
# tweak nginx config  
COPY config/nginx.conf /etc/nginx/nginx.conf  
  
# tweak php-fpm config  
COPY config/php.ini /etc/php5/fpm/php.ini  
COPY config/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
COPY config/www.conf /etc/php5/fpm/pool.d/www.conf  
RUN php5enmod mcrypt  
  
COPY core/memcached.conf /etc/memcached.conf  
  
# install php5-xdebug  
RUN apt-get clean && apt-get update && apt-get install --fix-missing -y
php5-xdebug; \  
  
# SASS and Compass installation  
gem install compass; \  
  
# Installation node.js  
curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -; \  
DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends install -y
nodejs; \  
  
# Installation of LESS  
npm update -g npm && \  
npm install -g less && npm install -g less-plugin-clean-css; \  
  
# Installation of Grunt  
npm install -g grunt-cli; \  
  
# Installation of Gulp  
npm install -g gulp; \  
  
# Installation of Composer  
cd /usr/src && curl -sS http://getcomposer.org/installer | php; \  
cd /usr/src && mv composer.phar /usr/bin/composer; \  
  
# Installation of drush  
git clone https://github.com/drush-ops/drush.git /usr/local/src/drush; \  
cd /usr/local/src/drush && git checkout 8.0.5; \  
ln -s /usr/local/src/drush/drush /usr/bin/drush; \  
cd /usr/local/src/drush && composer update && composer install; \  
  
# Install xdebug memcache and mongo. uploadprogress not supported with php-fpm  
pecl install xdebug-2.2.3 memcache-3.0.8 mongo-1.6.12 yaml-1.2.0; \  
echo "extension=mongo.so" > /etc/php5/fpm/conf.d/20-mongo.ini; \  
echo "extension=yaml.so" > /etc/php5/fpm/conf.d/20-yaml.ini; \  
  
# Installation of PHP_CodeSniffer with Drupal coding standards.  
# See https://www.drupal.org/node/1419988#coder-composer  
composer global require drupal/coder; \  
ln -s ~/.composer/vendor/bin/phpcs /usr/local/bin; \  
ln -s ~/.composer/vendor/bin/phpcbf /usr/local/bin; \  
phpcs --config-set installed_paths
~/.composer/vendor/drupal/coder/coder_sniffer  
  
# installation of ssmtp  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean && apt-get update && apt-get
install --fix-missing -y ssmtp && rm -r /var/lib/apt/lists/*  
ADD core/ssmtp.conf /etc/ssmtp/ssmtp.conf  
ADD core/php-smtp.ini /usr/local/etc/php/conf.d/php-smtp.ini  
  
# nginx site conf  
RUN rm /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
COPY config/default.conf /etc/nginx/sites-available/default  
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
RUN chown -R www-data:www-data /var/www  
  
# Setup Volume  
VOLUME ["/var/www/html"]  
  
# create directory for ssh keys  
RUN mkdir /var/www/.ssh/  
RUN chown -R www-data:www-data /var/www/.ssh/  
RUN chmod -R 600 /var/www/.ssh/  
  
WORKDIR /var/www/html  
  
# Expose Ports  
EXPOSE 80 9000  
# Start entrypoint and Supervisord  
ADD core/supervisord.conf /etc/supervisord.conf  
ADD core/docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod 755 /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
CMD ["/docker-entrypoint.sh"]  

