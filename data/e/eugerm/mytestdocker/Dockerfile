FROM ubuntu:14.04  
MAINTAINER flant <256@flant.com>  
  
RUN apt-get update -q && apt-get install -y \  
supervisor \  
curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -s
https://packagecloud.io/install/repositories/flant/php_fpm_docker/script.deb.sh
| sudo bash \  
&& apt-get install -y \  
php5-cli=5.5.34+dfsg-1+deb.sury.org~trusty+1buildizer2 \  
libapache2-mod-php5=5.5.34+dfsg-1+deb.sury.org~trusty+1buildizer2 \  
php5-common=5.5.34+dfsg-1+deb.sury.org~trusty+1buildizer2 \  
php5=5.5.34+dfsg-1+deb.sury.org~trusty+1buildizer2 \  
php5-fpm=5.5.34+dfsg-1+deb.sury.org~trusty+1buildizer2 \  
php5-gd=5.5.34+dfsg-1+deb.sury.org~trusty+1buildizer2 \  
php5-curl=5.5.34+dfsg-1+deb.sury.org~trusty+1buildizer2 \  
php5-mysql=5.5.34+dfsg-1+deb.sury.org~trusty+1buildizer2 \  
libnss-db;  
RUN /bin/bash -lec "\  
mkdir /.config; \  
cp /etc/passwd /.config/etc-passwd; \  
ln -fs /.config/etc-passwd /etc/passwd; \  
cp /etc/group /.config/etc-group; \  
ln -fs /.config/etc-group /etc/group; \  
mkdir /.config/ssmtp; \  
ln -fs /.config/ssmtp /etc/ssmtp; \  
mkdir /web; \  
rm -rf /etc/supervisor/conf.d; "  
RUN echo "zend_extension=opcache.so \nopcache.memory_consumption=64
\nopcache.max_accelerated_files=100000 \nopcache.save_comments=0" >
/etc/php5/mods-available/opcache.ini;  
RUN sed -r -i 's/compat/compat\ db/g' /etc/nsswitch.conf;  
RUN sed -r -i
's/include=\/etc\/php5\/fpm\/pool.d\//\#include=\/etc\/php5\/fpm\/pool.d\//g'
/etc/php5/fpm/php-fpm.conf;  
RUN echo "docker_socket = /rootfs/run/docker.sock
\ninclude=/.config/pool.d/*.conf" >> /etc/php5/fpm/php-fpm.conf;  

