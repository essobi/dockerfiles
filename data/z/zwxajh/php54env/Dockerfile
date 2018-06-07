#  
# VERSION 1.0  
#  
# use the official build of CentOS  
FROM centos:6  
MAINTAINER zhang wei, zwxajh@gmail.com  
  
# update  
RUN yum install -y yum-plugin-fastestmirror dnsmasq vi wget glibc-common nc
mcrypt  
RUN echo 'include_only=.jp' >> /etc/yum/pluginconf.d/fastestmirror.conf  
RUN yum update -y  
  
# setup remi repository  
RUN curl -O http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN curl -O http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
RUN curl -O http://rpms.famillecollet.com/RPM-GPG-KEY-remi; rpm --import RPM-
GPG-KEY-remi  
RUN rpm -Uvh remi-release-6*.rpm epel-release-6*.rpm  
  
# mysql and ssh httpd php  
RUN yum install -y --enablerepo=epel,remi mysql mysql-devel openssh httpd php
php-mysql php-gd php-pdo php-pear php-mbstring php-devel php-xml libmcrypt
libmcrypt-devel php-pecl-xdebug php-pecl-memcached memcached php-mcrypt  
  
ENV LANG ja_JP.UTF-8  
ADD adds/configure.sh /configure.sh  
RUN chmod 755 /configure.sh  
RUN /configure.sh  
  
# private expose  
EXPOSE 80  
ADD adds/start.sh /start.sh  
RUN chmod 755 /start.sh  
ENTRYPOINT ["/start.sh"]  

