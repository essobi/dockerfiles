FROM centos:7  
MAINTAINER Eric <eric.zhang@famesmart.com>  
  
ENV NGINX_VERSION 1.11.6  
ENV PHP_VERSION 7.1.0  
  
RUN set -x && \  
yum install -y gcc \  
gcc-c++ \  
autoconf \  
automake \  
libtool \  
make \  
cmake && \  
#Install PHP library  
## libmcrypt-devel DIY  
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm && \  
yum install -y zlib \  
zlib-devel \  
openssl \  
openssl-devel \  
pcre-devel \  
libxml2 \  
libxml2-devel \  
libcurl \  
libcurl-devel \  
libpng-devel \  
libjpeg-devel \  
freetype-devel \  
libmcrypt-devel \  
openssh-server \  
python-setuptools && \  
  
#Add user  
mkdir -p /data/{www,phpext} && \  
useradd -r -s /sbin/nologin -d /data/www -m -k no www && \  
  
#install npm  
curl -sL -o /etc/yum.repos.d/khara-nodejs.repo
https://copr.fedoraproject.org/coprs/khara/nodejs/repo/epel-7/khara-nodejs-
epel-7.repo && \  
yum install -y nodejs nodejs-npm && \  
# npm install antd --save && \  
#install yum tools  
mkdir /fame && \  
cd /fame && \  
  
yum install epel-release -y && \  
  
rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro && \  
rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-
release-0-5.el7.nux.noarch.rpm && \  
yum install harfbuzz -y && \  
  
yum install wget -y && \  
yum groupinstall "Development Tools" -y && \  
#install ffmpeg  
yum install fontconfig fribidi -y && \  
rpm -ivh
http://springdale.math.ias.edu/data/puias/7/x86_64/os/Addons/Packages/libass-0.13.4-1.sdl7.x86_64.rpm
&& \  
yum install ffmpeg ffmpeg-devel -y && \  
#install opencv3  
  
  
cd /fame && \  
wget http://develdownload.famesmart.com/Python-3.6.2.tar.xz && \  
  
mkdir /usr/local/python3 && \  
tar -xvJf Python-3.6.2.tar.xz && \  
cd Python-3.6.2 && \  
./configure --prefix=/usr/local/python3 && \  
make && make install && \  
  
ln -s /usr/local/python3/bin/python3 /usr/local/bin/python3 && \  
ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3 && \  
  
pip3 install numpy && \  
cd /fame && \  
# opencv  
yum install python-devel python-nose python-setuptools gcc gcc-gfortran
gcc-c++ blas-devel lapack-devel atlas-devel -y && \  
  
yum install gtk2-devel libdc1394-devel libv4l-devel gstreamer-plugins-base-
devel -y && \  
  
yum install libpng-devel libjpeg-turbo-devel jasper-devel openexr-devel
libtiff-devel libwebp-devel -y && \  
  
yum install cmake -y && \  
  
wget http://develdownload.famesmart.com/3.1.0.zip && \  
  
