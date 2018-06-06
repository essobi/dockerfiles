FROM centos:7  
ENV NODE_VERSION 8.11.2  
ENV PHP_VERSION 72  
ADD .docker/nginx.repo /etc/yum.repos.d/nginx.repo  
  
RUN yum -y update && yum -y install epel-release && \  
rpm -ivh http://rpms.remirepo.net/enterprise/remi-release-7.rpm  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
RUN yum -y update && yum -y install \  
bzip2 \  
git \  
nginx \  
nginx-module-geoip \  
php$PHP_VERSION php$PHP_VERSION-php \  
php$PHP_VERSION-php-bcmath \  
php$PHP_VERSION-php-cli \  
php$PHP_VERSION-php-common \  
php$PHP_VERSION-php-fpm \  
php$PHP_VERSION-php-gd \  
php$PHP_VERSION-php-imap \  
php$PHP_VERSION-php-iconv \  
php$PHP_VERSION-php-ioncube-loader \  
php$PHP_VERSION-php-json \  
php$PHP_VERSION-php-mysql \  
php$PHP_VERSION-php-mbstring \  
php$PHP_VERSION-php-mcrypt \  
php$PHP_VERSION-php-opcache \  
php$PHP_VERSION-php-pdo \  
php$PHP_VERSION-php-pecl-geoip \  
php$PHP_VERSION-php-pecl-redis \  
php$PHP_VERSION-php-pecl-zip \  
php$PHP_VERSION-php-imagick \  
php$PHP_VERSION-php-soap \  
php$PHP_VERSION-php-xml \  
php$PHP_VERSION-php-xmlrpc \  
python-setuptools && \  
yum clean all  
  
RUN easy_install supervisor  
  
RUN ln -s /opt/remi/php$PHP_VERSION/root/usr/bin/php /usr/bin && \  
ln -s /opt/remi/php$PHP_VERSION/root/usr/sbin/php-fpm /usr/sbin && \  
ln -s /etc/opt/remi/php$PHP_VERSION/php.ini /etc/php.ini  
  
ADD .docker/start.sh /start.sh  
ADD .docker/nginx.conf /etc/nginx/nginx.conf  
ADD .docker/supervisord.conf /etc/supervisord.conf  
ADD .docker/php-fpm.conf /etc/opt/remi/php$PHP_VERSION/php-fpm.conf  
  
RUN chmod 755 /start.sh  
  
CMD ["/bin/bash", "/start.sh"]  

