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
  
#Config sudo  
#RUN sed -i s/ALL$/NOPASSWD:ALL/g /etc/sudoers  
#Add user  
RUN useradd -ms /bin/bash handview -G sudo,ssh && echo 'handview:123' |
chpasswd  
  
# PHP  
RUN apt update && \  
apt install -y php7.0-fpm php7.0-cli php7.0-gd php7.0-mcrypt php7.0-mysql
php7.0-curl php7.0-intl php7.0-json php7.0-xml php7.0-mbstring php7.0-zip && \  
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
  
RUN echo 'error_log=/var/log/php/fpm.log' >> /etc/php/7.0/fpm/php.ini && \  
echo 'error_log=/var/log/php/cli.log' >> /etc/php/7.0/cli/php.ini && \  
mkdir /var/log/php/ && \  
touch /var/log/php/cli.log /var/log/php/fpm.log && \  
chown www-data:www-data /var/log/php/fpm.log /var/log/php/cli.log  
  
# Nginx  
RUN apt-get update && \  
apt-get install -y nginx && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN unlink /etc/nginx/sites-enabled/default  
ADD nginx/default /etc/nginx/sites-enabled/default  
RUN chown -R www-data:www-data /var/www/  
  
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
  
# SSHD  
RUN apt-get update && \  
apt-get install -y openssh-client openssh-server && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' |chpasswd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
# PHPMyAdmin  
ENV VERSION 4.5.5.1  
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
ADD nginx/config.inc.php /var/www/phpmyadmin/  
  
# Avconv && Mp4v2 && DVDAuthor  
RUN apt-get update && \  
apt-get install -y libav-tools mp4v2-utils dvdauthor && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Supervisor  
RUN apt-get update && \  
apt-get install -y supervisor && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
ADD supervisor/php5-fpm.conf /etc/supervisor/conf.d/php5-fpm.conf  
ADD supervisor/nginx.conf /etc/supervisor/conf.d/nginx.conf  
ADD supervisor/mysql.conf /etc/supervisor/conf.d/mysql.conf  
ADD supervisor/sshd.conf /etc/supervisor/conf.d/sshd.conf  
#Update locate  
RUN updatedb  
  
WORKDIR /var/www/handview/  
  
# isso faz que nao seja comitado  
# VOLUME /var/www/  
# VOLUME /var/lib/mysql/  
EXPOSE 80  
EXPOSE 22  
EXPOSE 3306  
CMD ["/usr/bin/supervisord", "--nodaemon", "-c",
"/etc/supervisor/supervisord.conf"]  

