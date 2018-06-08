FROM virtuman/nginx-pagespeed:latest  
  
MAINTAINER Alexei Smirnov <alexei@virtuman.com>  
  
  
ENV PHP_VERSION 7.0  
# LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php  
RUN wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
sh -c 'echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list' && \  
apt-get update && \  
packagesPHP7=' \  
php \  
php-bcmath \  
php-bz2 \  
php-cli \  
php-curl \  
php-fpm \  
php-gd \  
php-igbinary \  
php-imagick \  
php-imap \  
php-intl \  
php-mbstring \  
php-mcrypt \  
php-memcache \  
php-memcached \  
php-mongodb \  
php-monolog \  
php-msgpack \  
php-mysql \  
php-pear \  
php-recode \  
php-redis \  
php-xdebug \  
php-xml \  
php-xsl \  
php-zip ' && \  
packagesPHP5=' \  
php5.6 \  
php5.6-bcmath \  
php5.6-fpm \  
php5.6-mysql \  
php5.6-cli \  
php5.6-curl \  
php5.6-gd \  
php-imagick \  
php5.6-imap \  
php5.6-intl \  
php5.6-json \  
php5.6-ldap \  
php5.6-mbstring \  
php5.6-mcrypt \  
php-memcache \  
php-memcached \  
php-mongodb \  
php-msgpack \  
php5.6-mysql \  
php-mysqlnd-ms \  
php5.6-opcache \  
php-redis \  
php-xdebug \  
php5.6-xml \  
php5.6-recode \  
php5.6-soap \  
php5.6-zip ' && \  
[[ $PHP_VERSION == 5.6 ]] && LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
&& INSTALL_PACKAGES=$packagesPHP5 || INSTALL_PACKAGES=$packagesPHP7 && \  
apt-get install -y --no-install-recommends git-core $INSTALL_PACKAGES && \  
apt-get -y --no-install-recommends install \  
exim4 \  
rsync \  
newrelic-php5 && \  
newrelic-install install && \  
# Install Composer  
apt-get autoremove -yqq && \  
apt-get clean autoclean && \  
rm -Rf /tmp/* /var/tmp/* /var/lib/apt/lists/* && \  
mkdir /root/bin/ && \  
echo "export PATH=/root/bin:$PATH" > /root/.bashrc  
  
EXPOSE 443 80  
  
ENV DEFAULT_ADMIN_EMAIL=nobody@example.com \  
DEFAULT_APP_ENV=production \  
DEFAULT_CHOWN_APP_DIR=false \  
DEFAULT_VIRTUAL_HOST=example.com \  
DEFAULT_APP_HOSTNAME=example.com \  
DEFAULT_APP_USER=app \  
DEFAULT_APP_GROUP=app \  
DEFAULT_APP_UID=1000 \  
DEFAULT_APP_GID=1000 \  
DEFAULT_UPLOAD_MAX_SIZE=30M \  
DEFAULT_NGINX_MAX_WORKER_PROCESSES=8 \  
DEFAULT_NGINX_KEEPALIVE_TIMEOUT=30 \  
DEFAULT_PHP_MEMORY_LIMIT=128M \  
DEFAULT_PHP_MAX_EXECUTION_TIME=300 \  
DEFAULT_PHP_MAX_INPUT_VARS=2000 \  
DEFAULT_PHP_PROCESS_MANAGER=dynamic \  
DEFAULT_PHP_MAX_CHILDREN=6 \  
DEFAULT_PHP_START_SERVERS=3 \  
DEFAULT_PHP_MIN_SPARE_SERVERS=2 \  
DEFAULT_PHP_MAX_SPARE_SERVERS=3 \  
DEFAULT_PHP_MAX_REQUESTS=500 \  
DEFAULT_PHP_DISABLE_FUNCTIONS=false \  
DEFAULT_PHP_SHORT_OPEN_TAGS=on \  
DEFAULT_PHP_XDEBUG_REMOTE_HOST=172.17.42.1 \  
DEFAULT_PHP_XDEBUG_REMOTE_PORT=9000 \  
DEFAULT_PHP_XDEBUG_IDE_KEY=default_ide_key \  
DEFAULT_EXIM_DELIVERY_MODE=local \  
DEFAULT_EXIM_MAIL_FROM=example.com \  
DEFAULT_EXIM_SMARTHOST=smtp.example.org::587 \  
DEFAULT_EXIM_SMARTHOST_AUTH_USERNAME=postmaster@example.com \  
DEFAULT_EXIM_SMARTHOST_AUTH_PASSWORD=password_123 \  
DEFAULT_NEWRELIC_ENABLED=true \  
DEFAULT_NEWRELIC_LICENSE=DISABLED  
  
COPY . /app  
  
RUN chmod 750 /app/bin/* && \  
/app/bin/install_composer.sh && \  
/app/bin/init_php.sh  
  
ENTRYPOINT ["/app/bin/boot.sh"]  
  
CMD ["/sbin/my_init"]  

