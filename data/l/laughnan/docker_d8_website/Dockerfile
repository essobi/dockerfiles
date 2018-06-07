FROM centos:7  
# update centos  
RUN yum update -y  
  
# install rpm for php 5.6  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/epel-release.rpm  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
  
# install necessary libraries (includes php, ruby, gems, and git)  
RUN yum install php56w php56w-mbstring php56w-xml php56w-xmlrpc php56w-gd
php56w-pdo git ruby ruby-devel rubygems -y  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer

