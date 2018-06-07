FROM ubuntu:16.04  
MAINTAINER Apuroop Naidu <apuroop.naidu@gmail.com>  
  
#Setting up the environment variable.  
ENV DEBIAN_FRONTEND noninteractive  
  
#Updating and Installing resources.  
RUN apt-get -y update && apt-get install -y apt-utils \  
vim \  
sed \  
netcat-openbsd  
  
#Installing Apache2.  
RUN apt-get -y install apache2  
  
#Installing MySQL-5.7.  
RUN apt-get -y install -y mysql-server-5.7  
#Installing PHP7.0 and dependencies.  
RUN apt-get install -y \  
php7.0 \  
7.0-bz2 \  
php7.0-cgi \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-dev \  
php7.0-enchant \  
php7.0-fpm \  
php7.0-gd \  
php7.0-gmp \  
php7.0-imap \  
php7.0-interbase \  
php7.0-intl \  
php7.0-json \  
php7.0-ldap \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-odbc \  
php7.0-opcache \  
php7.0-pgsql \  
php7.0-phpdbg \  
php7.0-pspell \  
php7.0-readline \  
php7.0-recode \  
php7.0-snmp \  
php7.0-sqlite3 \  
php7.0-sybase \  
php7.0-tidy \  
php7.0-xmlrpc \  
php7.0-xsl \  
libapache2-mod-php7.0  
#Installing phpMyAdmin; Selecting dbconfig to set up a database and apache2
for the server-selection.  
RUN echo 'phpmyadmin phpmyadmin/dbconfig-install boolean true' | debconf-set-
selections && \  
echo 'phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2' |
debconf-set-selections && \  
apt-get -y install phpmyadmin --no-install-recommends  
  
#Copying the essentials folder to the filesystem of the image.  
COPY /essentials /essentials  
  
#Making directories; Copying files; Giving permissions.  
RUN phpenmod mcrypt && phpenmod mbstring && \  
mkdir -m777 /etc/tpch/ && \  
mkdir -p /var/run/mysqld && \  
touch /var/run/mysqld/mysqld.sock && \  
cp /essentials/index.php /var/www/html/ && \  
cp /essentials/my.cnf /etc/mysql/conf.d/my.cnf && \  
cp /essentials/run.sh /usr/local/bin/run.sh && \  
ln -s /usr/share/phpmyadmin /var/www/phpmyadmin && \  
chmod +x /usr/local/bin/run.sh && \  
chmod +x /essentials/*.sh && \  
chown -R www-data:www-data /var/www/html && \  
chown mysql:mysql /var/run/mysqld && \  
usermod -d /var/lib/mysql/ mysql && \  
apt-get clean  
  
#Copying the TPC-H_SQL folder to the destination in the filesystem of the
image.  
COPY TPC-H_SQL /etc/tpch/  
#Creating volume directories in the image filesystem, can later be used for
mounting volumes from the host or other containers.  
VOLUME ["/var/lib/mysql", "/etc/mysql"]  
  
#Exposing the network ports 80-tcp and 3306-mysql for communication.  
EXPOSE 80 3306  
#Running the command in shell.  
CMD /usr/local/bin/run.sh  

