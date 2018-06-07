FROM centos:7  
MAINTAINER patrick henry <docker@patrickhenry.co.uk>  
  
# Update repo for php 5.6  
#RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/epel-release.rpm  
RUN yum -y install wget  
RUN yum -y install git  
  
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
  
RUN wget http://rpms.remirepo.net/enterprise/remi-release-7.rpm  
  
RUN rpm -Uvh remi-release-7.rpm  
  
RUN yum-config-manager --enable remi-php70  
RUN yum -y install unzip  
RUN yum -y install php  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
#install  
WORKDIR /var/www/html/  

