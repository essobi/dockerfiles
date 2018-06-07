FROM centos:6  
MAINTAINER AKIRA MURATA <a.murata@sekaie.co.jp>  
  
#config  
ENV code_root /var/www/html  
ENV httpd_conf ${code_root}/httpd/httpd.conf  
  
#install tools  
RUN yum install -y -R 5 vim  
  
#install httpd php  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
RUN yum install -y -R 5 httpd  
RUN yum install --enablerepo=epel,remi-php56,remi -y -R 5 \  
php \  
php-cli \  
php-gd \  
php-mbstring \  
php-mcrypt \  
php-mysqlnd \  
php-pdo \  
php-xml \  
php-xdebug  
RUN sed -i -e "s|^;date.timezone =.*$|date.timezone = Asia/Tokyo|"
/etc/php.ini  
ADD . $code_root  
RUN test -e $httpd_conf && echo "Include $httpd_conf" >>
/etc/httpd/conf/httpd.conf  
  
#install mysql  
RUN yum install -y mysql mysql-devel mysql-server mysql-utilities  
  
#install git  
RUN yum install -y -R 5 git  
  
#install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#port open 80  
EXPOSE 80

