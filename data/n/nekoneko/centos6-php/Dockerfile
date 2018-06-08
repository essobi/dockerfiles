FROM centos:6  
MAINTAINER neko-neko  
ENV PHP_VERSION 5.6.20  
  
RUN yum -y update && yum -y install \  
autoconf \  
automake \  
bison \  
curl-devel \  
gcc \  
gcc-c++ \  
git-core \  
httpd-devel \  
libevent-devel \  
libxml2 \  
libxml2-devel \  
libXpm-devel \  
gmp-devel \  
libicu-devel \  
t1lib-devel \  
aspell-devel \  
mysql-devel \  
openssl \  
openssl-devel \  
bzip2-devel \  
libcurl-devel \  
libjpeg-devel \  
libvpx-devel \  
libpng-devel \  
freetype-devel \  
readline-devel \  
libtidy-devel \  
libxslt-devel \  
zlib \  
zlib-devel \  
wget \  
&& yum clean all  
  
# mcrypt install  
RUN rpm -ivh
http://pkgs.repoforge.org/libmcrypt/libmcrypt-2.5.7-1.2.el6.rf.x86_64.rpm  
RUN rpm -ivh http://pkgs.repoforge.org/libmcrypt/libmcrypt-
devel-2.5.7-1.2.el6.rf.x86_64.rpm  
  
# PHP install  
RUN wget --no-check-certificate
http://jp2.php.net/get/php-$PHP_VERSION.tar.gz/from/this/mirror -O
php-$PHP_VERSION.tar.gz  
RUN tar -xzvf php-$PHP_VERSION.tar.gz  
WORKDIR php-$PHP_VERSION  
RUN ./configure \  
--with-libdir=lib64 \  
--prefix=/usr/local \  
--with-layout=PHP \  
--with-pear \  
--with-apxs2 \  
--enable-json \  
--enable-fileinfo \  
--enable-calendar \  
--enable-bcmath \  
--enable-dom \  
--enable-mbregex \  
--with-gmp \  
--enable-pdo \  
--enable-exif \  
--with-mcrypt \  
--with-mhash \  
--with-zlib \  
--with-bz2 \  
--enable-posix \  
--enable-shmop \  
--enable-zip \  
--enable-ftp \  
--enable-zend-multibyte \  
--enable-mbstring \  
--with-iconv \  
--enable-intl \  
--with-kerberos \  
--with-libmbfl \  
--with-icu-dir=/usr \  
--with-gettext \  
--with-pspell \  
--enable-sockets \  
--with-openssl \  
--with-curl \  
--with-curlwrappers \  
--with-gd \  
--enable-gd-native-ttf \  
--with-jpeg-dir=/usr \  
--with-png-dir=/usr \  
--with-zlib-dir=/usr \  
--with-xpm-dir=/usr \  
--with-vpx-dir=/usr \  
--with-freetype-dir=/usr \  
--with-t1lib=/usr \  
--with-libxml-dir=/usr \  
--enable-mysqlnd \  
--with-mysql=mysqlnd \  
--with-mysqli=mysqlnd \  
--with-pdo-mysql=mysqlnd \  
--enable-soap \  
--with-xmlrpc \  
--with-xsl \  
--with-tidy=/usr \  
--with-readline \  
--enable-pcntl \  
--enable-sysvsem \  
--enable-sysvshm \  
--enable-sysvmsg \  
--enable-shmop  
RUN make && make install  
WORKDIR /  
CMD ["/bin/bash"]  

