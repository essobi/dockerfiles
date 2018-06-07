FROM centos:7  
MAINTAINER Thiago Ramos Fanfoni <thiagofanfoni@gmail.com>  
  
RUN \  
yum install -y epel-release \  
&& yum install -y \  
glibc \  
httpd \  
fping \  
php \  
php-ldap \  
php-mcrypt \  
php-pear \  
php-xml \  
php-ZendFramework-Db-Adapter-Pdo-Mysql.noarch \  
mysql \  
telnet \  
which \  
&& yum clean all  
  
RUN curl -kL
'http://downloads.sourceforge.net/project/phpipam/phpipam-1.2.1.tar?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fphpipam%2F%3Fsource%3Dtyp_redirect&ts=1472768582'
| \  
tar --strip=1 -xC /var/www/html  
  
RUN \  
echo "ServerName phpipam" >> /etc/httpd/conf/httpd.conf \  
&& sed -i \  
-e 's|;date.timezone =|date.timezone = America/Sao_Paulo|' \  
-e 's|max_execution_time = 30|max_execution_time = 1000|' \  
-e 's|max_input_time = 60|max_input_time = 1000|' \  
-e 's|memory_limit = 128M|memory_limit = 256M|' \  
/etc/php.ini \  
&& sed -i \  
-e 's|"logs/error_log"|/proc/self/fd/2|' \  
-e 's|"logs/access_log" combined|/proc/self/fd/1 common|' \  
-e 's|AllowOverride None|AllowOverride all|' \  
/etc/httpd/conf/httpd.conf \  
&& ln -s $(which fping) /bin/fping  
  
EXPOSE 80  
  
WORKDIR /var/www/html  
COPY ./entrypoint.sh /usr/local/bin  
  
ENTRYPOINT [ "entrypoint.sh" ]  
CMD [ "httpd","-D","FOREGROUND" ]  

