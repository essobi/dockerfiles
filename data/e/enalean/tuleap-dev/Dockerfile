FROM centos:7  
  
COPY Tuleap.repo /etc/yum.repos.d/  
  
RUN yum install -y epel-release centos-release-scl vim && \  
yum install --enablerepo=TuleapC7 -y \  
nginx \  
rh-php56-php-gd \  
rh-php56-php-pecl \  
rh-php56-php-pear \  
rh-php56-php-soap \  
rh-php56-php-mysqlnd \  
rh-php56-php-xml \  
rh-php56-php-mbstring \  
rh-php56-php-cli \  
rh-php56-php-opcache \  
rh-php56-php-process \  
rh-php56-php-pdo \  
rh-php56-php-fpm \  
rh-php56-php-ldap \  
rh-php56-php-intl \  
rh-php56-php-bcmath php-amqplib-amqplib \  
rh-php56-php-pecl-xdebug \  
php-ZendFramework2-Loader \  
php-zendframework \  
php-paragonie-random-compat \  
htmlpurifier \  
viewvc MySQL-python python-ldap viewvc-theme-tuleap \  
httpd mod_dav_svn logrotate sha1collisiondetector \  
mod_perl perl-DBI perl-LDAP perl-DBD-MySQL 'perl(Crypt::Eksblowfish::Bcrypt)'
\  
supervisor; \  
yum clean all  

