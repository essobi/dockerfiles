# Version 0.1  
  
# 基础镜像  
FROM centos:7  
  
# 维护者信息  
MAINTAINER ll-xzx@qq.com  
  
# 镜像操作命令  
RUN yum update -y && \  
yum install -y wget gcc && \  
yum clean all  
  
  
###############################nginx################################  
RUN useradd -d /usr/local/nginx/ -s /sbin/nologin www && \  
  
yum install -y pcre* openssl* zlib zlib-devel && \  
yum clean all && \  
##安装地址  
mkdir -p /usr/local/nginx/ && \  
mkdir -p /usr/local/nginx/etc/ && \  
mkdir -p /usr/local/nginx/var/logs/ && \  
mkdir -p /usr/local/nginx/var/nginx/ && \  
mkdir -p /usr/local/nginx/var/run/ && \  
mkdir -p /usr/local/nginx/sbin/ && \  
  
mkdir /package && \  
cd /package && \  
wget http://nginx.org/download/nginx-1.8.1.tar.gz && \  
tar -zxf nginx-1.8.1.tar.gz && \  
cd nginx-1.8.1 && \  
./configure --prefix=/usr/local/nginx/ --sbin-path=/usr/local/nginx/sbin/
--conf-path=/usr/local/nginx/etc/nginx.conf --pid-
path=/usr/local/nginx/var/logs/nginx/nginx.pid --error-log-
path=/usr/local/nginx/var/logs/error.log --http-log-
path=/usr/local/nginx/var/logs/access.log --user=www --group=www --with-
http_ssl_module && \  
make && make install && \  
rm -rf /package  
  
################################php################################################  
RUN mkdir -p /data/www/php/logs/ && \  
mkdir -p /data/www/php/userupload && \  
mkdir -p /data/www/php/phpsession && \  
mkdir -p /data/www/php/phpcache/ && \  
mkdir -p /usr/local/php && \  
  
  
yum install -y pcre* openssl* libxml2 libxml2-devel gdbm-devel gd-devel
libjpeg libjpeg-devel libpng libpng-devel xmlrpc-c xmlrpc-c-devel freetype
freetype-devel readline-devel bzip2 bzip2-devel libXpm-devel libX11-devel gmp-
devel libxslt-devel && \  
yum clean all && \  
  
mkdir /package && \  
cd /package && \  
wget http://cn.php.net/distributions/php-5.4.45.tar.gz && \  
tar -zxf php-5.4.45.tar.gz && \  
cd php-5.4.45 && \  
./configure --prefix=/usr/local/php --exec-prefix=/usr/local/php --with-mysql
--with-mysql-sock --with-mysqli --enable-fpm --enable-soap --with-libxml-dir
--with-openssl --with-mhash --with-pcre-regex --with-sqlite3 --with-zlib
--enable-bcmath --with-iconv --with-bz2 --enable-calendar --with-curl --with-
cdb --enable-dom --enable-exif --enable-fileinfo --enable-filter --with-pcre-
dir --enable-ftp --with-gd --with-openssl-dir --with-jpeg-dir --with-png-dir
--with-zlib-dir --with-freetype-dir --enable-gd-native-ttf --enable-gd-jis-
conv --with-gettext --with-gmp --with-mhash --enable-json --enable-
mbstring=all --disable-mbregex --disable-mbregex-backtrack --with-libmbfl
--with-onig --enable-pdo --with-pdo-mysql --with-zlib-dir --with-pdo-sqlite
--with-readline --enable-session --enable-shmop --enable-simplexml --enable-
sockets --enable-sysvmsg --enable-sysvsem --enable-sysvshm --enable-wddx
--with-libxml-dir --with-xsl --enable-zip --enable-mysqlnd-compression-support
--with-pear --enable-mbregex && \  
make && make install && \  
rm -rf /package && \  
ln -s /usr/local/php/bin/php* /usr/bin  
  
  
######################## 配置 ################################  
COPY usr/local /usr/local  
  
################################supervisor##################################  
  
  
RUN yum install python-setuptools -y && \  
easy_install supervisor  
  
COPY supervisord.conf /etc/supervisord.conf  
  
# 容器启动命令  
## /usr/local/nginx/sbin/nginx  
## /usr/local/php/sbin/php-fpm -y /usr/local/php/etc/web3/default/php-fpm.conf
-c /usr/local/php/etc/php.ini -p /usr/local/php/etc/web3/default/  
CMD ["/usr/bin/supervisord"]  
  
  
# 暴漏80端口  
EXPOSE 80  

