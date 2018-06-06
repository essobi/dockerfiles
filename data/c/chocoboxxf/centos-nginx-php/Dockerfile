FROM centos:7  
MAINTAINER https://github.com/chocoboxxf/docker-centos-nginx-php  
  
# add nginx, php files  
  
ADD container-files/soft/nginx-1.10.1.bin.tar.gz /tmp/soft/  
ADD container-files/soft/php-7.0.10.bin.tar.gz /tmp/soft/  
ADD container-files/conf/* /tmp/conf/  
  
RUN \  
`# install basic libs ...` \  
yum install -y epel-release && \  
yum update -y && \  
yum groupinstall -y "Development Tools" && \  
yum install -y gcc gcc-c++ autoconf libjpeg libjpeg-devel libpng libpng-devel
freetype freetype-devel libpng libpng-devel libxml2 libxml2-devel zlib zlib-
devel glibc glibc-devel glib2 glib2-devel bzip2 bzip2-devel ncurses curl
openssl-devel gdbm-devel db4-devel libXpm-devel libX11-devel gd-devel gmp-
devel readline-devel libxslt-devel expat-devel xmlrpc-c xmlrpc-c-devel
libmcrypt libmcrypt-devel pcre pcre-devel mysql libmemcached libmemcached-
devel wget && \  
  
`# install nginx & php ...` \  
mkdir -p /root/programs && \  
cd /root/programs && \  
cp -rf /tmp/soft/nginx-1.10.1 /root/programs/nginx-1.10.1 && \  
cp -rf /tmp/soft/php-7.0.10 /root/programs/php-7.0.10 && \  
ln -sf /root/programs/nginx-1.10.1 /root/programs/nginx && \  
ln -sf /root/programs/php-7.0.10 /root/programs/php && \  
  
`# copying nginx & php config files ...` \  
cp -f /tmp/conf/nginx.conf /root/programs/nginx/conf/nginx.conf && \  
cp -f /tmp/conf/fastcgi_params /root/programs/nginx/conf/fastcgi_params && \  
cp -f /tmp/conf/php.ini /root/programs/php/lib/php.ini && \  
cp -f /tmp/conf/php-fpm.conf /root/programs/php/etc/php-fpm.conf && \  
cp -f /tmp/conf/www.conf /root/programs/php/etc/php-fpm.d/www.conf  
  
ENV \  
PATH=/root/programs/nginx/sbin:/root/programs/php/bin:/root/programs/php/sbin:$PATH  
  
EXPOSE 80 443  
  
# start nginx, php-fpm  
  
ADD container-files/script/* /tmp/script/  
  
# put customized config and code files to /data  
  
VOLUME ["/data"]  
WORKDIR /data  
  
ENTRYPOINT ["/tmp/script/bootstrap.sh"]

