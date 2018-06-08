############################  
# Grab Ubuntu Base Image #  
############################  
FROM ubuntu:xenial  
SHELL ["/bin/bash", "-c"]  
MAINTAINER David Salman  
  
########################  
# Setup Environments #  
########################  
ENV DEBIAN_FRONTEND noninteractive  
ENV SERVER_IP 127.0.0.1  
ENV MYSQL_USER root  
ENV MYSQL_PASSWORD Pacefactory1!  
ENV PHPMYADMIN_USER ubuntu  
ENV PHPMYADMIN_PASSWORD Pacefactory1!  
  
####################################  
# Apache Web Server Installation #  
####################################  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends apt-utils  
RUN apt-get install -y apache2  
  
#################################  
# Configure Apache Web Server #  
#################################  
RUN apt-get install -y iproute2 ufw  
RUN export SERVER_IP=$(ip addr show lo | grep inet | awk '{ print $2; }' | sed
's/\/.*$//')  
RUN echo "ServerName $SERVER_IP" >> etc/apache2/apache2.conf  
  
RUN ufw app list && \  
ufw app info "Apache Full"  
#ufw allow in "Apache Full"  
  
RUN sed -i -e \  
"s/DirectoryIndex index.html index.cgi index.pl index.php index.xhtml
index.htm/DirectoryIndex index.php index.html index.cgi index.pl index.xhtml
index.htm/g" \  
/etc/apache2/mods-enabled/dir.conf  
  
RUN mkdir -p /var/www/PaceFactoryAPI  
RUN chmod -R 755 /var/www  
  
RUN touch /etc/apache2/sites-available/pacefactoryapi.com.conf  
RUN echo -e \  
"<VirtualHost *:80>\n\t\  
ServerAdmin dev@pacefactory.com\n\t\  
ServerName pacefactoryapi.com\n\t\  
ServerAlias www.pacefactoryapi.com\n\t\  
DocumentRoot /var/www/PaceFactoryAPI\n\t\  
ErrorLog ${APACHE_LOG_DIR}/pacefactory-api-error.log\n\t\  
CustomLog ${APACHE_LOG_DIR}/pacefactory-api-access.log combined\n\  
</VirtualHost>" \  
>> /etc/apache2/sites-available/pacefactoryapi.com.conf  
  
RUN a2ensite pacefactoryapi.com.conf  
RUN service apache2 restart  
RUN apachectl configtest  
  
RUN echo -e "$SERVER_IP pacefactoryapi.com" >> /etc/hosts  
  
########################  
# MySQL Installation #  
########################  
RUN echo "deb http://cn.archive.ubuntu.com/ubuntu/ xenial main restricted
universe multiverse" >> /etc/apt/sources.list  
RUN debconf-set-selections <<< "mysql-server mysql-server/root_password
password $MYSQL_PASSWORD"  
RUN debconf-set-selections <<< "mysql-server mysql-server/root_password_again
password $MYSQL_PASSWORD"  
  
SHELL ["/bin/sh", "-c"]  
RUN apt-get update && \  
apt-get -y install mysql-server  
  
##############################  
# Configure MySQL Database #  
##############################  
SHELL ["/bin/bash", "-c"]  
RUN apt-get install -y aptitude && \  
aptitude install -y expect  
RUN SECURE_MYSQL=$(expect -c "\  
spawn mysql_secure_installation \  
expect \"Enter current password for root (enter for none):\" \  
send \"$MYSQL_PASSWORD\r\" \  
expect \"Would you like to setup VALIDATE PASSWORD plugin?\" \  
send \"y\r\" \  
expect \"Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG:\" \  
send \"2\r\" \  
expect \"Change the root password?\" \  
send \"n\r\" \  
expect \"Remove anonymous users?\" \  
send \"y\r\" \  
expect \"Disallow root login remotely?\" \  
send \"y\r\" \  
expect \"Remove test database and access to it?\" \  
send \"y\r\" \  
expect \"Reload privilege tables now?\" \  
send \"y\r\" \  
expect eof\  
")  
RUN echo "$SECURE_MYSQL" && \  
aptitude -y purge expect  
  
########################  
# Enable PHP Modules #  
########################  
RUN apt-get install -y software-properties-common language-pack-en-base  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php  
RUN apt-get update  
RUN apt-get install -y \  
libapache2-mod-php7.0 \  
php7.0 \  
php7.0-fpm \  
php7.0-cli \  
php7.0-mysqlnd \  
php7.0-pgsql \  
php7.0-sqlite3 \  
php7.0-redis \  
php7.0-json \  
php7.0-curl \  
php7.0-zip \  
php7.0-gd \  
php7.0-xml \  
php7.0-mbstring \  
php7.0-mcrypt  
  
RUN phpenmod mcrypt  
RUN phpenmod mbstring  
  
#############################  
# PhpMyAdmin Installation #  
#############################  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:nijel/phpmyadmin  
RUN apt-get update  
RUN debconf-set-selections <<< "phpmyadmin phpmyadmin/reconfigure-webserver
multiselect apache2"  
RUN debconf-set-selections <<< "phpmyadmin phpmyadmin/dbconfig-install boolean
true"  
RUN debconf-set-selections <<< "phpmyadmin phpmyadmin/mysql/admin-pass
password $MYSQL_PASSWORD"  
RUN debconf-set-selections <<< "phpmyadmin phpmyadmin/mysql/app-pass password
$PHPMYADMIN_PASSWORD"  
RUN debconf-set-selections <<< "phpmyadmin phpmyadmin/app-password-confirm
password $PHPMYADMIN_PASSWORD"  
RUN apt-get install -y phpmyadmin  
  
######################  
# Setup PhpMyAdmin #  
######################  
RUN sed -i -e \  
"s/DirectoryIndex index.php/DirectoryIndex index.php\n\tAllowOverride All/g" \  
/etc/apache2/conf-available/phpmyadmin.conf  
  
RUN touch /usr/share/phpmyadmin/.htaccess  
RUN echo -e \  
"AuthType Basic\n\  
AuthName \"Restricted Files\"\n\  
AuthUserFile /etc/phpmyadmin/.htpasswd\n\  
Require valid-user" \  
>> /usr/share/phpmyadmin/.htaccess  
  
RUN htpasswd -bc /etc/phpmyadmin/.htpasswd $PHPMYADMIN_USER
$PHPMYADMIN_PASSWORD  
  
###########################  
# Composer Installation #  
###########################  
RUN apt-get install -y curl && \  
rm -rf /var/lib/apt/lists/* && \  
cd /tmp && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
RUN useradd -c 'ubuntu' -m -d /home/composer -s /bin/bash $PHPMYADMIN_USER  
RUN apt-get remove -y curl  
  
###########################  
# Setup PaceFactoryAPI #  
###########################  
WORKDIR /var/www/PaceFactoryAPI  
USER $PHPMYADMIN_USER  
  
RUN chown -R $USER:$USER /var/www/PaceFactoryAPI  
  
COPY composer.* ./  
CMD composer install && composer update  
COPY . .  
  
####################  
# Image Settings #  
####################  
#EXPOSE 80 443 3306  
#VOLUME ["/var/www/PaceFactoryAPI", "/var/log/mysql", "/var/lib/mysql"]  
  
##########################  
# Launch Micro-Service #  
##########################  
CMD ["service", "apache2", "restart"]

