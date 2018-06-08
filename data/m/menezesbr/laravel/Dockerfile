FROM ubuntu:14.04  
MAINTAINER André Menezes <menezesbr@gmail.com>  
  
# set some environment variables  
ENV APP_NAME app  
ENV APP_EMAIL app@empresa.com  
ENV APP_DOMAIN app.dev  
ENV DEBIAN_FRONTEND noninteractive  
  
# upgrade the container  
RUN apt-get update && \  
apt-get upgrade -y  
  
# install some prerequisites  
RUN apt-get install -y software-properties-common curl build-essential \  
dos2unix gcc git libmcrypt4 libpcre3-dev memcached make python2.7-dev \  
python-pip re2c unattended-upgrades whois vim libnotify-bin nano wget \  
debconf-utils python-software-properties software-properties-common nano zip
unzip p7zip-full  
  
# add some repositories  
RUN apt-add-repository ppa:nginx/stable -y && \  
apt-add-repository ppa:chris-lea/redis-server -y && \  
apt-add-repository ppa:ondrej/php -y && \  
LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php -y && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
add-apt-repository 'deb [arch=amd64,i386,ppc64el]
http://mirror.ufscar.br/mariadb/repo/10.2/ubuntu trusty main' && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - && \  
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >>
/etc/apt/sources.list.d/postgresql.list' && \  
curl -s https://packagecloud.io/gpg.key | apt-key add - && \  
echo "deb http://packages.blackfire.io/debian any main" | tee
/etc/apt/sources.list.d/blackfire.list && \  
curl --silent --location https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get update  
  
# set the locale  
RUN echo "LC_ALL=pt_BR.UTF-8" >> /etc/default/locale && \  
locale-gen pt_BR.UTF-8 && \  
ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime  
  
# setup bash  
COPY .bash_aliases /root  
  
# install nginx  
RUN apt-get install -y --force-yes nginx  
COPY homestead /etc/nginx/sites-available/  
RUN rm -rf /etc/nginx/sites-available/default && \  
rm -rf /etc/nginx/sites-enabled/default && \  
ln -fs "/etc/nginx/sites-available/homestead" "/etc/nginx/sites-
enabled/homestead" && \  
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size
100m/" /etc/nginx/nginx.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf && \  
usermod -u 1000 www-data && \  
chown -Rf www-data.www-data /var/www/html/ && \  
sed -i -e"s/worker_processes 1/worker_processes 5/" /etc/nginx/nginx.conf  
VOLUME ["/var/www/html/app"]  
VOLUME ["/var/cache/nginx"]  
VOLUME ["/var/log/nginx"]  
  
# install php 7  
RUN apt-get install -y --force-yes php7.0-fpm php7.0-cli php7.0-dev
php7.0-pgsql php7.0-sqlite3 php7.0-gd \  
php-apcu php7.0-curl php7.0-mcrypt php7.0-imap php7.0-mysql php7.0-readline
php-xdebug php-common \  
php7.0-mbstring php7.0-xml php7.0-zip php7.0-gmp php7.0-bcmath php7.0-common
php7.0-bcmath php7.0-intl php7.0-gmp  
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php/7.0/cli/php.ini && \  
sed -i "s/display_errors = .*/display_errors = On/" /etc/php/7.0/cli/php.ini
&& \  
sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php/7.0/cli/php.ini && \  
sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php/7.0/fpm/php.ini && \  
sed -i "s/display_errors = .*/display_errors = On/" /etc/php/7.0/fpm/php.ini
&& \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.0/fpm/php.ini &&
\  
sed -i "s/upload_max_filesize = .*/upload_max_filesize = 100M/"
/etc/php/7.0/fpm/php.ini && \  
sed -i "s/post_max_size = .*/post_max_size = 100M/" /etc/php/7.0/fpm/php.ini
&& \  
sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php/7.0/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-
fpm.conf && \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
find /etc/php/7.0/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
COPY fastcgi_params /etc/nginx/  
  
RUN phpenmod mcrypt && \  
mkdir -p /run/php/ && chown -Rf www-data.www-data /run/php  
  
