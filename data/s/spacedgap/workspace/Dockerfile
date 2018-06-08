FROM spacedgap/php:5.6-cli-centos6  
  
# Start as root  
USER root  
  
#  
#--------------------------------------------------------------------------  
# Software's Installation  
#--------------------------------------------------------------------------  
#  
# Install "PHP Extentions", "libraries", "Software's"  
RUN yum -y install \  
## Build Essentials  
autoconf \  
dpkg-dev dpkg \  
file \  
gcc-c++ \  
gcc \  
glibc-devel \  
make \  
pkgconfig \  
re2c \  
## Persitent / Runtime Deps  
ca-certificates \  
curl \  
tar \  
xz \  
openssl \  
wget \  
## Build Essentials Library  
libcurl-devel \  
libedit-devel \  
openssl-devel \  
libxml2-devel \  
libargon2-devel \  
libsodium-devel \  
zlib-devel \  
sqlite-devel \  
## PHP Libraries  
php \  
php-bcmath \  
php-intl \  
php-mcrypt \  
php-pgsql \  
php-sqlite \  
php-pecl-memcached \  
php-opcache \  
php-gd \  
php-devel \  
sudo \  
ack \  
screen \  
tmux \  
git \  
vim \  
nano \  
postgresql  
  
#####################################  
# SSH Keychain:  
#####################################  
  
RUN rpm --import https://wiki.psychotic.ninja/RPM-GPG-KEY-psychotic && \  
rpm -ivh http://packages.psychotic.ninja/6/base/x86_64/RPMS/psychotic-
release-1.0.0-1.el6.psychotic.noarch.rpm && \  
yum --enablerepo=psychotic -y install keychain  
  
#####################################  
# Composer:  
#####################################  
# Install composer and add its bin to the PATH.  
RUN curl -s http://getcomposer.org/installer | php && \  
# echo "export PATH=${PATH}:/var/www/vendor/bin" >> ~/.bashrc && \  
mv composer.phar /usr/local/bin/composer  
  
# Clean up  
RUN yum clean all && \  
rm -rf \  
/var/cache/* \  
/tmp/* \  
/var/tmp/*  
  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
CMD ["/bin/bash"]  

