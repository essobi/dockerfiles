FROM docker.io/kitsudo/aliyun_centos6.6  
ADD http://cn.php.net/distributions/php-5.5.38.tar.gz /root/  
RUN yum install -y tar  
RUN yum groupinstall -y "Development Tools"  
RUN yum install -y libxml2-devel openssl* libcurl-devel libjpeg-devel libpng-
devel freetype-devel libmcrypt-devel  
RUN cd /root && tar xvf php-5.5.38.tar.gz  
RUN cd /root/php-5.5.38 && ./configure --prefix=/usr/local/php --with-mysql
--with-pdo-mysql --with-iconv-dir --with-freetype-dir --with-jpeg-dir --with-
png-dir --with-zlib --with-libxml-dir --enable-xml --disable-rpath --enable-
bcmath --enable-shmop --enable-sysvsem --enable-inline-optimization --with-
curl --with-mcrypt --enable-fileinfo --enable-mbregex --enable-fpm --enable-
mbstring --with-gd --enable-gd-native-ttf --with-openssl --with-mhash
--enable-pcntl --enable-sockets --enable-zip --with-pdo-mysql --with-mysql &&
make && make install  
RUN ln -s /usr/local/php/bin/php /bin/php  
RUN yum install -y nginx  
  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer && composer -V  
ADD . /src/app/  
WORKDIR /src/app/  
RUN echo $'\  
service nginx start \n\  
php -S 0.0.0.0:8080 \n\  
'> docker-entrypoint.sh && chmod a+x docker-entrypoint.sh  
  
EXPOSE 80  
ENTRYPOINT /src/app/docker-entrypoint.sh  

