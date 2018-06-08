# Version 0.0.1  
FROM centos:7  
MAINTAINER Alan Chu "malevanilla@gmail.com"  
#Update  
RUN yum update -y  
  
#Install base package  
RUN yum install -y git wget make gcc autoconf automake libtool re2c flex bison
xml2lib-devel openssl-devel bzip2-devel libcurl-devel freetype-devel libjpeg-
devel libpng-devel libxslt-devel pam-devel  
  
  
#Clear package  
RUN yum clean all  
  
#Install imap  
RUN mkdir /home/src \  
&& cd /home/src \  
&& wget ftp://ftp.cac.washington.edu/imap/imap-2007f.tar.gz \  
&& tar -zxf imap-2007f.tar.gz \  
&& cd imap-2007f \  
&& make lr5 PASSWDTYPE=std SSLTYPE=unix.nopwd EXTRACFLAGS=-fPIC IP6=4 \  
&& rm -rf /usr/local/imap-2007f \  
&& mkdir /usr/local/imap-2007f \  
&& mkdir /usr/local/imap-2007f/include \  
&& mkdir /usr/local/imap-2007f/lib \  
&& cp c-client/*.h /usr/local/imap-2007f/include/ \  
&& cp c-client/*.c /usr/local/imap-2007f/lib/ \  
&& cp c-client/c-client.a /usr/local/imap-2007f/lib/libc-client.a \  
&& rm -rf /home/src/imap-2007f \  
&& rm /home/src/imap-2007f.tar.gz  
  
#Git PHP  
WORKDIR "/home/src"  
RUN git clone -b PHP-7.1.0 https://github.com/php/php-src.git && cd php-src \  
&& ./buildconf --force \  
&& ./configure \  
\--prefix=/usr/local/php7 \  
\--with-config-file-path=/usr/local/php7/etc \  
\--enable-mbstring \  
\--enable-fpm \  
\--enable-opcache \  
\--with-zlib-dir \  
\--with-freetype-dir \  
\--with-libxml-dir=/usr \  
\--enable-soap \  
\--enable-calendar \  
\--with-curl \  
\--with-zlib \  
\--with-gd \  
\--disable-rpath \  
\--enable-inline-optimization \  
\--with-bz2 \  
\--with-zlib \  
\--enable-sockets \  
\--enable-sysvsem \  
\--enable-sysvshm \  
\--enable-pcntl \  
\--enable-mbregex \  
\--enable-exif \  
\--enable-bcmath \  
\--with-mhash \  
\--enable-zip \  
\--with-pcre-regex \  
\--with-pdo-mysql \  
\--with-mysqli \  
\--enable-gd-native-ttf \  
\--with-openssl \  
\--enable-ftp \  
\--with-imap=/usr/local/imap-2007f \  
\--with-imap-ssl \  
\--with-kerberos \  
\--with-gettext \  
\--with-xmlrpc \  
\--with-xsl \  
&& make && make install \  
&& cp php.ini-production /usr/local/php7/etc/php.ini  
  
WORKDIR "/usr/local/php7/etc"  
RUN mv php-fpm.conf.default php-fpm.conf \  
&& mv php-fpm.d/www.conf.default php-fpm.d/www.conf  
  
WORKDIR "/home/src/php-src/sapi/fpm"  
RUN cp init.d.php-fpm /etc/init.d/php-fpm \  
&& chmod +x /etc/init.d/php-fpm \  
&& chkconfig --add php-fpm \  
&& chkconfig php-fpm on  
RUN rm -rf /home/src  
  
#Modify .conf|.ini file  
#RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php.ini && \  
# sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php-fpm.conf && \  
# sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php.ini && \  
# sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php.ini && \  
# sed -i '/^listen = /clisten = 0.0.0.0:9000' /etc/php-fpm.d/www.conf && \  
# sed -i '/^listen.allowed_clients/c;listen.allowed_clients =' /etc/php-
fpm.d/www.conf && \  
# sed -i '/^;catch_workers_output/ccatch_workers_output = yes' /etc/php-
fpm.d/www.conf && \  
# sed -i "s/php_admin_flag\\[log_errors\\] = .*/;php_admin_flag[log_errors]
=/" /etc/php-fpm.d/www.conf && \  
# sed -i "s/php_admin_value\\[error_log\\] =.*/;php_admin_value[error_log] =/"
/etc/php-fpm.d/www.conf && \  
# sed -i "s/php_admin_value\\[error_log\\] =.*/;php_admin_value[error_log] =/"
/etc/php-fpm.d/www.conf && \  
# echo "php_admin_value[display_errors] = 'stderr'" >> /etc/php-fpm.d/www.conf  
  
  
EXPOSE 9000  
CMD ["/etc/init.d/php-fpm start"]  

