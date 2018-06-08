FROM repositoryjp/phpbrew-1.21.3:centos-6.6  
MAINTAINER Shinya Kinoshita <skinoshita@repositories.jp>  
  
LABEL name="PHP 5.6.20 Image" \  
description="The image for creating docker container of PHP 5.6.20
Environment." \  
distribution="centos" \  
centos-version="6.6" \  
php-version="5.6.20" \  
vendor="REPOSIORY <http://www.repositories.jp>" \  
license="MIT"  
  
ENV PHP_VERSION 5.6.20  
USER root  
  
# Install PHP 5.6.20  
RUN phpbrew install ${PHP_VERSION} +default +everything -- --with-icu-dir=/usr
--with-gd --with-jpeg-dir=/usr/lib64 --with-png-dir=/usr/png --enable-gd-jis-
conv && \  
sed -e 's/;date.timezone =/date.timezone = UTC/g'
$HOME/.phpbrew/php/php-${PHP_VERSION}/etc/php.ini > /tmp/php.ini && \  
mv -f /tmp/php.ini $HOME/.phpbrew/php/php-${PHP_VERSION}/etc/php.ini && \  
echo "[[ -d ~/.phpbrew/php/php-5.6.20 ]] && phpbrew switch php-5.6.20" >>
~/.bashrc  
  
# Configure container.  
USER root  
WORKDIR /root  
  
CMD ["/usr/sbin/sshd", "-D"]  

