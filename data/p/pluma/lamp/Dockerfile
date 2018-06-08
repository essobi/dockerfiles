FROM ubuntu:precise  
MAINTAINER Alan Plum <me@pluma.io>  
  
# Install packages  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install
supervisor apache2 libapache2-mod-php5 mysql-server php5-mysql  
  
# Add image configuration and scripts  
ADD start-apache2.sh /start-apache2.sh  
ADD start-mysqld.sh /start-mysqld.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
  
# config to enable .htaccess  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
# Add volumes for MySQL and Apache  
VOLUME ["/var/www", "/var/lib/mysql" ]  
  
EXPOSE 80 3306  
CMD ["/run.sh"]  

