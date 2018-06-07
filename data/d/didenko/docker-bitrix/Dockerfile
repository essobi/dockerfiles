FROM ubuntu:latest  
MAINTAINER Aleksandr Didenko <aa.didenko@yandex.com>  
  
# Install packages  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor git apache2
libapache2-mod-php5 mysql-server php5-mysql php5-gd php5-mcrypt pwgen wget  
  
RUN a2enmod rewrite  
  
# Add image configuration and scripts  
ADD ./bin/start-apache2.sh /start-apache2.sh  
ADD ./bin/start-mysqld.sh /start-mysqld.sh  
  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
ADD ./etc/mysql/conf.d/my.cnf /etc/mysql/conf.d/my.cnf  
ADD ./etc/supervisord/conf.d/supervisord-apache2.conf
/etc/supervisor/conf.d/supervisord-apache2.conf  
ADD ./etc/supervisord/conf.d/supervisord-mysqld.conf
/etc/supervisor/conf.d/supervisord-mysqld.conf  
  
# Add MySQL utils  
ADD ./bin/import_sql.sh /import_sql.sh  
ADD ./bin/create_db.sh /create_db.sh  
  
RUN chmod 755 /*.sh  
  
# Configure /app folder with sample app  
RUN mkdir -p /app && rm -fr /var/www && ln -s /app /var/www  
  
RUN chmod -R 777 /app  
  
ADD ./etc/apache2/sites-enabled/000-default /etc/apache2/sites-
enabled/000-default  
ADD ./etc/apache2/php5/php.ini /etc/php5/apache2/php.ini  
ADD phpinfo.php /app/phpinfo.php  
  
WORKDIR /app  
RUN wget http://www.1c-bitrix.ru/download/scripts/bitrixsetup.php  
  
EXPOSE 80 3306  
CMD ["/run.sh"]  

