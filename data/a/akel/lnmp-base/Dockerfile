FROM centos:7  
MAINTAINER Akel <akel@akelmaister.com>  
  
ENV container docker  
  
RUN yum -y update; yum clean all  
RUN yum -y install systemd; yum clean all; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
## install base-packages  
RUN yum -y install epel-release  
RUN yum -y install nginx php-fpm php-devel gcc libtool php-mysql wget git nano
mariadb-server mariadb  
  
## Get latest Phalcon sources  
RUN cd /usr/local/src/ && git clone --depth=1
git://github.com/phalcon/cphalcon.git  
  
## Build Phalcon2 module  
RUN cd /usr/local/src/cphalcon/build && /bin/sh install  
  
## Add Phalcon module to php (need to connect after mysql extension)  
RUN echo "extension=phalcon.so" >> /etc/php.d/pdo_mysql.ini  
  
EXPOSE 22 80  
CMD [“/usr/sbin/init”]  

