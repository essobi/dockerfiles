FROM php:7.1.17-fpm  
SHELL ["/bin/bash", "-c"]  
  
RUN apt update  
RUN apt-get -o Acquire::ForceIPv4=true install -y libgmp-dev build-essential
cmake \  
git libpcre3-dev libssl-dev wget libtool \  
m4 automake nano unzip  
  
WORKDIR /tmp  
RUN wget http://dist.libuv.org/dist/v1.13.1/libuv-v1.13.1.tar.gz  
RUN tar xzf libuv-v1.13.1.tar.gz  
  
WORKDIR /tmp/libuv-v1.13.1  
RUN ./autogen.sh  
RUN ./configure  
RUN make install  
  
WORKDIR /tmp  
RUN git clone https://github.com/datastax/cpp-driver  
  
WORKDIR /tmp/cpp-driver/build  
RUN cmake ..  
RUN make  
RUN make install  
  
RUN pecl install cassandra  
  
RUN echo "extension=cassandra.so" >> /usr/local/etc/php/conf.d/docker-php-ext-
pdo_cassandra.ini  
RUN echo "/usr/local/lib/x86_64-linux-gnu" >>
/etc/ld.so.conf.d/extraLibraries.conf  
RUN ldconfig  
  
RUN docker-php-ext-install pdo pdo_mysql  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
WORKDIR /var/www  

