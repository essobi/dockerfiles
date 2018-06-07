FROM ubuntu:16.04  
  
RUN echo "mysql-server mysql-server/root_password password nmm-secret" |
debconf-set-selections && \  
echo "mysql-server mysql-server/root_password_again password nmm-secret" |
debconf-set-selections && \  
apt-get update && apt-get -y install apache2 \  
php mysql-server \  
php php-cli libapache2-mod-php \  
php-mbstring php-pdo-mysql php-gmp \  
php-json php-gettext php-gd \  
git \  
wget htop vim nano joe net-tools iputils-ping traceroute socat mtr host iperf3
curl iproute2 tcpdump telnet  
  
RUN git clone https://github.com/phpipam/phpipam.git /var/www/phpipam/  
  
RUN cd /var/www/phpipam && git checkout 1.3 && git submodule update --init
--recursive  
  
RUN service mysql start && \  
echo "create database phpipam;\nGRANT ALL on phpipam.* to phpipam@localhost
identified by 'phpipamadmin';\nexit" | mysql -u root -pnmm-secret && \  
mysql -u root -pnmm-secret phpipam < /var/www/phpipam/db/SCHEMA.sql && \  
echo "update users set password =
'\$6\$rounds=3000\$e4N4k3JEMTGVqRtw\$9FRviyr/K.Z1.ROJCftjErq9eoizVS.dcoBOgJmHMk72bs9wswhu/qr/.4it9BsRNIWd5Agb8abthZLhSJLET/'
where username = 'Admin'" | mysql -u root -pnmm-secret phpipam && \  
echo "update users set passChange = 'No' where username = 'Admin';" | mysql -u
root -pnmm-secret phpipam  
  
RUN echo "Alias /phpipam /var/www/phpipam/" >/etc/apache2/sites-
available/phpipam.conf && \  
a2ensite phpipam && \  
a2enmod rewrite && \  
service apache2 restart && \  
cp /var/www/phpipam/config.dist.php /var/www/phpipam/config.php && \  
sed -i.bak "s/define('BASE', \"\/\"/define('BASE', \"\/phpipam\/\"/g"
/var/www/phpipam/config.php  
  
ADD start-services.sh /root/start-services.sh  
RUN chmod +x /root/start-services.sh  
  
CMD /root/start-services.sh  
  
VOLUME /root /var/lib/mysql  

