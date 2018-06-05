FROM centos:6.6  
MAINTAINER go_chiba <go.chiba@gmail.com>  
  
RUN yum update -y  
  
RUN yum install -y \  
httpd \  
mysql  
  
RUN rpm -ivh \  
http://ftp.jaist.ac.jp/pub/Linux/Fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm \  
http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
  
RUN yum install -y --enablerepo=remi,remi-php56 \  
php \  
php-common \  
php-mbstring \  
php-mysql \  
php-pdo \  
php-cli \  
php-xml  
  
COPY composer.json .  
RUN curl -sS https://getcomposer.org/installer | php  
RUN ./composer.phar install  
ENV PATH $PATH:/vendor/bin  
  
COPY httpd.conf /etc/httpd/conf/httpd.conf  
COPY ./html /var/www/html  
COPY ./my.cnf.client /etc/my.cnf  
  
EXPOSE 80  
CMD ["httpd", "-D", "FOREGROUND"]  

