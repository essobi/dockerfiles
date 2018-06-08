FROM ubuntu:14.04  
  
ADD fs/ /  
  
MAINTAINER Francisco Giana <gianafrancisco@gmail.com>  
  
RUN apt-get update && \  
apt-get -y install libmysqlclient18 libpq5 php5-common php5-gd php-pear php-db
libapache2-mod-php5 php-mail apache2 php5-mysql && \  
cd /opt/ && tar -zxvf freeradius.tgz && ldconfig && \  
mv -f radiusd.conf freeradius/etc/raddb/ && \  
mv -f default freeradius/etc/raddb/sites-available/ && \  
rm -f /etc/apache2/sites-available/000-default.conf && \  
rm -f freeradius.tgz && \  
mv /etc/apache2/sites-available/000-default.conf.daloradius
/etc/apache2/sites-available/000-default.conf && \  
cd /var/www/ && tar -zxvf daloradius-0.9-9.tar.gz && mv daloradius-0.9-9
daloradius && \  
mv -f daloradius.conf.php daloradius/library/ && \  
rm -f daloradius-0.9-9.tar.gz && \  
chown www-data.www-data -R daloradius  
RUN echo "mysql-server mysql-server/root_password password toor" | debconf-
set-selections && \  
echo "mysql-server mysql-server/root_password_again password toor" | debconf-
set-selections && \  
apt-get -y install mysql-server && sh /mysqlSchema.sh  
  
EXPOSE 1812 1813 80  
  
ENTRYPOINT /init.sh  

