FROM centos:7  
MAINTAINER SeymourLabs Ltd <info@seymourlabs.co.uk>  
  
# add repo  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm  
  
# update cache  
RUN yum clean all && yum makecache  
  
# php and relevant requirements  
RUN yum -y update && yum -y install \  
python \  
python-pip \  
zip \  
git \  
php71u-fpm \  
php71u-common \  
php71u-json \  
php71u-iconv \  
php71u-mcrypt \  
php71u-curl \  
php71u-pdo \  
php71u-pdo_mysql \  
php71u-mbstring \  
php71u-xml \  
php71u-gd \  
php71u-cli \  
wget  
  
# install nodejs  
RUN yum -y install nodejs  
  
# install php-phalcon  
RUN rpm -ivh
https://packagecloud.io/phalcon/stable/packages/el/7/php71u-phalcon-3.1.2-1.ius.el7.centos.x86_64.rpm/download.rpm  

