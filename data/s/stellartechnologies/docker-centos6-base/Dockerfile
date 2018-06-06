FROM centos:6  
MAINTAINER Andy Kirkham <andy@spiders-lair.com>  
  
RUN yum -y update && yum clean all \  
&& yum -y install wget curl tar rpm bzip2 \  
&& rpm -ivh http://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/epel-
release-6-5.noarch.rpm \  
&& rpm -ivh http://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/ius-
release-1.0-11.ius.centos6.noarch.rpm \  
&& yum -y groupinstall 'Development Tools' \  
&& yum -y install bzip2-devel libcurl-devel t1lib-devel mcrypt libmcrypt
libmcrypt-devel \  
&& yum -y install openssl openssl-devel \  
&& yum -y install libxml2 libxml2-devel libtool-ltdl-devel \  
&& yum -y install libjpeg-turbo-devel libpng-devel libXpm-devel freetype-devel
t1lib-devel \  
&& yum -y install gmp-devel mcrypt libmcrypt libmcrypt-devel libtidy-devel
tidy bison libtool-ltdl-devel \  
&& yum -y install autoconf213 \  
&& yum -y install unixODBC unixODBC-devel libsodium libsodium-devel \  
&& yum -y install mysql55 mysql55-libs mysqlclient16-devel mysql55-devel
sqlite-devel \  
&& yum -y install xz-libs libffi-devel golang-bin  
  
COPY dist/CMake-v3.3.1.zip /tmp/CMake-v3.3.1.zip  
RUN cd /tmp && unzip CMake-v3.3.1.zip && rm -f CMake-v3.3.1.zip \  
&& cd CMake-3.3.1 \  
&& ./configure && make && make install && make clean \  
&& cd .. && rm -rf CMake-3.3.1  
  
COPY dist/Jansson-v2.7.zip /tmp/Jansson-v2.7.zip  
RUN cd /tmp && unzip Jansson-v2.7.zip && rm -f Jansson-v2.7.zip \  
&& cd /tmp/jansson-2.7 \  
&& sh autoreconf -i && ./configure && make && make install \  
&& cd /tmp && rm -rf jansson-2.7  
  
COPY dist/Libevent-release-2.0.22-stable.zip /tmp/Libevent-
release-2.0.22-stable.zip  
RUN cd /tmp && unzip Libevent-release-2.0.22-stable.zip && rm -f Libevent-
release-2.0.22-stable.zip \  
&& cd Libevent-release-2.0.22-stable \  
&& sh autogen.sh && ./configure && make && make install \  
&& cd .. && rm -rf Libevent-release-2.0.22-stable  
  
COPY dist/memcached-1.4.24.tar.gz /tmp/memcached-1.4.24.tar.gz  
RUN cd /tmp && tar -zxf memcached-1.4.24.tar.gz && rm -f
memcached-1.4.24.tar.gz \  
&& cd memcached-1.4.24 \  
&& ./configure && make && make install && cd ~ && rm -rf memcached-1.4.24  
  
COPY dist/ZeroMQ-v3.2.5.zip /tmp/ZeroMQ-v3.2.5.zip  
RUN cd /tmp && unzip ZeroMQ-v3.2.5.zip && rm -f ZeroMQ-v3.2.5.zip \  
&& cd zeromq3-x-3.2.5 \  
&& sh autogen.sh && ./configure && make && make install \  
&& cd .. && rm -rf zeromq3-x-3.2.5  
  
COPY dist/CZMQ-v3.0.2.zip /tmp/CZMQ-v3.0.2.zip  
RUN cd /tmp && unzip CZMQ-v3.0.2.zip && rm -f CZMQ-v3.0.2.zip \  
&& cd czmq-3.0.2 \  
&& sh autogen.sh && ./configure && make && make install \  
&& cd /tmp && rm -rf czmq-3.0.2  
  
RUN cd /tmp && wget https://github.com/alanxz/rabbitmq-c/archive/v0.7.1.zip \  
&& unzip v0.7.1.zip && rm -f v0.7.1.zip \  
&& cd rabbitmq-c-0.7.1 && mkdir _build && cd _build \  
&& cmake -DCMAKE_INSTALL_PREFIX=/usr .. \  
&& cmake --build . --config Release --target install \  
&& cd /tmp && rm -rf rabbitmq-c-0.7.1  
  
RUN yum -y install php56u php56u-devel  
RUN yum -y install php56u-tidy  
  
COPY dist/phpjansson.tgz /tmp/phpjansson.tgz  
RUN cd /tmp && tar -zxf phpjansson.tgz && rm -f phpjansson.tgz \  
&& cd /tmp/phpjansson \  
&& phpize \  
&& ./configure --with-jansson && make && make install  
COPY ini/60-jansson.ini /etc/php.d/60-jansson.ini  
  
COPY dist/php-zmq-1.1.2.zip /tmp/php-zmq-1.1.2.zip  
RUN cd /tmp && unzip php-zmq-1.1.2.zip \  
&& cd /tmp/php-zmq-1.1.2 \  
&& phpize \  
&& ./configure && make && make install  
COPY ini/50-zmq.ini /etc/php.d/50-zmq.ini  
  
RUN cd /tmp && wget https://github.com/pdezwart/php-amqp/archive/v1.6.1.zip \  
&& unzip v1.6.1.zip && rm -f v1.6.1.zip \  
&& cd php-amqp-1.6.1 \  
&& phpize && ./configure --with-amqp && make && make install \  
&& cd /tmp && rm -rf php-amqp-1.6.1  
COPY ini/60-amqp.ini /etc/php.d/60-amqp.ini  
  

