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
&& yum -y install xz-libs  
  
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
  
# COPY dist/Libevhtp-1.2.10.zip /tmp/Libevhtp-1.2.10.zip  
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
  
RUN yum -y install php56u php56u-devel  
  
COPY dist/phpjansson.tgz /tmp/phpjansson.tgz  
RUN cd /tmp && tar -zxf phpjansson.tgz && rm -f phpjansson.tgz \  
&& cd /tmp/phpjansson \  
&& phpize \  
&& ./configure --with-jansson && make && make install && make clean  
  
COPY ini/60-jansson.ini /etc/php.d/60-jansson.ini  
  
COPY dist/php-zmq-1.1.2.zip /tmp/php-zmq-1.1.2.zip  
RUN cd /tmp && unzip php-zmq-1.1.2.zip \  
&& cd /tmp/php-zmq-1.1.2 \  
&& phpize \  
&& ./configure && make && make install && make clean  
  
RUN yum -y install librabbitmq-devel  
COPY dist/amqp-1.4.0.tgz /tmp/amqp-1.4.0.tgz  
RUN cd /tmp && tar -zxf amqp-1.4.0.tgz && rm -f amqp-1.4.0.tgz \  
&& cd amqp-1.4.0 && phpize && ./configure && make && make install && make
clean \  
&& cd .. && rm -rf amqp-1.4.0  
  
COPY ini/50-zmq.ini /etc/php.d/50-zmq.ini  
COPY ini/50-amqp.ini /etc/php.d/50-amqp.ini  
  
RUN yum -y install php56u-mysqlnd php56u-pecl-memcached php56u-pdo
php56u-mbstring \  
php56u-gd php56u-mcrypt php56u-opcache php56u-pecl-geoip php56u-pecl-pthreads
\  
php56u-process php56u-imap php56u-intl php56u-ldap php56u-pecl-redis
php56u-pecl-imagick \  
php56u-pspell php56u-soap php56u-snmp php56u-tidy php56u-xml php56u-bcmath
php56u-fpm mod_proxy_fcgi  
  
COPY ini/php.ini /etc/php.ini  
  
COPY dist/nanomsg-0.6-beta.zip /tmp/nanomsg-0.6-beta.zip  
RUN cd /tmp && unzip nanomsg-0.6-beta.zip \  
&& cd /tmp/nanomsg-0.6-beta && ./autogen.sh && ./configure && make && make
install  
  
COPY dist/php-nano.zip /tmp/php-nano.zip  
RUN cd /tmp && unzip php-nano.zip  
RUN cd /tmp/php-nano-master && export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
\  
&& phpize \  
&& ./configure --with-nano=/usr/local && make && make install && make clean  
  
COPY ini/50-nano.ini /etc/php.d/50-nano.ini  
  
COPY dist/libevent-0.1.0.tgz /tmp/libevent-0.1.0.tgz  
RUN cd /tmp && tar -zxf libevent-0.1.0.tgz  
RUN cd /tmp/libevent-0.1.0 && phpize && ./configure --with-nano=/usr/local &&
make && make install && make clean  
  
COPY ini/50-libevent.ini /etc/php.d/  
  
COPY dist/xhprof-0.9.4.tgz /tmp/xhprof-0.9.4.tgz  
RUN cd /tmp && tar -zxf xhprof-0.9.4.tgz  
RUN cd /tmp/xhprof-0.9.4/extension && phpize && ./configure && make && make
install && make clean  
  
RUN mkdir -p /var/log/xhprof && chmod 777 /var/log/xhprof  
COPY ini/55-xhprof.ini /etc/php.d/  
  
RUN yum -y install libev libev-devel  
COPY dist/ev-0.2.15.tgz /tmp/ev-0.2.15.tgz  
RUN cd /tmp && tar -zxf ev-0.2.15.tgz  
RUN cd /tmp/ev-0.2.15 && phpize && ./configure && make && make install && make
clean  
  
COPY ini/50-ev.ini /etc/php.d/  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
COPY dist/Python-2.7.9.tgz /tmp/Python-2.7.9.tgz  
RUN cd /tmp && tar -zxf Python-2.7.9.tgz && rm Python-2.7.9.tgz  
RUN cd /tmp/Python-2.7.9 && ./configure && make && make altinstall && cd /tmp
&& rm -rf Python-2.7.9  
RUN cd /usr/local/bin && ln -s python2.7 python  
COPY dist/setuptools-1.4.2.tar.gz /tmp/setuptools-1.4.2.tar.gz  
RUN cd /tmp && tar -zxf setuptools-1.4.2.tar.gz && rm setuptools-1.4.2.tar.gz  
RUN cd /tmp/setuptools-1.4.2 && python2.7 setup.py install  
COPY src/get-pip.py /tmp/get-pip.py  
RUN cd /tmp && cat get-pip.py | python2.7 -  
RUN pip install virtualenv  
RUN yum -y install which pwhois valgrind  
  
RUN yum -y install libffi-devel  
RUN mkdir -p /var/www/html/crossbar  
RUN cd /var/www/html/crossbar && virtualenv python-venv && \  
cd python-venv/ && \  
. bin/activate && \  
pip install crossbar  
  
RUN yum -y install golang-bin  
  
RUN cd /tmp && rm -rf * \  
&& wget files.ajk.io/jdk-8u66-linux-x64.rpm \  
&& rpm -ivh jdk-8u66-linux-x64.rpm \  
&& rm -f jdk-8u66-linux-x64.rpm  
  
RUN yum -y install java-1.8.0-openjdk  
  
RUN cd /tmp && wget http://mirror.sdunix.com/apache/ant/binaries/apache-
ant-1.9.6-bin.zip \  
&& unzip apache-ant-1.9.6-bin.zip && rm -f apache-ant-1.9.6-bin.zip \  
&& mv apache-ant-1.9.6/ /opt/ant \  
&& ln -s /opt/ant/bin/ant /usr/bin/ant  
  
COPY etc/profile.d/ant.sh /etc/profile.d/ant.sh  
COPY etc/profile.d/maven.sh /etc/profile.d/maven.sh  
RUN chmod +x /etc/profile.d/ant.sh && chmod +x /etc/profile.d/maven.sh \  
&& source /etc/profile.d/ant.sh  
  
RUN cd /tmp && wget
http://mirror.cc.columbia.edu/pub/software/apache/maven/maven-3/3.0.5/binaries/apache-
maven-3.0.5-bin.tar.gz \  
&& tar -zxf apache-maven-3.0.5-bin.tar.gz && rm -f apache-
maven-3.0.5-bin.tar.gz \  
&& mv apache-maven-3.0.5 /usr/local/ \  
&& ln -s /usr/local/apache-maven-3.0.5 /usr/local/maven \  
&& source /etc/profile.d/maven.sh  
  
RUN cd /tmp && wget http://files.ajk.io/sencha-dist-6-0-2.tgz \  
&& tar -zxf sencha-dist-6-0-2.tgz && rm sencha-dist-6-0-2.tgz \  
&& mv Sencha /usr/bin/  
COPY etc/profile.d/sencha.sh /etc/profile.d/sencha.sh  
RUN chmod +x /etc/profile.d/sencha.sh && source /etc/profile.d/sencha.sh  
  

