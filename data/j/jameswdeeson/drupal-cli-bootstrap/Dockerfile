FROM ubuntu:16.04  
RUN apt update && apt install -y language-pack-en-base software-properties-
common python-software-properties  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
4F4EA0AAE5267A6C  
RUN LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php  
  
# maria. from : https://downloads.mariadb.org/mariadb/repositories  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8  
RUN add-apt-repository 'deb [arch=amd64,i386,ppc64el]
http://lon1.mirrors.digitalocean.com/mariadb/repo/10.0/ubuntu xenial main'  
  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
RUN DEBIAN_FRONTEND=noninteractive apt install -y \  
curl \  
mariadb-server \  
mariadb-client \  
php5.6-cli \  
php5.6-zip \  
php5.6-mysql \  
php5.6-gd \  
php5.6-mcrypt \  
php5.6-curl \  
php5.6-sqlite \  
php5.6-xdebug \  
php5.6-xhprof \  
php5.6-mbstring \  
php5.6-simplexml  
  
RUN mkdir -p /var/run/mysqld  
ADD ./mysql-startup.sh /opt/mysql-startup.sh  
RUN chmod u+x /opt/mysql-startup.sh  
  
RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV MYSQL_ROOT_PASSWORD root  
ENV PATH "/vendor/bin:$PATH"  
ENV HOME "/"  
# this seemed to be required. Although it worked without for a bit.  
ENV PHP_OPTIONS " -d pcre.recursion_limit=10000 "  
RUN curl -LO http://getcomposer.org/composer.phar && \  
mv composer.phar /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer && \  
composer require drush/drush:7.* && \  
composer require phpunit/phpunit:5.*  
  
ADD ./drupal-build.sh /opt/drupal-build.sh  
RUN chmod u+x /opt/drupal-build.sh  
  

