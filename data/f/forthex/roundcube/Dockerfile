FROM centos:7  
MAINTAINER Anatoliy Kartashov  
  
RUN yum -y install epel-release && \  
yum -y install php \  
php-cli \  
php-common \  
php-pdo \  
php-mysqlnd \  
mariadb \  
php-gd \  
php-xml \  
php-mbstring \  
httpd  
  
ADD
https://github.com/roundcube/roundcubemail/releases/download/1.3.1/roundcubemail-1.3.1-complete.tar.gz
/tmp  
RUN cd /tmp && tar -xzvf roundcubemail-1.3.1-complete.tar.gz  
  
RUN mv /tmp/roundcubemail-1.3.1/* /var/www/html  
RUN mv /tmp/roundcubemail-1.3.1/.[!.]* /var/www/html && \  
rm -rf /tmp/roundcubemail-1.3.1  
  
### remove installer for security perposes  
RUN rm -rf /var/www/html/installer  
  
### setup log to stdout  
RUN ln -s /dev/stderr /var/log/httpd/error_log  
RUN ln -s /dev/stdout /var/log/httpd/access_log  
RUN ln -s /dev/stderr /var/www/html/logs/errors  
  
ADD ./start.sh /root/start.sh  
  
EXPOSE 80  
CMD ["/root/start.sh"]  

