FROM ubuntu:xenial  
  
ENV OS_LOCALE="en_US.UTF-8"  
RUN apt-get update && apt-get install -y locales && locale-gen ${OS_LOCALE}  
ENV LANG=${OS_LOCALE} \  
LANGUAGE=en_US:en  
  
ENV APACHE_CONF_DIR=/etc/apache2 \  
PHP_CONF_DIR=/etc/php/7.1 \  
PHP_DATA_DIR=/var/lib/php  
  
RUN \  
buildDeps='software-properties-common python-software-properties' \  
&& apt-get install --no-install-recommends -y $buildDeps \  
&& add-apt-repository -y ppa:ondrej/php \  
&& add-apt-repository -y ppa:ondrej/apache2 \  
&& apt-get update \  
&& apt-get install -y curl apache2 libapache2-mod-php7.1 php7.1-common
php7.1-cli php7.1-readline php7.1-mbstring php7.1-zip php7.1-intl php7.1-xml
php7.1-json php7.1-curl php7.1-mcrypt php7.1-gd php7.1-pgsql php7.1-mysql
php7.1-sqlite php-pear \  
# Apache settings  
&& cp /dev/null ${APACHE_CONF_DIR}/conf-available/other-vhosts-access-log.conf
\  
&& rm ${APACHE_CONF_DIR}/sites-enabled/000-default.conf
${APACHE_CONF_DIR}/sites-available/000-default.conf \  
&& a2enmod proxy_http rewrite headers php7.1 \  
# PHP settings  
&& phpenmod mcrypt \  
# Install composer  
&& curl -sS https://getcomposer.org/installer | php -- --version=1.4.1
\--install-dir=/usr/local/bin --filename=composer \  
# Cleaning  
&& apt-get purge -y \--auto-remove $buildDeps locales \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
# Forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/apache2/access.log \  
&& ln -sf /dev/stderr /var/log/apache2/error.log \  
&& chown www-data:www-data ${PHP_DATA_DIR} -Rf  
  
RUN mkdir /var/www/app  
WORKDIR /var/www/app  

