# cloned from https://hub.docker.com/r/x4j5/silverstripe-lamp/~/dockerfile/  
FROM nodesource/jessie:6.3.0  
MAINTAINER Simon Winter <simon@saltedherring.com>  
  
### SET UP  
ENV DEBIAN_FRONTEND=noninteractive  
  
# BASE jessie-backports O/S with some helpful tools  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >>
/etc/apt/sources.list  
RUN apt-get -qq update && \  
apt-get -qqy install sudo wget lynx telnet nano curl make git-core locales vim
\  
&& apt-get clean  
  
# Local settings for local people don't touch the things! :)  
RUN echo "LANG=en_NZ.UTF-8\n" > /etc/default/locale && \  
echo "en_NZ.UTF-8 UTF-8\n" > /etc/locale.gen && \  
locale-gen  
  
# MARIADB  
RUN apt-get -yqq install mariadb-server && \  
sed -i 's/^\\(bind-address\s.*\\)/# \1/' /etc/mysql/my.cnf && \  
echo "mysqld_safe &" > /tmp/config && \  
echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \  
echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" WITH GRANT
OPTION;'" >> /tmp/config && \  
bash /tmp/config && \  
rm -f /tmp/config && \  
apt-get clean  
  
# ADD php7.0 deb  
RUN echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list
&& \  
echo 'deb-src http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list
&& \  
cd /tmp && \  
wget https://www.dotdeb.org/dotdeb.gpg && \  
apt-key add dotdeb.gpg && \  
rm dotdeb.gpg && \  
apt-get update  
  
# APACHE, PHP & SUPPORT TOOLS  
RUN apt-get -yqq install apache2 \  
php7.0-sqlite3 php7.0-imagick \  
php7.0-cli libapache2-mod-php7.0 php7.0-mysql php7.0-mcrypt php7.0-tidy
php7.0-curl \  
php7.0-gd php7.0-xml php7.0-mbstring zip unzip php7.0-zip php7.0-intl php-pear
\  
jpegoptim optipng && \  
apt-get clean  
  
RUN a2enmod headers  
  
# - Phpunit, Composer, Phing  
RUN wget https://phar.phpunit.de/phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit && \  
wget https://getcomposer.org/composer.phar && \  
chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/composer && \  
pear channel-discover pear.phing.info && \  
pear install phing/phing  
  
RUN composer self-update  
  
# add codesniffer  
RUN composer global require "squizlabs/php_codesniffer=*"  
  
# add silverstripe 4 upgrader  
RUN composer global require "silverstripe/upgrader"  
  
# SilverStripe Apache Configuration  
RUN rm /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite && \  
if [ -f /var/www/index.html]; then rm /var/www/index.html; fi  
  
RUN echo "date.timezone = Pacific/Auckland" >> /etc/php/7.0/apache2/php.ini  
  
ADD startup /usr/local/bin/startup  
ADD apache-default-vhost /etc/apache2/sites-available/000-default.conf  
  
# add public dir  
RUN if ! [ -d /var/www/public ]; then mkdir /var/www/public; fi  
  
# update node  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs  
  
# Install node apps  
RUN npm install -g grunt-cli gulp bower npm  
  
####  
## Commands and ports  
EXPOSE 80  
# Run apache in foreground mode  
RUN chmod 755 /usr/local/bin/startup  
WORKDIR /var/www  
  
CMD ["/usr/local/bin/startup"]  
  
ENV LANG en_GB.UTF-8  

