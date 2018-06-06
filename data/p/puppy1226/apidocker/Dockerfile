FROM centos:7.0.1406  
MAINTAINER Tais P. Hansen <tph@casalogic.dk>  
  
# CentOS  
RUN yum clean all && yum -y swap fakesystemd systemd  
RUN yum install -y yum-plugin-ovl  
  
# PHP 7.0  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
RUN yum install -y php70w-devel php70w php70w-common php70w-gd php70w-mcrypt \  
php70w-opcache php70w-pdo php70w-xmly php70w-odbc php70w-mbstring php70w-dom
php70w-xdebug php70w-bcmath  
  
# wget  
RUN yum install -y wget  
  
# tar  
RUN yum install -y tar  
  
# git  
RUN yum install -y git  
  
# PHPUnit + Composer  
WORKDIR /tmp  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');" \  
&& composer require "phpunit/phpunit:~5.5.0" \--prefer-source --no-interaction
\  
&& composer require "phpunit/php-invoker" \--prefer-source --no-interaction \  
&& ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit \  
&& sed -i 's/nn and/nn, Julien Breux (Docker) and/g'
/tmp/vendor/phpunit/phpunit/src/Runner/Version.php  
  
# OpenSSL  
RUN yum install -y openssl-devel  
  
# Install Development tools  
RUN yum groupinstall -y "Development tools"  
  
# MongoDB extension for PHP  
WORKDIR /mongo  
RUN wget https://pecl.php.net/get/mongodb-1.1.8.tgz  
RUN tar -xzvf mongodb-1.1.8.tgz  
WORKDIR /mongo/mongodb-1.1.8  
RUN ls  
RUN phpize  
RUN ./configure  
RUN make && make install  
RUN echo "extension=mongodb.so" > /etc/php.d/mongodb.ini  
  
# Finish building all extension back to phpunit  
VOLUME ["/app"]  
WORKDIR /app  
  
ENTRYPOINT ["/usr/local/bin/phpunit"]  
CMD ["--help"]  

