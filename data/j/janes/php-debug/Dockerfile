FROM debian:jessie  
# package with compile:  
# -- build-essential autoconf automake libtool bison2.7 re2c  
RUN apt-get update && apt-get install -y \  
build-essential autoconf automake libtool re2c wget git gdb \  
libgmp-dev && \  
rm -rf /var/lib/apt/lists/* && \  
ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h  
  
COPY .gdbinit /tmp/.gdbinit  
ENV PHP_VERSION php-5.6.20  
ENV PHP_URL https://secure.php.net/get/php-5.6.20.tar.gz/from/this/mirror  
ENV PATH "/opt/bison/bin:$PATH"  
ENV PATH "/opt/php/bin:$PATH"  
  
RUN cd /tmp && wget http://ftp.gnu.org/gnu/bison/bison-2.7.tar.gz && \  
tar -xvf bison-2.7.tar.gz && \  
rm bison-2.7.tar.gz && \  
cd bison-2.7 && \  
./configure \--prefix=/opt/bison \--with-libiconv-prefix=/opt/libiconv && \  
make && make install && \  
rm -rf /tmp/bison-2.7  
  
RUN cd /root && wget -O php-src.tar.gz "$PHP_URL" && \  
tar -zxvf php-src.tar.gz && \  
rm php-src.tar.gz && \  
mv $PHP_VERSION php-src && \  
cd php-src && \  
./configure \--disable-all \--enable-debug \--prefix=/opt/php \--with-gmp && \  
make && make install && \  
cp /root/php-src/.gdbinit /root/.gdbinit && \  
cat /tmp/.gdbinit >> /root/.gdbinit  
  
  
RUN git clone https://github.com/derickr/vld.git /root/vld && \  
cd /root/vld && \  
phpize && \  
./configure && \  
make && make install && \  
echo "extension=vld.so" >> /opt/php/lib/php.ini && \  
rm -rf /root/vld  
# install xdebug  
RUN cd /root && wget http://xdebug.org/files/xdebug-2.5.4.tgz && \  
tar -xvzf xdebug-2.5.4.tgz && \  
rm xdebug-2.5.4.tgz && \  
cd xdebug-2.5.4 && \  
phpize && \  
./configure && \  
make && make install && \  
echo "zend_extension=xdebug.so" >> /opt/php/lib/php.ini && \  
rm -rf /root/xdebug-2.5.4 && \  
mkdir /www  
  
  
WORKDIR /www  
#VOLUME ["/www"]  
  
CMD ["/bin/bash"]  

