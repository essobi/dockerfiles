# Set the base image to centos6.8  
FROM centos:6.8  
  
# File Author / Maintainer  
MAINTAINER lvyalin lvyalin.yl@gmail.com  
  
# php build  
RUN cd /usr/src && \  
yum -y install libxml2-devel curl-devel libpng-devel gd-devel autoconf zlib-
devel gcc make openssl-devel unzip crontabs && \  
curl http://php.net/distributions/php-7.1.7.tar.gz -o php-7.1.7.tar.gz && \  
tar xvf php-7.1.7.tar.gz && cd php-7.1.7 && \  
./configure --prefix=/usr/local/php --with-mysqli=mysqlnd --with-pdo-
mysql=mysqlnd --with-gd --with-jpeg-dir=/usr/lib64/ \--with-iconv --with-
openssl --with-curl --enable-pcntl --with-zlib --enable-bcmath --enable-json
--enable-fpm --enable-mbstring --enable-soap --enable-opcache && \  
make && make install && yum clean all && cd /usr/src && rm -rf php-7.1.7*  
  
# env path  
ENV PATH=$PATH:/usr/local/php/bin:/usr/local/php/sbin/  
  
# extension  
RUN cd /usr/src && \  
curl http://pecl.php.net/get/yaf-3.0.4.tgz -o yaf-3.0.4.tgz && tar zxvf
yaf-3.0.4.tgz && \  
cd yaf-3.0.4 && /usr/local/php/bin/phpize && ./configure --with-php-
config=/usr/local/php/bin/php-config && make && make install && cd /usr/src &&
rm -rf yaf-3.0.4* && \  
  
### yac  
cd /usr/src && \  
curl http://pecl.php.net/get/yac-2.0.1.tgz -o yac-2.0.1.tgz && tar zxvf
yac-2.0.1.tgz && \  
cd yac-2.0.1 && /usr/local/php/bin/phpize && ./configure --with-php-
config=/usr/local/php/bin/php-config && make && make install && cd /usr/src &&
rm -rf yaf-3.0.4* && \  
  
### redis  
cd /usr/src && \  
curl http://pecl.php.net/get/redis-3.1.1.tgz -o redis-3.1.1.tgz && tar zxvf
redis-3.1.1.tgz && \  
cd redis-3.1.1 && /usr/local/php/bin/phpize && ./configure --with-php-
config=/usr/local/php/bin/php-config && make && make install && cd /usr/src &&
rm -rf redis-3.1.1* && \  
  
### phpunit  
cd /usr/src && \  
curl https://phar.phpunit.de/phpunit-6.1.4.phar -o phpunit-6.1.4.phar && \  
mv phpunit-6.1.4.phar /usr/local/bin/phpunit && \  
chmod +x /usr/local/bin/phpunit  
  
# config  
COPY conf/php-fpm.conf /usr/local/php/etc/  
COPY conf/www.conf /usr/local/php/etc/php-fpm.d/  
COPY conf/php.*.ini /usr/local/php/lib/  
COPY ./docker-entrypoint.sh /usr/local/php/bin/  
  
#framewok  
RUN mkdir -p /data1/htdocs/ && cd /data1/htdocs/ && curl
https://codeload.github.com/ifintech/phplib/zip/master -o phplib.zip && unzip
phplib.zip && rm phplib.zip  
  
### consumer  
RUN cd /usr/src && \  
curl https://raw.githubusercontent.com/ifintech/phplib-
channel/master/bin/consumer -o consumer && \  
mv consumer /usr/local/bin/consumer && \  
chmod +x /usr/local/bin/consumer  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

