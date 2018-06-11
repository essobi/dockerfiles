# https://github.com/phusion/baseimage-docker  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:latest  
MAINTAINER Sebastien Lavoie <seb@wemakecustom.com>  
  
# Set correct environment variables.  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN locale-gen en_US.UTF-8 fr_CA.UTF-8  
ENV LANG en_US.UTF-8  
RUN echo "America/Montreal" > /etc/timezone && dpkg-reconfigure tzdata  
  
# Ubuntu mirrors  
RUN for i in "" -updates -backports -security; do echo "deb
mirror://mirrors.ubuntu.com/mirrors.txt $(lsb_release -cs)${i} main restricted
universe multiverse"; done > /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y python-software-properties wget  
  
# ElasticSearch  
RUN wget -q -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch |
apt-key add - \  
&& echo "deb http://packages.elasticsearch.org/elasticsearch/1.3/debian stable
main" > /etc/apt/sources.list.d/elasticsearch.list  
  
# PHP Stable  
RUN add-apt-repository -y ppa:ondrej/php5 && add-apt-repository -y
ppa:duggan/composer  
  
# Percona  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A \  
&& echo "deb http://repo.percona.com/apt $(lsb_release -cs) main\ndeb-src
http://repo.percona.com/apt $(lsb_release -cs) main" >
/etc/apt/sources.list.d/percona.list  
  
RUN apt-get update && apt-get dist-upgrade -y  
  
# http://serverfault.com/questions/322400/install-mysql-server-and-set-
password-from-the-command-line  
# /var/lib/dpkg/info/percona-server-server-5.6.config  
RUN echo "percona-server-server-5.6 percona-server-server/root_password
password root\npercona-server-server-5.6 percona-server-
server/root_password_again password root" | debconf-set-selections  
  
RUN apt-get install -y \  
apache2 \  
apache2-mpm-worker \  
aptitude \  
build-essential \  
elasticsearch \  
gettext \  
git \  
imagemagick \  
libapache2-mod-fastcgi \  
linux-headers-generic \  
nodejs-legacy \  
npm \  
percona-server-server-5.6 \  
php-gettext \  
php-pear \  
php5-apcu \  
php5-cli \  
php5-composer \  
php5-curl \  
php5-dev \  
php5-fpm \  
php5-gd \  
php5-gmp \  
php5-imagick \  
php5-intl \  
php5-json \  
php5-mcrypt \  
php5-mysqlnd \  
php5-readline \  
php5-recode \  
php5-sqlite \  
php5-tidy \  
php5-xdebug \  
php5-xsl \  
phpmyadmin \  
phpunit \  
siege \  
subversion \  
unrar \  
unzip \  
vim  
  
RUN wget -nv
https://gist.githubusercontent.com/lavoiesl/6e4de808a291b8665445/raw/php-
extras.ini -O /etc/php5/mods-available/extras.ini  
RUN php5enmod extras  
  
RUN wget -nv https://gist.githubusercontent.com/lavoiesl/3867674/raw/wmc-
clone.sh -O /usr/local/bin/wmc-clone.sh  
RUN chmod +x /usr/local/bin/wmc-clone.sh  
  
RUN wget -nv
https://gist.githubusercontent.com/lavoiesl/2227920/raw/wordpress-change-
url.php -O /usr/local/bin/wordpress-change-url.php  
RUN chmod +x /usr/local/bin/wordpress-change-url.php  
  
# wget -nv https://gist.githubusercontent.com/lavoiesl/3864795/raw/gitconfig
-O /home/wmc/.gitconfig  
RUN wget -nv https://gist.githubusercontent.com/lavoiesl/3864795/raw/gitignore
-O /etc/gitignore  
  
RUN pear -q upgrade pear  
RUN for chan in pear.phpunit.de components.ez.no pear.symfony.com; do pear
list-channels | grep -q "${chan}" || pear -q channel-discover "${chan}"; done  
RUN pear -q install --alldeps phpunit/PHPUnit  
  
EXPOSE 80  
EXPOSE 3306  
## End custom code  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/sbin/my_init"]  

