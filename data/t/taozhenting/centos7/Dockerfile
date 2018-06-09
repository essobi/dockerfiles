FROM centos:latest  
MAINTAINER tom.tao  
COPY ./mysql57-community-release-el7-11.noarch.rpm /usr/local/src/  
COPY ./epel-release-latest-7.noarch.rpm /usr/local/src/  
RUN rpm -ivh /usr/local/src/epel-release-latest-7.noarch.rpm  
RUN rpm -ivh /usr/local/src/mysql57-community-release-el7-11.noarch.rpm  
RUN yum install -y openssh-server openssh-clients net-tools traceroute telnet
sudo mysql-community-client  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
RUN echo 'root:tom123' | chpasswd  
RUN systemctl enable sshd  
COPY ./php-7.2.1.tar.gz /usr/local/src/  
RUN yum install -y nginx gcc make apr-devel apr-util-devel pcre-devel
libxml2-devel curl-devel gd-devel openssl-devel autoconf libjpeg-devel libpng-
devel libxslt-devel  
WORKDIR /usr/local/src/  
RUN tar zxvf php-7.2.1.tar.gz  
WORKDIR php-7.2.1  
RUN ./configure \  
\--prefix=/opt/php7.2.1 \  
\--with-curl \  
\--with-freetype-dir \  
\--with-gd \  
\--with-gettext \  
\--with-iconv-dir \  
\--with-kerberos \  
\--with-libdir=lib64 \  
\--with-libxml-dir \  
\--with-mysqli \  
\--with-openssl \  
\--with-pcre-regex \  
\--with-pdo-mysql \  
\--with-pdo-sqlite \  
\--with-pear \  
\--with-png-dir \  
\--with-xmlrpc \  
\--with-xsl \  
\--with-zlib \  
\--enable-fpm \  
\--enable-bcmath \  
\--enable-libxml \  
\--enable-inline-optimization \  
\--enable-gd-native-ttf \  
\--enable-mbregex \  
\--enable-mbstring \  
\--enable-opcache \  
\--enable-pcntl \  
\--enable-shmop \  
\--enable-soap \  
\--enable-sockets \  
\--enable-sysvsem \  
\--enable-xml \  
\--enable-zip \  
\--with-jpeg-dir  
RUN make && make install  
COPY ./php.ini /opt/php7.2.1/lib/php.ini  
COPY ./php-fpm.conf /opt/php7.2.1/etc/php-fpm.conf  
COPY ./www.conf /opt/php7.2.1/etc/php-fpm.d/  
RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak  
COPY ./nginx.conf /etc/nginx/  
COPY ./test.php /usr/share/nginx/html/  
RUN cp /usr/local/src/php-7.2.1/sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm  
RUN chmod +x /etc/init.d/php-fpm  
RUN chkconfig --add php-fpm  
RUN chkconfig php-fpm on  
RUN /etc/init.d/php-fpm start  
RUN systemctl enable nginx  

