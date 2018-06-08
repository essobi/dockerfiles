FROM centos:6.9  
MAINTAINER furuyamah <furuyamah@isao.co.jp>  
  
RUN yum update -y && \  
yum install -y epel-release && \  
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm && \  
yum install -y --enablerepo=remi mysql compat-mysql51 && \  
yum install -y gcc ImageMagick-devel curl-devel fuse git syslog crontabs wget
&& \  
yum install -y \  
httpd \  
httpd-devel \  
httpd-tools \  
php \  
php-cli \  
php-common \  
php-dba \  
php-devel \  
php-gd \  
php-mbstring \  
php-mcrypt \  
php-mysql \  
php-pdo \  
php-pear \  
php-pecl-apc \  
php-pecl-memcache \  
php-xml \  
php-xmlrpc && \  
pecl clear-cache && \  
printf "\n" | pecl install imagick-3.1.2 && \  
printf "\n" | pecl install pecl_http-1.7.6  
  
# for mount S3  
RUN mkdir -p /root/go/bin && \  
wget https://github.com/kahing/goofys/releases/download/v0.0.13/goofys -O
/root/go/bin/goofys && \  
chmod a+x /root/go/bin/goofys && \  
mkdir /root/.aws  
WORKDIR /var/www  

