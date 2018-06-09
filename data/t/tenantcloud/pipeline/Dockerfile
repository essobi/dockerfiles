FROM ubuntu:16.04  
  
MAINTAINER Igor Bronovskyi <admin@brun.if.ua>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \--force-yes software-properties-common \  
&& apt-add-repository ppa:nginx/development -y \  
&& apt-add-repository ppa:chris-lea/redis-server -y \  
&& LC_ALL=C.UTF-8 apt-add-repository ppa:ondrej/apache2 -y \  
&& LC_ALL=C.UTF-8 apt-add-repository ppa:ondrej/php -y \  
&& apt-get update \  
&& apt-get install -y \--force-yes build-essential curl gcc git libmcrypt4
libpcre3-dev \  
make python2.7 python-pip sendmail supervisor unattended-upgrades unzip whois
redis-server \  
ruby-dev libsqlite3-dev libxrender1 \  
&& apt-get install -y \--force-yes php7.1-cli php7.1-dev \  
php7.1-pgsql php7.1-sqlite3 php7.1-gd \  
php7.1-curl php7.1-memcached \  
php7.1-imap php7.1-mysql php7.1-mbstring \  
php7.1-xml php7.1-imagick php7.1-zip php7.1-bcmath php7.1-soap \  
php7.1-intl php7.1-readline php7.1-mcrypt php7.1-fpm \  
&& curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer \  
&& curl --silent \--location https://deb.nodesource.com/setup_8.x | bash - \  
&& gem install mailcatcher \  
&& apt-get update && apt-get install -y \--force-yes nodejs \  
&& echo "mysql-server mysql-server/root_password password root" | debconf-set-
selections \  
&& echo "mysql-server mysql-server/root_password_again password root" |
debconf-set-selections \  
&& apt-get install -y mysql-server \  
&& sed -i '/^bind-address/s/bind-address.*=.*/bind-address = */'
/etc/mysql/mysql.conf.d/mysqld.cnf \  
&& service mysql start \  
&& mysql -uroot -proot -e "GRANT ALL ON *.* TO root@'%' IDENTIFIED BY 'root';"
\  
&& apt-get autoclean && apt-get clean && apt-get autoremove \  
&& rm -rf /root/.npm /root/.composer /tmp/* /var/lib/apt/lists/*  
  