unzip 3.1.0.zip && \  
cd opencv-3.1.0/ && \  
wget http://develdownload.famesmart.com/ippicv_linux_20151201.tgz && \  
mkdir -p 3rdparty/ippicv/downloads/linux-808b791a6eac9ed78d32a7666804320e/ &&
\  
cp ippicv_linux_20151201.tgz
3rdparty/ippicv/downloads/linux-808b791a6eac9ed78d32a7666804320e/ && \  
mkdir build && \  
cd build && \  
  
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D
PYTHON_LIBRARY=/usr/local/python3/lib -D
PYTHON_INCLUDE_DIR=/usr/local/python3/include/python3.6m .. && \  
make && \  
make install && \  
#Download nginx & php  
mkdir -p /home/nginx-php && cd $_ && \  
curl -Lk http://develdownload.famesmart.com/nginx-1.11.6.tar.gz | gunzip | tar
x -C /home/nginx-php && \  
curl -Lk http://develdownload.famesmart.com/php-7.1.0.tar.gz | gunzip | tar x
-C /home/nginx-php && \  
#Make install nginx  
cd /home/nginx-php/nginx-1.11.6 && \  
./configure --prefix=/usr/local/nginx \  
\--user=www --group=www \  
\--error-log-path=/var/log/nginx_error.log \  
\--http-log-path=/var/log/nginx_access.log \  
\--pid-path=/var/run/nginx.pid \  
\--with-pcre \  
\--with-http_ssl_module \  
\--without-mail_pop3_module \  
\--without-mail_imap_module \  
\--with-http_gzip_static_module && \  
make && make install && \  
#Make install php  
cd /home/nginx-php/php-7.1.0 && \  
./configure --prefix=/usr/local/php \  
\--with-config-file-path=/usr/local/php/etc \  
\--with-config-file-scan-dir=/usr/local/php/etc/php.d \  
\--with-fpm-user=www \  
\--with-fpm-group=www \  
\--with-mcrypt=/usr/include \  
\--with-mysqli \  
\--with-pdo-mysql \  
\--with-openssl \  
\--with-gd \  
\--with-iconv \  
\--with-zlib \  
\--with-gettext \  
\--with-curl \  
\--with-png-dir \  
\--with-jpeg-dir \  
\--with-freetype-dir \  
\--with-xmlrpc \  
\--with-mhash \  
\--enable-fpm \  
\--enable-xml \  
\--enable-shmop \  
\--enable-sysvsem \  
\--enable-inline-optimization \  
\--enable-mbregex \  
\--enable-mbstring \  
\--enable-ftp \  
\--enable-gd-native-ttf \  
\--enable-mysqlnd \  
\--enable-pcntl \  
\--enable-sockets \  
\--enable-zip \  
\--enable-soap \  
\--enable-session \  
\--enable-opcache \  
\--enable-bcmath \  
\--enable-exif \  
\--enable-fileinfo \  
\--disable-rpath \  
\--enable-ipv6 \  
\--disable-debug \  
\--without-pear && \  
make && make install && \  
#Install php-fpm  
cd /home/nginx-php/php-7.1.0 && \  
cp php.ini-production /usr/local/php/etc/php.ini && \  
cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf &&
\  
cp /usr/local/php/etc/php-fpm.d/www.conf.default /usr/local/php/etc/php-
fpm.d/www.conf && \  
#Install supervisor  
easy_install supervisor && \  
mkdir -p /var/{log/supervisor,run/{sshd,supervisord}} && \  
#install composer  
#export PATH=$PATH:/usr/local/php/bin && \  
ln -s /usr/local/php/bin/* /usr/local/bin/ && \  
cd /usr/local && \  
mkdir composer && \  
cd composer && \  
php -r "copy('http://develdownload.famesmart.com/installer', 'composer-
setup.php');" && \  
chmod +x composer-setup.php && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar /usr/local/bin/composer && \  
cd /usr/local/bin && \  
chmod a+x composer && \  
#memcached  
cd /fame && \  
yum install memcached libmemcached libmemcached-devel zlib zlib-devel -y && \  
  
git clone https://github.com/php-memcached-dev/php-memcached memcached && \  
cd memcached/ && \  
git checkout php7 && \  
/usr/local/php/bin/phpize && \  
./configure --with-php-config=/usr/local/php/bin/php-config --disable-
memcached-sasl && \  
make && \  
make install && \  
echo "extension=memcached.so">> /usr/local/php/etc/php.ini && \  
  
#thrift  
cd /fame && \  
wget http://develdownload.famesmart.com/bison-2.5.1.tar.gz && \  
tar xvf bison-2.5.1.tar.gz && \  
cd bison-2.5.1 && \  
./configure --prefix=/usr && \  
make && \  
make install && \  
  
yum install bzip2 bzip2-devel bzip2-libs python-devel -y && \  
  
cd /fame && \  
wget http://develdownload.famesmart.com/boost_1_53_0.tar.gz && \  
tar xvf boost_1_53_0.tar.gz && \  
cd boost_1_53_0 && \  
./bootstrap.sh && \  
./b2 && \  
./b2 install && \  
  
cd /fame && \  
wget http://archive.apache.org/dist/thrift/0.9.3/thrift-0.9.3.tar.gz && \  
tar -xvf thrift-0.9.3.tar.gz && \  
# cd thrift-0.9.3 && \  
# # ./bootstrap.sh && \  
# ./configure && \  
# make && \  
# make install && \  
# cd / && \  
  
cd / && \  
wget http://develdownload.famesmart.com/ffmpeg.tar && \  
tar -xvf ffmpeg.tar && \  
rm -rf ffmpeg.tar && \  
  
# Clean OS  
# yum remove -y gcc \  
# gcc-c++ \  
# autoconf \  
# automake \  
# libtool \  
# make \  
# cmake && \  
yum clean all && \  
rm -rf /tmp/* /var/cache/{yum,ldconfig} /etc/my.cnf{,.d} && \  
mkdir -p --mode=0755 /var/cache/{yum,ldconfig} && \  
find /var/log -type f -delete && \  
rm -rf /home/nginx-php && \  
rm -rf /fame && \  
  
# yum clean all && \  
# rm -rf /tmp/* /var/cache/{yum,ldconfig} /etc/my.cnf{,.d} && \  
# mkdir -p --mode=0755 /var/cache/{yum,ldconfig} && \  
# find /var/log -type f -delete && \  
# rm -rf /home/nginx-php && \  
# rm -rf /fame && \  
#Change Mod from webdir  
chown -R www:www /data/www  
  
#Add supervisord conf  
ADD supervisord.conf /etc/  
  
#Create web folder  
VOLUME ["/data/www", "/usr/local/nginx/conf/ssl",
"/usr/local/nginx/conf/vhost", "/usr/local/php/etc/php.d", "/data/phpext"]  
  
ADD index.php /data/www/  
  
#ADD extini/ /usr/local/php/etc/php.d/  
#ADD extfile/ /data/phpext/  
#Update nginx config  
ADD nginx.conf /usr/local/nginx/conf/  
  
#Start  
ADD start.sh /  
RUN chmod +x /start.sh  
  
#Set port  
EXPOSE 80 443  
  
#Start it  
ENTRYPOINT ["/start.sh"]  
  
#Start web server  
#CMD ["/bin/bash", "/start.sh"]  

