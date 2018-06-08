# docker-gitlab-ci-runner-php (PHP 5.4)  
FROM centos:latest  
MAINTAINER Leo "leo.on.the.earth@gmail.com"  
# Install epel repo & remi repo & PHP 5.4 & composer  
RUN cd /tmp && \  
curl -O https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
&& \  
curl -O http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \  
rpm -Uvh remi-release-7*.rpm epel-release-latest-7*.rpm && \  
yum -y update && \  
yum --enablerepo=remi install -y \  
which \  
git \  
php \  
php-bcmath \  
php-cli \  
php-common \  
php-dba \  
php-devel \  
php-embedded \  
php-enchant \  
php-fpm \  
php-gd \  
php-gmp \  
php-imap \  
php-interbase \  
php-intl \  
php-ldap \  
php-litespeed \  
php-mbstring \  
php-mcrypt \  
php-mssql \  
php-mysqlnd \  
php-odbc \  
php-opcache \  
php-pdo \  
php-pear \  
php-pgsql \  
php-process \  
php-pspell \  
php-recode \  
php-snmp \  
php-soap \  
php-tidy \  
php-xml \  
php-xmlrpc \  
php-pecl-xdebug && \  
mkdir /root/.composer && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
echo 'date.timezone="UTC"' > /etc/php.d/docker-gitlab-ci-runner-php.ini  
  
VOLUME ["/root/.composer"]  

