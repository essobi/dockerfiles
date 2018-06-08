FROM centos:7  
MAINTAINER Markus Latzel <markus@palominosys.com>  
  
# Update repo for php 5.6  
#RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/epel-release.rpm  
RUN yum -y -q install wget zip sudo git  
  
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN rpm -ivh epel-release-latest-7.noarch.rpm  
  
RUN wget http://rpms.remirepo.net/enterprise/remi-release-7.rpm  
RUN rpm -Uvh remi-release-7.rpm  
  
RUN yum-config-manager --enable remi-php70  
  
RUN yum -y -q install unzip php php-mcrypt php-memcache php-memcached php-gd
php-pecl php-common php-process php-pecl php-cli php-xml php-mbstring php-pecl
php-pdo php-mysqlnd php-mcrypt php-devel php-pear php-ioncube php-mbstring
php-dom  
  
WORKDIR /root/  
RUN curl -sS https://getcomposer.org/installer | php && chmod a+x
composer.phar && mv composer.phar /usr/local/bin/composer  
  
#install  
RUN mkdir -p /var/www/stage  
COPY httpd.conf /etc/httpd/conf/httpd.conf  
RUN systemctl enable httpd.service  
  
WORKDIR /var/www/stage  
RUN mkdir app web files  
#RUN wget "https://github.com/palominoinc/webpal-app/archive/master.zip" -o
/dev/null  
#RUN unzip master.zip && rm master.zip  
#RUN mv /var/www/stage/webpal-app-master /var/www/stage/app  
# following is redundant if the loaded app has webpal-app submodule, but good
to have in container anyway:  
#RUN git clone https://github.com/palominoinc/webpal-app.git app  
#WORKDIR /var/www/stage/app  
#RUN git submodule init && git submodule update  
#RUN composer update --no-dev --ignore-platform-reqs --prefer-dist  

