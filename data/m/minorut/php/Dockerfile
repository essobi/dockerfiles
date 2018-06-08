FROM minorut/centos:6.8  
MAINTAINER minorut <taguchi@buddying.jp>  
  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm \  
&& rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm \  
&& yum update -y \  
&& yum install -y httpd \  
&& yum install -y --enablerepo=remi-php55 \  
php \  
php-devel \  
php-dom \  
php-gd \  
php-intl \  
php-mbstring \  
php-mcrypt \  
php-mysqlnd \  
php-pdo \  
php-pecl-xdebug \  
php-pecl-apcu \  
php-posix \  
php-simplexml \  
php-soap \  
php-xml \  
php-xmlwriter \  
php-xsl \  
&& yum install -y postfix \  
&& rm -rf /var/tmp/* /var/lib/yum/* /var/cache/yum/* \  
&& yum clean all  
  
# Settings  
COPY ./setup/httpd_development.conf /etc/httpd/conf.d/  
COPY ./setup/php_development.ini /etc/php.d/  
COPY ./setup/entrypoint.sh /  
# Directory, permission, ...  
RUN rm -rf /var/www/* \  
&& mkdir /var/www/html \  
&& mkdir /var/log/php \  
&& chmod 777 -R /var/log/php \  
&& chmod 777 -R /var/lib/php/session \  
&& usermod -u 1000 apache \  
&& groupmod -g 1000 apache \  
&& sed -i.dist 's,^#ServerName.*$,ServerName 127.0.0.1:80,g'
/etc/httpd/conf/httpd.conf \  
&& chmod 700 /entrypoint.sh  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Environment  
ENV HOME=/root LANG=ja_JP.utf-8  
WORKDIR /var/www  
  
# Listen  
EXPOSE 80  
  
ENTRYPOINT /entrypoint.sh  

