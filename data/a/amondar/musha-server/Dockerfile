FROM centos:7  
MAINTAINER Amondar  
  
# Update the base system with latest patches  
# and latest epel release NO NEED add epel repos!!!  
RUN yum -y update && yum clean all  
RUN yum install -y epel-release  
  
# Install Main Programs  
RUN yum install -y \  
nginx \  
mysql \  
curl \  
supervisor \  
cronie \  
npm  
  
# add repo for new php version  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
  
# доступные модули  
# php56w-bcmath php56w-cli php56w-common php56w-dba php56w-devel php56w-gd  
# php56w-mbstring php56w-mcrypt php56w-mysql php56w-pdo php56w-pear
php56w-pecl-apcu  
# php56w-soap php56w-tidy php56w-xml php56w-xmlrpc  
RUN yum install -y \  
php56w \  
php56w-fpm \  
php56w-opcache \  
php56w-cli \  
php56w-common \  
php56w-mbstring \  
php56w-mcrypt \  
php56w-mysql \  
php56w-gd \  
php56w-pdo \  
php56w-soap \  
php56w-xml \  
php56w-xmlrpc  
  
# Set local IP  
RUN yum install -y iproute  
  
ENV TERM dumb  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN npm install --global gulp  
  
EXPOSE 80

