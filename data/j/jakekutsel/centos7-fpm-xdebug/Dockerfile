FROM centos:7  
MAINTAINER Jake Kutsel <e.kutel@invento.by>  
  
ENV container=docker  
  
RUN yum -y update  
  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum -y install gcc-c++ pcre-devel zlib-devel make unzip  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
  
RUN yum -y install --enablerepo=webtatic php70w php70w-common php70w-fpm
php70w-cli php70w-opcache php70w-pear php70w-devel php70w-intl php70w-mbstring
php70w-mcrypt php70w-pdo php70w-mssql php70w-soap  
  
RUN sed -i '/^listen/c \  
listen = 0.0.0.0:9000' /etc/php-fpm.d/www.conf  
  
RUN sed -i 's/^listen.allowed_clients/;listen.allowed_clients/' /etc/php-
fpm.d/www.conf  
  
RUN mkdir -p /srv/http && \  
echo "<?php phpinfo(); ?>" > /srv/http/index.php && \  
chown -R apache:apache /srv/http  
  
RUN rm -r /usr/share/file/magic  
RUN mkdir -p /usr/share/file/magic  
EXPOSE 9000  
VOLUME /srv/http  
  
ENTRYPOINT ["php-fpm","-F"]  
  

