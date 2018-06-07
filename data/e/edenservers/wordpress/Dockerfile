FROM ubuntu:14.04  
MAINTAINER EdenServers  
  
#Install LAMP  
RUN apt-get -y update  
RUN apt-get -y install apache2 libapache2-mod-php5 php5 php5-mysql mysql-
server wget curl unzip  
  
#Delete index.html  
RUN rm /var/www/html/*  
  
#Download Wordpress  
RUN wget "https://wordpress.org/latest.zip" && \  
unzip latest.zip && \  
mv wordpress/* /var/www/html/ && \  
rm -Rf wordpress && \  
rm latest.zip  
  
# Apache CHOWN  
RUN chown -R www-data:www-data /var/www/html  
  
#Add configuration scripts  
ADD wp-config.php /var/www/html/wp-config.php  
ADD mysql_config.sh /mysql_config.sh  
ADD apache_config.sh /apache_config.sh  
ADD start.sh /start.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 80  
VOLUME ["/var/lib/mysql", "/var/www/html"]  
CMD ["/start.sh"]  

