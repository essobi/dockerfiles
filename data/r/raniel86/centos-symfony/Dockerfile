FROM centos:latest  
  
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm  
RUN yum install -y php56u php56u-xml php56u-pdo php56u-devel php56u-mysqlnd
php56u-opcache php56u-cli php56u-common php56u-pgsql php56u-gd php56u-mbstring
php56u-soap php56u-process php56u-pear php56u-mcrypt php56u-fpm php56u-pecl-
memcache php56u-pecl-jsonc php56u-pecl-jsonc-devel php56u-pecl-apcu nodejs npm
ant wget ansible mysql mysql-server  
RUN sed -ie 's/;date\\.timezone =/date\\.timezone = Europe\/Rome/g'
/etc/php.ini  
  
# composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  

