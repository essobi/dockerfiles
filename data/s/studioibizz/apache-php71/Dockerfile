FROM centos:centos7  
RUN yum update -y && yum install httpd httpd-tools -y  
  
RUN yum install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm -y  
RUN yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm -y  
  
RUN yum install yum-utils -y  
RUN yum install mc -y  
  
# Changed the current timezone to Europe/Amsterdam  
RUN rm -f /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime  
  
RUN yum-config-manager --enable remi-php71 -y  
  
# install php7  
# breaking it down to see where dockerhub dies.  
RUN \  
yum -y install \  
php php-common \  
php-mbstring \  
php-mcrypt \  
php-pear \  
php-devel \  
php-xml \  
php-mysqlnd \  
php-pdo \  
php-opcache --nogpgcheck \  
php-bcmath \  
php-soap \  
php-gd \  
php-xdebug  
  
# php-fpm  
RUN yum -y install php-fpm  
  
# SSL  
RUN yum -y install mod_ssl \  
openssl  
  
# Zip  
RUN yum -y install zip \  
unzip \  
php-zip  
  
# Copied custom configuration for alias  
COPY conf/vhost.conf /etc/httpd/conf.d/wingzz-vhost.conf  
COPY ini/50-xdebug.ini /etc/php.d/50-xdebug.ini  
  
# Install the latest version of CVS  
COPY repo/mercurial.selenic.com.repo
/etc/yum.repos.d/mercurial.selenic.com.repo  
RUN yum -y install \  
mercurial \  
git  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install Pipeline utilities  
RUN pear install PHP_CodeSniffer  
  
# Install JSHint for checking javascripts  
RUN yum -y install nodejs  
RUN npm install -g jshint  
  
EXPOSE 80 443  
# Copied script file to run every time  
COPY scripts/start.sh /root/scripts/start.sh  
RUN ["chmod", "+x", "/root/scripts/start.sh"]  
  
CMD ["/root/scripts/start.sh"]  

