FROM blinkmobile/apache-httpd:2.4.7  
# update the base image  
RUN apt-get update  
RUN apt-get install apt-utils -y  
RUN apt-get upgrade -y  
  
# install build tools  
RUN apt-get -y install git curl build-essential re2c m4  
  
# install development headers (needed for Ruby, Node.JS and PHP)  
RUN apt-get -y install libcurl4-openssl-dev libmysqlclient-dev libssl-dev
libxml2-dev libxslt1-dev zlib1g-dev  
  
# install development libraries for PHP  
RUN apt-get -y build-dep php5 php5-cli  
RUN apt-get -y install libedit-dev libreadline-dev libmhash-dev libt1-dev
libzip2 libxpm-dev libgd2-xpm-dev libfreetype6-dev libmcrypt-dev  
  
ENV PATH /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin  
  
# install bison-2.6.x, needed to compile PHP 5.3.x  
WORKDIR /usr/src  
RUN curl -O http://ftp.gnu.org/gnu/bison/bison-2.6.5.tar.gz  
RUN curl -O http://ftp.gnu.org/gnu/bison/bison-2.6.5.tar.gz.sig  
# TODO: verify GPG signature  
WORKDIR /usr/src  
RUN tar zxf bison-2.6.5.tar.gz  
WORKDIR /usr/src/bison-2.6.5  
RUN ./configure --prefix=/usr/local  
RUN make install  
WORKDIR /usr/src  
RUN rm -fr /usr/src/bison-2.6.5  
  
# install php-build, needed for PHP 5.3.x  
RUN mkdir /opt/php-build  
RUN git clone https://github.com/CHH/php-build.git /opt/php-build  
RUN bash /opt/php-build/install.sh  
RUN rm -fr /opt/php-build  
  
# download PHP 5.3.29 source code  
#RUN mkdir -p /tmp/php-build/packages/5.3.29  
#WORKDIR /tmp/php-build/packages/5.3.29  
#RUN curl -O http://php.net/distributions/php-5.3.29.tar.bz2  
#RUN curl -O http://php.net/distributions/php-5.3.29.tar.bz2.asc  
# TODO: verify GPG signature  
# TODO: figure out why php-build keeps re-downloading this anyway :S  
# install PHP 5.3.29  
ENV MAKEOPTS -j3  
ENV EXTRA_LIBS -lstdc++ -lssl -lcrypto  
ENV PHP_BUILD_CONFIGURE_OPTS --with-gettext --with-gmp-dir=/usr --with-mhash
--enable-cli --with-libxml-dir=/usr --with-bz2 --enable-calendar --disable-dba
--with-t1lib --with-xpm --with-freetype --enable-gd-native-ttf --with-icu-
dir=/usr --with-libedit --enable-mbregex --enable-sysvmsg --enable-wddx
--with-iconv-dir=/usr --with-pcre-regex --enable-fileinfo --enable-pdo
--enable-simplexml --disable-cgi --disable-fpm --enable-intl --with-apxs2
--enable-maintainer-zts  
RUN php-build --pear 5.3.29 /usr/local  
RUN a2enmod php5  
RUN pecl upgrade radius  
RUN apt-get -y install libmagickwand-dev  
RUN pecl upgrade imagick  
  
WORKDIR /  
  
# cleanup some unwanted packages  
RUN apt-get -y remove build-essential g++ gcc  
RUN apt-get -y autoremove  
RUN rm -fr /tmp/php-build*  
  
ENTRYPOINT ["/usr/local/bin/php"]  

