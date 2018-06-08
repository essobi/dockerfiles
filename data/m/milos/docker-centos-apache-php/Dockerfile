FROM gpmidi/centos-5.6  
  
#--------------------------------------  
# initialize  
#--------------------------------------  
# useradd apache  
RUN groupadd apache  
RUN useradd -g apache -s /sbin/nologin apache  
  
RUN yum -y install wget autoconf  
RUN yum -y install tar gcc gcc-c++ kernel-devel diffutils make bison perl
t1lib-devel  
  
#--------------------------------------  
# install Apache 2.2.27  
#--------------------------------------  
  
# resolving dependence  
RUN yum -y install zlib-devel openssl-devel  
RUN yum -y install apr apr-util cyrus-sasl-lib file mailcap openldap
postgresql-libs  
RUN yum -y install system-logos  
  
RUN (\  
cd /usr/local/src;\  
wget -O httpd-2.2.27.tar.gz
http://archive.apache.org/dist/httpd/httpd-2.2.27.tar.gz;\  
tar zxvf httpd-2.2.27.tar.gz;\  
cd httpd-2.2.27;\  
./configure \  
--prefix=/usr/local/apache \  
--enable-so \  
--enable-mods-shared=all \  
--enable-ssl;\  
make;\  
make install;\  
make clean;\  
cp -f ./build/rpm/httpd.init /etc/rc.d/init.d/httpd;\  
chmod +x /etc/rc.d/init.d/httpd;\  
)  
  
  
RUN sed -i -e "s/!\/replace\/with\/path\/to\/perl\/interpreter
-w/!\/usr\/bin\/perl -w/g" /usr/local/apache/bin/apxs  
  
  
  
#--------------------------------------  
# install PHP 5.3.8  
#--------------------------------------  
  
  
# resolving dependence  
RUN yum -y install libxml2-devel libjpeg-devel libpng-devel pcre-devel
bzip2-devel gmp-devel sqlite-devel curl-devel libXpm-devel freetype-devel
t1lib-devel libmhash-devel postgresql-devel  
  
# install PHP  
RUN (\  
cd /usr/local/src;\  
wget -O php-5.3.8.tar.gz http://museum.php.net/php5/php-5.3.8.tar.gz;\  
tar xvzf php-5.3.8.tar.gz;\  
cd php-5.3.8;\  
./configure\  
--enable-zip \  
--with-apxs2=/usr/local/apache/bin/apxs \  
--build=x86_64-redhat-linux-gnu \  
--host=x86_64-redhat-linux-gnu \  
--target=x86_64-amazon-linux-gnu \  
--enable-mbstring \  
--enable-zend-multibyte \  
--prefix=/usr \  
--exec-prefix=/usr \  
--bindir=/usr/bin \  
--sbindir=/usr/sbin \  
--sysconfdir=/etc \  
--datadir=/usr/share \  
--includedir=/usr/include \  
--libdir=/usr/lib64 \  
--libexecdir=/usr/libexec \  
--localstatedir=/var \  
--sharedstatedir=/var/lib \  
--mandir=/usr/share/man \  
--infodir=/usr/share/info \  
--cache-file=../config.cache \  
--with-libdir=lib64 \  
--with-config-file-path=/etc \  
--with-config-file-scan-dir=/etc/php.d \  
--disable-debug \  
--with-pic \  
--disable-rpath \  
--without-pear \  
--with-bz2 \  
--with-exec-dir=/usr/bin \  
--with-freetype-dir=/usr \  
--with-png-dir=/usr \  
--with-xpm-dir=/usr \  
--enable-gd-native-ttf \  
--without-gdbm \  
--with-gettext \  
--with-gmp \  
--with-iconv \  
--with-jpeg-dir=/usr \  
--with-openssl \  
--with-zlib \  
--with-layout=GNU \  
--enable-exif \  
--enable-ftp \  
--enable-magic-quotes \  
--enable-sockets \  
--with-kerberos \  
--enable-ucd-snmp-hack \  
--enable-shmop \  
--enable-calendar \  
--without-sqlite \  
--with-libxml-dir=/usr \  
--enable-xml \  
--with-mhash \  
--libdir=/usr/lib64/php \  
--enable-pdo=shared \  
--enable-pdo-sqlite=shared \  
--with-pdo-sqlite=shared \  
--with-gd \  
--enable-dom \  
--enable-dba \  
--without-unixODBC \  
--disable-xmlreader \  
--disable-xmlwriter \  
--with-sqlite3 \  
--enable-phar \  
--enable-fileinfo \  
--enable-json \  
--without-pspell \  
--disable-wddx \  
--with-curl \  
--disable-posix \  
--disable-sysvmsg \  
--disable-sysvshm \  
--disable-sysvsem \  
  
make;\  
make install;\  
make clean;\  
  
)  
  
  
RUN sed -i -e "s/DirectoryIndex \\(.\\+\\)/DirectoryIndex index.php \1/g"
/usr/local/apache/conf/httpd.conf  
RUN sed -i -e "s/^#\\(Include conf\/extra\/httpd-vhosts.conf\\)$/Include
conf\/extra\/*.conf/g" /usr/local/apache/conf/httpd.conf  
RUN sed -i -e "s/^#\\(EnableMMAP off\\)$/\1/g"
/usr/local/apache/conf/httpd.conf  
RUN sed -i -e "s/^#\\(EnableSendfile off\\)$/\1/g"
/usr/local/apache/conf/httpd.conf  
  
# service  
#RUN sed -i -e
"s/^\\(httpd\\)=\${\\(HTTPD\\)-.\\+}$/\1=\${\2-\/usr\/local\/apache\/bin\/httpd}/g"
/etc/rc.d/init.d/httpd  
#RUN sed -i -e
"s/^\\(pidfile\\)=\${\\(PIDFILE\\)-.\\+}$/\1=\${\2-\/usr\/local\/apache\/logs\/httpd\\.pid}/g"
/etc/rc.d/init.d/httpd  
#RUN sed -i -e
"s/CONFFILE=.\\+$/CONFFILE=\/usr\/local\/apache\/conf\/httpd\\.conf/g"
/etc/rc.d/init.d/httpd  
  
# Adds MIME type for PHP inside Apache config  
RUN echo "AddType application/x-httpd-php .php" >>
/usr/local/apache/conf/httpd.conf  
  
RUN cp -f /usr/local/src/php-5.3.8/php.ini-development /etc/php.ini;  
  
# Composer fix  
RUN echo "detect_unicode = Off" >> /etc/php.ini  
  
# Compile and Install Xdebug  
RUN (\  
wget http://pecl.php.net/get/xdebug-2.2.7.tgz; \  
tar zxvf xdebug-2.2.7.tgz; \  
cd xdebug-2.2.7; \  
phpize; \  
./configure --enable-xdebug; \  
make; \  
make install; \  
)  
  
RUN echo "zend_extension = /usr/lib64/php/20090626/xdebug.so" >> /etc/php.ini  
  
  
ADD apache-run.sh /apache-run.sh  
RUN chmod 0500 /apache-run.sh  
  
EXPOSE 80  
CMD ["/apache-run.sh"]  

