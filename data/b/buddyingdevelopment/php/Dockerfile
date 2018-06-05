FROM buddyingdevelopment/centos:6.8  
MAINTAINER buddyingdevelopment <development@buddying.jp>  
  
RUN curl https://repos.fedorapeople.org/repos/jkaluza/httpd24/epel-
httpd24.repo --output /etc/yum.repos.d/epel-httpd24.repo  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
RUN yum update -y  
RUN yum install -y httpd24  
RUN yum install -y --enablerepo=remi-php56 \  
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
RUN yum install -y postfix  
RUN yum install -y zip unzip  
RUN rm -rf /var/tmp/* /var/lib/yum/* /var/cache/yum/*  
RUN yum clean all  
  
# Settings  
COPY ./setup/httpd_development.conf /opt/rh/httpd24/root/etc/httpd/conf.d/  
COPY ./setup/php_development.ini /etc/php.d/  
COPY ./setup/entrypoint.sh /  
  
# Directory, permission, ...  
RUN rm -rf /var/www/*  
RUN mkdir /var/www/html  
RUN mkdir /var/log/php  
RUN chmod 777 -R /var/log/php  
RUN chmod 777 -R /var/lib/php/session  
RUN usermod -u 1000 apache  
RUN groupmod -g 1000 apache  
RUN sed -i.dist 's,^#ServerName.*$,ServerName 127.0.0.1:80,g'
/opt/rh/httpd24/root/etc/httpd/conf/httpd.conf  
RUN sed -i.dist 's/^inet_interfaces = localhost$/inet_interfaces = all/g'
/etc/postfix/main.cf  
RUN chmod 700 /entrypoint.sh  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Environment  
ENV HOME=/root LANG=ja_JP.utf-8  
WORKDIR /var/www  
  
# Listen  
EXPOSE 80  
ENTRYPOINT /entrypoint.sh  

