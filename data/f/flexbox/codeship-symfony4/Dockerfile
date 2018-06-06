FROM centos:latest  
  
LABEL name="Flexbox PHP 7.2 + Tools Image" \  
maintainer="Alex Karshin <https://flexbox.it>" \  
license="The Unlicense" \  
build-date="20180224"  
  
COPY google-chrome.repo /etc/yum.repos.d/google-chrome.repo  
  
RUN yum clean all; yum -y update --nogpgcheck  
RUN yum -y install yum-utils  
  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm; \  
rpm -Uvh http://rpms.remirepo.net/enterprise/remi-release-7.rpm; \  
yum-config-manager --enable remi-php72  
  
RUN yum -y install --nogpgcheck \  
epel-release \  
google-chrome-stable \  
wget \  
git \  
nano \  
postfix \  
gcc-c++ \  
make \  
sqlite \  
sqlite-devel \  
zlib-devel \  
libicu-devel \  
gcc \  
freetype-devel \  
libjpeg-turbo-devel \  
libmcrypt-devel \  
libpng-devel \  
openssl-devel \  
curl-devel \  
libxml2-devel \  
gnupg2 \  
xorg-x11-server-Xvfb \  
gtk2 \  
libnotify-devel \  
GConf2 \  
nss \  
libXScrnSaver \  
alsa-lib \  
nginx \  
libXtst \  
libXtst-devel \  
php \  
php-bcmath \  
php-cli \  
php-curl \  
php-devel \  
php-gd \  
php-fpm \  
php-imagick \  
php-intl \  
php-mbstring \  
php-mcrypt \  
php-mysqlnd \  
php-opcache --nogpgcheck \  
php-pdo \  
php-posix \  
php-xml \  
php-zip  
  
RUN rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-
centos-7-0.el7.ngx.noarch.rpm \  
&& yum -y install nginx --nogpgcheck  
  
RUN curl https://phar.phpunit.de/phpunit.phar -L -o phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt. Maybe a new
version was released and you forgot to update the verification hash?';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar /usr/local/bin/composer  
  
RUN curl --silent --location https://rpm.nodesource.com/setup_9.x | bash - &&
\  
yum install -y nodejs  
  
RUN chown -R nginx:nginx /var/lib/php/session && chmod 0777
/var/lib/php/session  
RUN mkdir -p /var/www/.config && \  
chown -R nginx:nginx /var/www/.config  
  
ARG userid=1000  
ARG groupid=1000  
RUN usermod -u $userid nginx  
RUN groupmod -g $groupid nginx  
  
WORKDIR /html  
  
STOPSIGNAL SIGTERM  
  
COPY start.sh /tmp/start.sh  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY www.conf /etc/php-fpm.d/www.conf  
COPY php.ini /etc/php.d/01-docker.ini  
  
CMD ["/tmp/start.sh"]  

