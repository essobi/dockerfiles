FROM ubuntu:trusty  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y install supervisor git apache2 libapache2-mod-php5 mysql-server
php5-mysql pwgen php-apc php5-mcrypt wget && \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
RUN apt-get upgrade -q -y ;\  
apt-get install -q -y curl php5-gd php5-ldap php5-imap; apt-get clean ; \  
php5enmod imap  
  
# Add image configuration and scripts  
ADD start-apache2.sh /start-apache2.sh  
ADD start-mysqld.sh /start-mysqld.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
# Add MySQL utils  
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh  
RUN chmod 755 /*.sh  
  
# config to enable .htaccess  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
#Environment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
# Add volumes for MySQL  
VOLUME ["/etc/mysql", "/var/lib/mysql" ]  
  
RUN rm -rf /app  
  
RUN wget https://www.limesurvey.org/stable-
release?download=1908:limesurvey2551%20161026targz -O limesurvey.tar.gz  
RUN tar -xvzf limesurvey.tar.gz  
  
RUN mkdir -p /uploadstruct; \  
cp -r /limesurvey/upload/* /uploadstruct ; \  
chown -R www-data:www-data /uploadstruct  
  
RUN mv limesurvey/ /var/www/html/limesurvey/; \  
chown www-data:www-data -R /var/www/html/limesurvey  
  
RUN chown www-data:www-data /var/lib/php5  
  
ADD start.sh /  
  
RUN chmod +x /start.sh  
  
VOLUME /app/upload  
  
EXPOSE 80 587 3306  
CMD ["/start.sh"]  

