FROM centos:6.8  
  
RUN yum -y update && yum -y install \  
automake \  
autoconf \  
apr \  
apr-util \  
apr-util-devel \  
bzip2 \  
curl \  
curl-devel \  
libcurl \  
libcurl-devel\  
gmp \  
gmp-devel \  
libgmp \  
httpd-devel \  
httpd \  
libtool \  
libxml2 \  
libxml2-devel \  
mod_ssl \  
mysql-devel \  
openssl \  
openssl-devel \  
libjpeg \  
libjpeg-devel \  
libpng \  
libpng-devel \  
mysql-devel \  
readline \  
readline-devel \  
tar \  
wget \  
epel-release \  
vim-enhanced \  
&& yum clean all  
  
# Install dependencies  
RUN mkdir -p /tmp/deps && wget --quiet -P /tmp/deps
ftp://fr2.rpmfind.net/linux/dag/redhat/el6/en/x86_64/dag/RPMS/libmcrypt-2.5.7-1.2.el6.rf.x86_64.rpm
\  
ftp://fr2.rpmfind.net/linux/dag/redhat/el6/en/x86_64/dag/RPMS/libmcrypt-
devel-2.5.7-1.2.el6.rf.x86_64.rpm \  
ftp://mirror.switch.ch/pool/4/mirror/scientificlinux/6.7/x86_64/os/Packages/libtidy-
devel-0.99.0-19.20070615.1.el6.x86_64.rpm \  
ftp://ftp.pbone.net/mirror/ftp.scientificlinux.org/linux/scientific/6rolling/x86_64/os/Packages/libtidy-0.99.0-19.20070615.1.el6.x86_64.rpm
\  
ftp://fr2.rpmfind.net/linux/epel/6/x86_64/mcrypt-2.6.8-10.el6.x86_64.rpm \  
ftp://fr2.rpmfind.net/linux/epel/6/x86_64/mhash-0.9.9.9-3.el6.x86_64.rpm \  
ftp://fr2.rpmfind.net/linux/epel/6/x86_64/mhash-devel-0.9.9.9-3.el6.x86_64.rpm
\  
http://museum.php.net/php5/php-5.2.17.tar.bz2  
  
RUN cd /tmp/deps/ && yum -y install \  
libmcrypt-2.5.7-1.2.el6.rf.x86_64.rpm \  
libmcrypt-devel-2.5.7-1.2.el6.rf.x86_64.rpm \  
libtidy-0.99.0-19.20070615.1.el6.x86_64.rpm \  
libtidy-devel-0.99.0-19.20070615.1.el6.x86_64.rpm \  
mcrypt-2.6.8-3.el6.x86_64.rpm \  
mhash-0.9.9.9-3.el6.x86_64.rpm \  
mhash-devel-0.9.9.9-3.el6.x86_64.rpm \  
&& yum clean all  
  
RUN cd /tmp/deps/ && tar xjf php-5.2.17.tar.bz2  
  
RUN cd /tmp/deps/php-5.2.17 && \  
./configure --prefix=/usr/local/php \  
\--with-apxs2=/usr/sbin/apxs \  
\--with-mysql=/usr/bin \  
\--with-libdir=lib64 \  
\--enable-fastcgi \  
\--with-libxml-dir \  
\--with-openssl \  
\--with-kerberos \  
\--with-zlib \  
\--enable-bcmath \  
\--with-curl \  
\--enable-ftp \  
\--enable-sockets \  
\--with-kerberos \  
\--enable-mbstring \  
\--with-mcrypt \  
\--with-mhash \  
\--with-pear \  
\--with-xmlrpc \  
\--enable-sysvsem \  
\--enable-sysvshm \  
\--enable-sysvmsg \  
\--enable-pcntl \  
\--with-pdo-mysql \  
\--with-readline \  
\--enable-shmop \  
\--enable-soap \  
\--with-tidy \  
\--enable-wddx \  
\--enable-xml \  
\--enable-zip \  
\--with-gd \  
\--with-jpeg-dir \  
\--with-png-dir \  
\--with-mysqli \  
\--with-gmp && make && make install  
  
ADD php_handler.conf /  
RUN sed -i '/LoadModule php5_module/ r php_handler.conf'
/etc/httpd/conf/httpd.conf  
  
ADD citi-fan.repo /etc/yum.repos.d/  
RUN yum install -y curl  
  
ENTRYPOINT service httpd restart && bash  
  
EXPOSE 80 443  
  
MAINTAINER percy.deleon@gmail.com  

