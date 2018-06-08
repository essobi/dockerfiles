FROM centos:centos6  
MAINTAINER pepechoko  
  
RUN yum update -y && \  
yum clean all  
  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm && \  
yum clean all  
  
RUN yum install -y --enablerepo=epel \  
re2c \  
libmcrypt \  
libmcrypt-devel && \  
yum clean all  
  
RUN yum install -y \  
ksh \  
bison \  
bison-devel \  
bzip2-devel \  
curl-devel \  
enchant-devel \  
freetype-devel \  
gcc \  
git \  
gmp-devel \  
httpd \  
httpd-devel \  
libXpm \  
libXpm-devel \  
libc-client-devel \  
libcurl-devel \  
libicu-devel \  
libjpeg-turbo-devel \  
libpng-devel \  
libtidy-devel \  
libtool-ltdl-devel \  
libxml2 \  
libxml2-devel \  
libxslt-devel \  
net-snmp \  
net-snmp-devel \  
oniguruma-devel \  
openssl-devel \  
readline-devel \  
sudo \  
t1lib \  
t1lib-devel \  
which \  
tar \  
bzip2 \  
wget && \  
yum clean all  
  
## add phpenv group  
RUN groupadd phpenv  
  
# Install PHPenv  
# git clone git://github.com/phpenv/phpenv.git && \  
ENV PHPENV_ROOT /usr/local/phpenv  
RUN \  
cd /usr/local && \  
curl -L https://raw.github.com/CHH/phpenv/master/bin/phpenv-install.sh | sh &&
\  
chgrp -R phpenv /usr/local/phpenv && \  
chmod -R g+rwxXs /usr/local/phpenv && \  
cd /usr/local/phpenv && \  
git reset --hard origin/master && \  
exec $SHELL && \  
/usr/local/phpenv/bin/phpenv rehash  
  
# install PHP-build  
RUN \  
mkdir /usr/local/phpenv/plugins && \  
cd /usr/local/phpenv/plugins && \  
git clone https://github.com/CHH/php-build.git && \  
chgrp -R phpenv /usr/local/phpenv/plugins/php-build && \  
chmod -R g+rwxXs /usr/local/phpenv/plugins/php-build  
  
# install phpenv-apache-version  
RUN \  
cd /usr/local/phpenv/plugins && \  
git clone https://github.com/garamon/phpenv-apache-version && \  
chgrp -R phpenv /usr/local/phpenv/plugins/phpenv-apache-version && \  
chmod -R g+rwxXs /usr/local/phpenv/plugins/phpenv-apache-version  
  
# install phpenv-composer  
RUN \  
cd /usr/local/phpenv/plugins && \  
git clone https://github.com/ngyuki/phpenv-composer.git && \  
chgrp -R phpenv /usr/local/phpenv/plugins/phpenv-composer && \  
chmod -R g+rwxXs /usr/local/phpenv/plugins/phpenv-composer  
  
##  
# Complete ENV  
ENV PHPENV_ROOT /usr/local/phpenv  
ENV PATH /usr/local/phpenv/bin:/usr/local/phpenv/shims:$PATH  
ADD phpenv.sh /etc/profile.d/phpenv.sh  
RUN chmod +x /etc/profile.d/phpenv.sh  
RUN eval "(phpenv init -)"  
RUN chgrp -R phpenv /usr/local/phpenv  
RUN chmod -R g+rwxXs /usr/local/phpenv  
  
# Install multiple versions of php  
# RUN perl -i -pe 's/--enable-fpm\n//g' /usr/local/phpenv/plugins/php-
build/share/php-build/default_configure_options  
# RUN sed -i -e '$s/--with-apxs2\n//g' /usr/local/phpenv/plugins/php-
build/share/php-build/default_configure_options  
  
ADD versions.txt /usr/local/phpenv/versions.txt  
RUN xargs -L 1 -i ksh -c ' \  
sed -i "1s/^/configure_option -D --enable-fpm\n/"
/usr/local/phpenv/plugins/php-build/share/php-build/definitions/{}; \  
sed -i "1s/^/configure_option --disable-fpm\n/" /usr/local/phpenv/plugins/php-
build/share/php-build/definitions/{}; \  
sed -i "1s/^/configure_option --with-apxs2=\/usr\/sbin\/apxs\n/"
/usr/local/phpenv/plugins/php-build/share/php-build/definitions/{}; \  
' < /usr/local/phpenv/versions.txt  
  
RUN xargs -L 1 -i ksh -c ' \  
/usr/local/phpenv/plugins/php-build/bin/php-build {}
/usr/local/phpenv/versions/{}; \  
mv /etc/httpd/modules/libphp5.so /usr/local/phpenv/versions/{}/ \  
' < /usr/local/phpenv/versions.txt  
  
# settgin global use PHP  
ADD global_version.txt /usr/local/phpenv/global_version.txt  
RUN \  
phpenv global `cat /usr/local/phpenv/global_version.txt` && \  
phpenv rehash  
  

