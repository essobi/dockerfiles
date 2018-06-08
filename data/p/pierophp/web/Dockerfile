FROM ubuntu:16.04  
MAINTAINER "Piero Giusti <pierophp@gmail.com>"  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# Upgrade  
RUN apt update && \  
apt upgrade -y && \  
apt clean && rm -rf /var/lib/apt/lists/*  
  
# Tools  
RUN apt update && \  
apt install -y wget curl vim nano less unzip git mlocate && \  
apt clean && rm -rf /var/lib/apt/lists/*  
  
#Add user  
RUN useradd -ms /bin/bash dev -G sudo,ssh && echo 'dev:123' | chpasswd  
  
# Nginx  
# Nginx  
RUN apt-get update && \  
apt-get install -y nginx && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN unlink /etc/nginx/sites-enabled/default  
ADD nginx/default /etc/nginx/sites-enabled/default  
RUN chown -R www-data:www-data /var/www/  
  
RUN chown -R dev:dev /var/www/  
  
# MySql  
RUN apt-get update && \  
echo "mysql-server mysql-server/root_password password" | debconf-set-
selections && \  
echo "mysql-server mysql-server/root_password_again password" | debconf-set-
selections && \  
apt-get install -y mysql-server && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN sed -i 's/^key_buffer\s*=/key_buffer_size =/' /etc/mysql/my.cnf  
RUN chown -R mysql:mysql /var/lib/mysql  
  
# PHPMyAdmin  
ENV VERSION 4.5.1  
RUN mkdir -p /var/www/phpmyadmin && \  
cd /var/www/phpmyadmin && \  
wget
"https://files.phpmyadmin.net/phpMyAdmin/${VERSION}/phpMyAdmin-${VERSION}-all-
languages.zip" && \  
unzip phpMyAdmin-${VERSION}-all-languages.zip && \  
mv phpMyAdmin-${VERSION}-all-languages/* /var/www/phpmyadmin && \  
rm -rf phpMyAdmin-${VERSION}-all-languages/ && \  
rm -rf phpMyAdmin-${VERSION}-all-languages.zip && \  
rm -rf *.md .coveralls.yml ChangeLog composer.json config.sample.inc.php DCO
doc examples phpunit.* README RELEASE-DATE-* setup  
ADD phpmyadmin/config.inc.php /var/www/phpmyadmin/  
  
# Supervisor  
RUN apt-get update && \  
apt-get install -y supervisor && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ADD supervisor/php-fpm.conf /etc/supervisor/conf.d/php-fpm.conf  
ADD supervisor/nginx.conf /etc/supervisor/conf.d/nginx.conf  
ADD supervisor/mysql.conf /etc/supervisor/conf.d/mysql.conf  
  
RUN apt update && \  
apt install -y php7.0-fpm php7.0-cli php7.0-gd php7.0-mcrypt php7.0-mysql
php7.0-curl php7.0-intl php7.0-json php7.0-xml php7.0-mbstring php7.0-zip
php7.0-dev && \  
apt clean && rm -rf /var/lib/apt/lists/* && \  
unlink /etc/php/7.0/fpm/pool.d/www.conf && \  
unlink /etc/php/7.0/cli/php.ini && \  
unlink /etc/php/7.0/fpm/php.ini  
  
ADD php/fpm.conf /etc/php/7.0/fpm/pool.d/fpm.conf  
ADD php/php.ini /etc/php/7.0/fpm/php.ini  
ADD php/php.ini /etc/php/7.0/cli/php.ini  
  
#PHP Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN mkdir /var/log/php/ && \  
touch /var/log/php/fpm.log && \  
chown www-data:www-data /var/log/php/fpm.log && \  
mkdir /tmp/sessions && \  
chown -R dev:dev /tmp/sessions && \  
chmod 777 -R /tmp/sessions  
  
#PHPRedis  
RUN cd /tmp && \  
git clone -b php7 https://github.com/phpredis/phpredis.git && \  
cd /tmp/phpredis && \  
phpize && \  
./configure && \  
make && make install && \  
rm -Rf /tmp/phpredis  
  
#Update locate  
RUN updatedb  
  
WORKDIR /var/www/  
  
EXPOSE 80  
EXPOSE 3306  
CMD ["/usr/bin/supervisord", "--nodaemon", "-c",
"/etc/supervisor/supervisord.conf"]  

