FROM centos:6.8  
ARG BUILD_ENV=live  
ENV BUILD_ENV ${BUILD_ENV}  
  
# Update & Upgrade  
USER root  
RUN yum update -y \  
&& yum upgrade -y  
  
RUN echo "ENVIRONMENT::$BUILD_ENV"  
RUN if [ "${BUILD_ENV}" = "dev" ]; then echo "${BUILD_ENV}"; fi  
  
# Add Repos - EPEL, Remi  
USER root  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
RUN yum repolist  
RUN yum update -y  
  
# Install "PHP Extentions", "libraries", "Software's"  
USER root  
RUN yum --enablerepo remi-php55,remi,epel install -y \  
php \  
php-bcmath \  
php-cli \  
php-common \  
php-dba \  
php-devel \  
php-enchant \  
php-fpdf \  
php-fpm \  
php-gd \  
php-gmp \  
php-imap \  
php-intl \  
php-ldap \  
php-mbstring \  
php-mcrypt \  
php-mysqlnd \  
php-oauth \  
php-opcache \  
php-pdo \  
php-pear \  
php-pgsql \  
php-process \  
php-pspell \  
php55-runtime \  
php-soap \  
php-tidy \  
php-xml \  
php-xmlrpc \  
php-pecl-amqp \  
php-pecl-igbinary \  
php-pecl-imagick \  
php-pecl-jsonc \  
php-pecl-jsonc-devel \  
php-pecl-memcache \  
php-pecl-mongo \  
php-pecl-oauth \  
php-pecl-pdflib \  
php-pecl-redis \  
php-pecl-runkit \  
php-pecl-ssh2 \  
php-pecl-zip  
  
# Install dev stuff  
RUN if [ ${BUILD_ENV} = 'dev' ]; then \  
yum --enablerepo remi-php55,remi,epel install -y \  
php-pecl-xdebug \  
;fi  
  
# Clean up  
USER root  
RUN yum clean all -y \  
&& rm -rf \  
/tmp/* \  
/var/tmp/*  
  
COPY docker-php-entrypoint /usr/local/bin/  
  
ENTRYPOINT ["docker-php-entrypoint"]  
  
WORKDIR /var/www/html  
  
RUN sed -i 's/daemonize = yes/daemonize = no/' /etc/php-fpm.conf \  
&& sed -i 's/listen.allowed_clients = 127.0.0.1/;listen.allowed_clients =
127.0.0.1/' /etc/php-fpm.d/www.conf \  
&& sed -i 's/listen = 127.0.0.1:9000/listen = [::]:9000/' /etc/php-
fpm.d/www.conf \  
&& sed -i 's/;catch_workers_output = yes/catch_workers_output = yes/'
/etc/php-fpm.d/www.conf \  
&& sed -i 's/error_log = \/var\/log\/php-fpm\/error.log/error_log =
\/dev\/stderr/' /etc/php-fpm.conf \  
&& sed -i 's/php_admin_value\\[error_log\\] = \/var\/log\/php-fpm\/www-
error.log/php_admin_value[error_log] = \/dev\/stderr/' /etc/php-fpm.d/www.conf
\  
&& { \  
echo '[www]'; \  
echo 'access.log = /dev/stdout'; \  
echo 'clear_env = no'; \  
} | tee /etc/php-fpm.d/docker.conf  
  
EXPOSE 9000  
CMD ["php-fpm", "-F"]  

