FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get -y install php5 apache2 php5-mysql mysql-server mysql-client wget  
  
RUN wget http://wordpress.org/latest.tar.gz && \  
  
tar xzvf latest.tar.gz && \  
  
cp -R ./wordpress/* /var/www/html && \  
  
rm /var/www/html/index.html  
  
  
RUN touch /var/www/html/wp-config.php  
  
RUN cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.php  
  
EXPOSE 80  
CMD  

