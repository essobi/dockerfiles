FROM library/centos:centos6  
  
MAINTAINER pica9  
  
# add additional repos  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
RUN curl -sL https://rpm.nodesource.com/setup_8.x | bash -  
  
# install apache, php5  
RUN yum install -y --enablerepo=remi --enablerepo=remi-php71 \  
httpd \  
gcc \  
php \  
php-common \  
php-bcmath \  
php-cli \  
php-pear \  
php-pdo \  
php-pgsql \  
php-gd \  
php-mbstring \  
php-mcrypt \  
php-xml \  
php-devel \  
php-soap \  
php-intl \  
php-redis \  
php-zip \  
zlib-devel \  
curl \  
libcurl-devel \  
git \  
java-1.7.0-openjdk \  
nodejs \  
mod_ssl \  
tar \  
libssh2 \  
libssh2-devel \  
make \  
wget \  
unzip  
  
RUN mkdir -p /etc/httpd/ssl  
  
#install ssh2  
RUN wget http://pecl.php.net/get/ssh2-1.1.1.tgz  
RUN tar -zxf ssh2-1.1.1.tgz  
RUN cd ssh2-1.1.1 && phpize && ./configure && make && make install  
RUN echo "extension=ssh2.so" > /etc/php.d/20-ssh2.ini  
  
RUN npm install -g bower  
  
#install composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/bin/composer  

