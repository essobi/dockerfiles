FROM autoglass/base  
RUN export DEBIAN_FRONTEND=noninteractive && \  
export TERM=xterm && \  
apt-get update && \  
apt-get -y install apache2 \  
fonts-font-awesome \  
fonts-liberation \  
libapache2-mod-php7.0 \  
libapache2-mod-auth-openid \  
fonts-linuxlibertine \  
fonts-lohit-deva \  
fonts-sil-gentium-basic \  
fonts-wqy-microhei \  
libjs-chosen \  
libjs-cropper \  
libjs-jquery \  
libjs-jquery-colorbox \  
libjs-jquery-colorpicker \  
libjs-jquery-cookie \  
libjs-jquery-coolfieldset \  
libjs-jquery-countdown \  
libjs-jquery-datatables \  
libjs-jquery-dotdotdot \  
libjs-mediaelement \  
libphp-phpmailer \  
php-doctrine-dbal \  
php-getid3 \  
php-patchwork-utf8 \  
php-pear \  
php-pimple \  
php-sabre-dav \  
php-seclib \  
php-symfony-console \  
php-symfony-routing \  
php \  
php-curl \  
php-intl \  
php-ldap \  
php-mcrypt \  
smbclient \  
php-cli \  
php-gd \  
php-json \  
php-mysql \  
php-zend-code php-zend-eventmanager php-zend-hydrator php-zend-stdlib \  
libapache2-mod-xsendfile \  
libav-tools \  
php-crypt-chap php-seclib \  
php-apcu \  
php-imagick && \  
echo "ServerName default" >> /etc/apache2/apache2.conf && a2enmod ssl &&
a2ensite default-ssl  
ENV DEBIAN_FRONTEND=noninteractive  
ENV TERM=xterm  
HEALTHCHECK --interval=1m \--timeout=3s CMD nc -zv 127.0.0.1 389 || exit 1

