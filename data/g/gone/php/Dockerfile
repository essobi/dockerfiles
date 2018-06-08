FROM gone/base:latest  
RUN sh -c 'echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu
$(lsb_release -sc) main" > /etc/apt/sources.list.d/nginx-stable.list' && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \  
add-apt-repository -y ppa:ondrej/php && \  
apt-get -qq update && \  
apt-get -yq install --no-install-recommends \  
apache2 \  
libapache2-mod-php7.1 \  
php7.1 \  
php-xdebug\  
php7.1-fpm \  
php7.1-mysql \  
php7.1-curl \  
php-apcu \  
php7.1-gd \  
php7.1-intl \  
php7.1-imap \  
php7.1-cli \  
php7.1-mcrypt \  
php7.1-soap \  
php7.1-sqlite \  
php7.1-opcache \  
php7.1-ldap \  
php7.1-mbstring \  
php7.1-json \  
php7.1-xml \  
php7.1-zip \  
php7.1-bcmath \  
php7.1-pspell \  
mysql-client \  
curl \  
inetutils-ping \  
host \  
&& \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
\  
sed -i "s/upload_max_filesize.*/upload_max_filesize = 1024M/g"
/etc/php/7.1/apache2/php.ini && \  
sed -i "s/post_max_size.*/post_max_size = 1024M/g"
/etc/php/7.1/apache2/php.ini && \  
sed -i "s/max_execution_time.*/max_execution_time = 0/g"
/etc/php/7.1/apache2/php.ini && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php/7.1/apache2/php.ini && \  
sed -i "s/error_reporting.*/error_reporting = E_ALL \& \~E_DEPRECATED \&
\~E_STRICT \& \~E_CORE_WARNING/g" /etc/php/7.1/apache2/php.ini && \  
cp /etc/php/7.1/apache2/php.ini /etc/php/7.1/cli/php.ini && \  
sed -i "s/ServerSignature On/ServerSignature Off/g" /etc/apache2/conf-
enabled/security.conf && \  
sed -i "s/ServerTokens OS/ServerTokens Prod/g" /etc/apache2/conf-
enabled/security.conf  
  
# Expose ports.  
EXPOSE 80  
  
COPY . /app  
RUN rm -fr /var/www/html && \  
ln -s /app /var/www/html && \  
mv ApacheConfig.conf /etc/apache2/sites-enabled/000-default.conf && \  
mv envvars /etc/apache2/ && \  
mv apache2.conf /etc/apache2/ && \  
mkdir /etc/service/apache && \  
mkdir /etc/service/show_logs && \  
mv run.apache.sh /etc/service/apache/run && \  
mv run.show_logs.sh /etc/service/show_logs/run && \  
chmod +x /etc/service/*/run && \  
rm /app/* && \  
a2enmod rewrite  
  
# On build, add anything in with Dockerfile into /app  
ONBUILD ADD ./ /app  
  
# If composer.json/composer.lock exist, do a composer install.  
ONBUILD RUN composer install --ignore-platform-reqs; exit 0  
ONBUILD RUN composer dumpautoload -o; exit 0