# install php 7.1  
RUN apt-get install -y --force-yes php7.1 php7.1-gmp php7.1-bcmath php7.1-curl
php7.1-xml \  
php7.1-soap php7.1-fpm php7.1-cli php7.1-common php7.1-mbstring php7.1-gd
php7.1-intl \  
php7.1-xml php7.1-mysql php7.1-mcrypt php7.1-zip  
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php/7.1/cli/php.ini && \  
sed -i "s/display_errors = .*/display_errors = On/" /etc/php/7.1/cli/php.ini
&& \  
sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php/7.1/cli/php.ini && \  
sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php/7.1/fpm/php.ini && \  
sed -i "s/display_errors = .*/display_errors = On/" /etc/php/7.1/fpm/php.ini
&& \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.1/fpm/php.ini &&
\  
sed -i "s/upload_max_filesize = .*/upload_max_filesize = 100M/"
/etc/php/7.1/fpm/php.ini && \  
sed -i "s/post_max_size = .*/post_max_size = 100M/" /etc/php/7.1/fpm/php.ini
&& \  
sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php/7.1/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-
fpm.conf && \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
find /etc/php/7.1/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
COPY /php/7.0/cli/php.ini /etc/php/7.0/cli/php.ini  
COPY /php/7.0/fpm/php.ini /etc/php/7.0/fpm/php.ini  
COPY /php/7.1/cli/php.ini /etc/php/7.1/cli/php.ini  
COPY /php/7.1/fpm/php.ini /etc/php/7.1/fpm/php.ini  
  
# install php complementos  
RUN apt-get install --force-yes -y php5.6-xml  
  
# install sqlite  
RUN apt-get install --force-yes -y sqlite3 libsqlite3-dev  
  
# install mysql  
RUN echo mariadb-server mariadb-server/root_password password $DB_PASS |
debconf-set-selections;\  
echo mariadb-server mariadb-server/root_password_again password $DB_PASS |
debconf-set-selections;\  
apt-get install -y mariadb-server && \  
echo "default_password_lifetime = 0" >> /etc/mysql/my.cnf && \  
sed -i '/^bind-address/s/bind-address.*=.*/bind-address = 0.0.0.0/'
/etc/mysql/my.cnf  
  
RUN /etc/init.d/mysql restart  
  
RUN /usr/sbin/mysqld & \  
sleep 10s && \  
echo "GRANT ALL ON *.* TO root@'0.0.0.0' IDENTIFIED BY 'secret' WITH GRANT
OPTION; CREATE USER 'homestead'@'0.0.0.0' IDENTIFIED BY 'secret'; GRANT ALL ON
*.* TO 'homestead'@'0.0.0.0' IDENTIFIED BY 'secret' WITH GRANT OPTION; GRANT
ALL ON *.* TO 'homestead'@'%' IDENTIFIED BY 'secret' WITH GRANT OPTION; FLUSH
PRIVILEGES; CREATE DATABASE homestead;" | mysql  
VOLUME ["/var/lib/mysql"]  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
printf "\nPATH=\"~/.composer/vendor/bin:\$PATH\"\n" | tee -a ~/.bashrc  
  
# install prestissimo  
# RUN composer global require "hirak/prestissimo"  
# install laravel envoy  
RUN composer global require "laravel/envoy"  
  
#install laravel installer  
RUN composer global require "laravel/installer"  
  
# install nodejs  
RUN apt-get install -y nodejs  
  
# install gulp  
RUN /usr/bin/npm install -g gulp  
  
# install bower  
RUN /usr/bin/npm install -g bower  
  
# install redis  
RUN apt-get install -y redis-server  
  
# install blackfire  
RUN apt-get install -y blackfire-agent blackfire-php  
  
# install beanstalkd  
RUN apt-get install -y --force-yes beanstalkd && \  
sed -i "s/BEANSTALKD_LISTEN_ADDR.*/BEANSTALKD_LISTEN_ADDR=0.0.0.0/"
/etc/default/beanstalkd && \  
sed -i "s/#START=yes/START=yes/" /etc/default/beanstalkd && \  
/etc/init.d/beanstalkd start  
  
# install supervisor  
RUN apt-get install -y supervisor && \  
mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
VOLUME ["/var/log/supervisor"]  
  
# clean up our mess  
RUN apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
# expose ports  
EXPOSE 80 443 3306 6379  
# set container entrypoints  
ENTRYPOINT ["/bin/bash","-c"]  
CMD ["/usr/bin/supervisord"]  

