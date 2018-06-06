# This Dockerfile deletes a number of unit files which might cause issues.  
# From here, you are ready to build your base image.  
FROM centos:7  
ENV container docker  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
CMD ["/usr/sbin/init"]  
  
# Apache2  
RUN yum -y install httpd; yum clean all; systemctl enable httpd.service  
EXPOSE 80  
# CentOS  
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
  
# Install FreeTDS (Database Driver)  
WORKDIR /freetds  
RUN yum install -y gcc \  
&& yum install -y re2c  
RUN wget ftp://ftp.freetds.org/pub/freetds/stable/freetds-patched.tar.gz  
RUN tar -xzvf freetds-patched.tar.gz  
  
# Start APACHE SEVER  
ENTRYPOINT ["/usr/sbin/init"]  
CMD ["/usr/sbin/init"]  

