FROM ubuntu  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install lamp-server^  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install wget supervisor  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install unzip pwgen  
  
RUN DEBIAN_FRONTEND=noninteractive sudo apt-get -y install mcrypt php5-mcrypt
curl php5-curl php5-gd  
  
RUN DEBIAN_FRONTEND=noninteractive php5enmod mcrypt  
ADD adminer.php /var/www/html/magento/  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
ADD start-apache2.sh /start-apache2.sh  
ADD start-mysqld.sh /start-mysqld.sh  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh  
RUN chmod 755 /*.sh  
RUN rm -rf /var/lib/mysql/*  
  
EXPOSE 80  
EXPOSE 3306  
ADD magento.zip /var/www/html/  
  
RUN cd /var/www/html && unzip magento.zip  
  
RUN cd /var/www/html && chown -R www-data:www-data magento  
  
ADD startupscript.sh /var/www/startupscript.sh  
  
RUN chmod 755 /var/www/*.sh  
  
CMD ["/var/www/startupscript.sh"]  

