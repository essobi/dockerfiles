FROM centos:7.0.1406  
MAINTAINER Tais P. Hansen <tph@casalogic.dk>  
  
# CentOS  
RUN yum clean all && yum -y swap fakesystemd systemd  
RUN yum -y groupinstall "Development Tools"  
  
# PHP 5.6  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
RUN yum -y install php56w-cli php56w-devel php56w-pear php56w-soap php56w-imap
php56w-intl php56w-mbstring php56w-mcrypt php56w-pdo  
  
# Mongo PHP driver  
RUN yum -y install cyrus-sasl-devel openssl-devel  
RUN pecl install mongodb  
RUN echo "extension=mongodb.so" > /etc/php.d/mongodb.ini  
  
# NPM  
RUN yum -y install npm  
  
# Bower  
RUN npm install -q -g bower grunt-cli  
RUN cd $HOME && mkdir -p .cache/bower && ln -s /var/cache/bower .cache/bower  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin  
RUN cd /usr/local/bin && ln -s composer.phar composer  
RUN cd $HOME && mkdir -p .composer/cache  

