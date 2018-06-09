FROM ubuntu:trusty  
MAINTAINER Yorgos Tavantzopoulos <g.tavantzopoulos@gmail.com>  
  
#Apache mandatory environment variables  
ENV SERVER_ROOT=/app  
  
RUN mkdir -p /var/lock/apache2 && \  
mkdir -p /var/run/apache2 && \  
mkdir -p /var/log/apache2 && \  
mkdir -p /etc/apache2 && \  
mkdir -p $SERVER_ROOT  
  
ADD . /docker  
ADD ./apache2 /etc/apache2  
ADD ./supervisord.conf /etc/supervisor/conf.d/httpd.conf  
  
EXPOSE 80  
EXPOSE 443  
  
RUN apt-get update -qq -y && apt-get install supervisor wget build-essential
libxml2 libxml2-dev libsslcommon2-dev libcurl4-openssl-dev pkg-config libssl-
dev libpcre3 libpcre3-dev libbz2-dev libjpeg-dev libpng12-dev libfreetype6-dev
libt1-dev libgd2-xpm-dev libgmp-dev libmysqlclient-dev libsasl2-dev libmhash-
dev libtidy-dev libtidy-0.99-0 libxslt1-dev libmcrypt-dev libc-client2007e-dev
libpspell-dev libmm-dev libmm14 libsnmp-dev -qq -y && \  
mkdir -p /usr/include/freetype2/freetype && \  
ln -s /usr/include/freetype2/freetype.h
/usr/include/freetype2/freetype/freetype.h && \  
ln -s /usr/lib/libc-client.so /usr/lib/x86_64-linux-gnu/libc-client.so && ln
-s /usr/lib/libc-client.a /usr/lib/x86_64-linux-gnu/libc-client.a && \  
ln -s /usr/lib/libtidy.so /usr/lib/x86_64-linux-gnu/libtidy.so && ln -s
/usr/lib/libtidy.a /usr/lib/x86_64-linux-gnu/libtidy.a  
  
WORKDIR /root  
RUN wget http://archive.apache.org/dist/httpd/httpd-2.0.65.tar.gz && \  
tar -xzf httpd-2.0.65.tar.gz  
  
WORKDIR httpd-2.0.65  
  
RUN ./configure --enable-so && \  
make && make install && \  
ln -s /usr/local/apache2/bin/apachectl /usr/local/bin/apachectl  
  
WORKDIR /root  
RUN wget http://museum.php.net/php5/php-5.2.17.tar.gz && \  
tar -xzf php-5.2.17.tar.gz  
WORKDIR php-5.2.17  
  
RUN cp -f /docker/patches/node.c ext/dom/node.c && \  
cp -f /docker/patches/documenttype.c ext/dom/documenttype.c && \  
cp -f /docker/patches/simplexml.c ext/simplexml/simplexml.c && \  
patch ext/openssl/xp_ssl.c
/docker/patches/debian_patches_disable_SSLv2_for_openssl_1_0_0.patch && \  
'./configure' '--enable-bcmath' '--enable-calendar' '--enable-exif' '--enable-
ftp' '--enable-gd-native-ttf' '--enable-libxml' '--enable-magic-quotes' '--
enable-mbstring' '--enable-pdo=shared' '--enable-soap' '--enable-sockets' '--
enable-wddx' '--enable-zend-multibyte' '--enable-zip' '--prefix=/usr' '--with-
bz2' '--with-curl=/opt/curlssl/' '--with-curlwrappers' '--with-freetype-
dir=/usr' '--with-gd' '--with-gettext' '--with-
imap=/opt/php_with_imap_client/' '--with-imap-ssl=/usr' '--with-jpeg-dir=/usr'
'--with-kerberos' '--with-libdir=/lib/x86_64-linux-gnu' '--with-libexpat-
dir=/usr' '--with-libxml-dir=/opt/xml2' '--with-libxml-dir=/opt/xml2/' '--
with-mcrypt=/opt/libmcrypt/' '--with-mhash=/opt/mhash/' '--with-mime-magic' '
--with-mm=/opt/mm/' '--with-mysql=/usr' '--with-mysql-
sock=/var/lib/mysql/mysql.sock' '--with-mysqli=/usr/bin/mysql_config' '--with-
openssl=/usr' '--with-openssl-dir=/usr' '--with-pcre-dir=/opt/pcre' '--with-
pdo-mysql=shared' '--with-pdo-sqlite=shared' '--with-pic' '--with-png-
dir=/usr' '--with-pspell' '--with-sqlite=shared' '--with-tidy=shared,/usr' '--
with-ttf' '--with-xmlrpc' '--with-xpm-dir=/usr' '--with-xsl=/opt/xslt/' '--
with-zlib' '--with-zlib-dir=/usr' '--with-apxs2=/usr/local/apache2/bin/apxs'
&& \  
make && \  
make install && \  
apt-get autoremove --purge -qq -y && \rm -rf /root/httpd-2.0.65 && \  
rm -f /root/httpd-2.0.65.tar.gz && \  
rm -rf /root/php-5.2.17 && \  
rm -f /root/php-5.2.17.tar.gz  
  
WORKDIR $SERVER_ROOT  
CMD "supervisord" "-c" "/etc/supervisor/supervisord.conf"  

