#  
# Rocketgraph jenkins for php  
#  
# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER Konstantinos Christofilos <kostas.christofilos@rocketgraph.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install base.  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y curl git htop vim wget openjdk-7-jdk  
  
# Install PHP 7  
# Download source and signature  
RUN curl -SL "http://php.net/get/php-7.0.7.tar.gz/from/this/mirror" -o
php7.tar.gz  
RUN curl -SL "http://php.net/get/php-7.0.7.tar.gz.asc/from/this/mirror" -o
php7.tar.gz.asc  
  
# Verify file  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
"1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763"  
RUN gpg --verify php7.tar.gz.asc php7.tar.gz  
  
# Install tools for compile  
RUN apt-get install -y build-essential libxml2-dev libcurl4-gnutls-dev libpng-
dev libmcrypt-dev libxslt-dev libicu-dev libssl-dev libbz2-dev libjpeg-dev
autoconf  
  
# Uncompress  
RUN tar zxvf php7.tar.gz  
  
ENV PHP_VERSION 7.0.7  
ENV PHP_CLI_INI_DIR /etc/php7/cli  
  
RUN mkdir -p $PHP_CLI_INI_DIR/conf.d  
  
#php7-cli  
RUN cd php-7.0.7 && \  
./configure \  
\--with-config-file-path="$PHP_CLI_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_CLI_INI_DIR/conf.d" \  
\--with-libdir=/lib/x86_64-linux-gnu \  
\--enable-mysqlnd \  
\--enable-intl \  
\--enable-mbstring \  
\--enable-zip \  
\--enable-exif \  
\--enable-pcntl \  
\--enable-bcmath \  
\--enable-ftp \  
\--enable-exif \  
\--enable-calendar \  
\--enable-sysvmsg \  
\--enable-sysvsem \  
\--enable-sysvshm \  
\--enable-wddx \  
\--enable-gd-native-ttf \  
\--enable-gd-jis-conv \  
\--enable-sockets \  
\--enable-opcache \  
\--enable-sysvsem \  
\--enable-sysvshm \  
\--with-curl \  
\--with-mysqli=mysqlnd \  
\--with-pdo-mysql=mysqlnd \  
\--with-openssl \  
\--with-xsl \  
\--with-gd \  
\--with-mcrypt \  
\--with-iconv \  
\--with-bz2 \  
\--with-mhash \  
\--with-jpeg-dir=/usr \  
\--with-png-dir=/usr \  
\--with-zlib && \  
make -j"$(nproc)" && \  
make install && \  
make clean  
  
# Install APCu  
RUN curl -SL "https://pecl.php.net/get/apcu-5.1.4.tgz" -o apcu.tgz  
RUN tar zxvf apcu.tgz  
  
RUN cd apcu-5.1.4 && \  
phpize && \  
./configure && \  
make && \  
cp modules/apcu.so /usr/local/lib/php/extensions/no-debug-non-zts-20151012  
  
# Clear files  
RUN rm -rf php*  
RUN rm -rf apcu*  
  
# Create session folder  
RUN mkdir -p /var/lib/php7/sessions  
RUN chown www-data:root /var/lib/php7/sessions  
  
ADD ./php_cli.ini /etc/php7/cli/php.ini  
ADD ./browscap.ini /etc/php7/browscap.ini  
  
# Install latest phpunit  
RUN wget -q https://phar.phpunit.de/phpunit.phar ; chmod +x phpunit.phar ; mv
phpunit.phar /usr/bin/phpunit  
  
# Install PHPLOC  
RUN wget -q https://phar.phpunit.de/phploc.phar ; chmod +x phploc.phar ; mv
phploc.phar /usr/local/bin/phploc  
  
# Install PHP Depend  
RUN wget -q http://static.pdepend.org/php/latest/pdepend.phar ; chmod +x
pdepend.phar ; mv pdepend.phar /usr/local/bin/pdepend  
  
# Install PHP_CodeSniffer  
RUN wget -q https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar ; chmod +x
phpcs.phar ; mv phpcs.phar /usr/local/bin/phpcs  
RUN wget -q https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar ; chmod +x
phpcbf.phar ; mv phpcbf.phar /usr/local/bin/phpcbf  
  
# Instal PHP Copy/Paste Detector (PHPCPD)  
RUN wget -q https://phar.phpunit.de/phpcpd.phar ; chmod +x phpcpd.phar ; mv
phpcpd.phar /usr/local/bin/phpcpd  
  
# Install phpdoc  
RUN wget -q http://www.phpdoc.org/phpDocumentor.phar ; chmod +x
phpDocumentor.phar ; mv phpDocumentor.phar /usr/bin/phpdoc  
  
# Install Jenkins  
RUN \  
wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key
add - && \  
sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ >
/etc/apt/sources.list.d/jenkins.list' && \  
sudo apt-get update && \  
sudo apt-get install -y jenkins  
  
RUN mkdir -p /var/jenkins_home  
  
ENV JENKINS_HOME=/var/jenkins_home  
  
#Install Node.js and npm  
RUN apt-get install -y node npm  
RUN mv /usr/sbin/node /usr/sbin/node.BACKUP  
RUN ln -s /usr/bin/nodejs /usr/sbin/node  
  
#Install Gulp  
RUN npm install -g gulp  
  
# Define mountable directories.  
VOLUME ["/var/jenkins_home"]  
  
EXPOSE 8080  
CMD ["java", "-jar", "/usr/share/jenkins/jenkins.war"]  

