FROM ubuntu:14.04  
MAINTAINER Loading <dxf351@gmail.com>  
  
RUN echo "deb http://cn.archive.ubuntu.com/ubuntu/ trusty main restricted
universe multiverse" > /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -yq --force-yes install openssh-server openssh-client mysql-server
supervisor rsync  
RUN /etc/init.d/mysql start &&\  
mysql -e "grant all privileges on *.* to 'root'@'%' identified by 'root';"&&\  
mysql -e "grant all privileges on *.* to 'root'@'localhost' identified by
'root';"&&\  
mysql -u root -proot -e "create database wordpress;"  
  
RUN sed -i "s/127.0.0.1/0.0.0.0/g" /etc/mysql/my.cnf  
  
RUN apt-get install -yq --force-yes apache2 php5 libapache2-mod-php5 php5-gd
php5-curl libssh2-php php5-mysql  
  
RUN sed -i "s/expose_php\ \=\ On/expose_php\ \=\ Off/g"
/etc/php5/apache2/php.ini  
RUN sed -i "s/allow_url_fopen\ \=\ On/allow_url_fopen\ \=\ Off/g"
/etc/php5/apache2/php.ini  
  
RUN sudo a2enmod rewrite  
  
RUN echo "LoadModule php5_module /usr/lib/apache2/modules/libphp5.so" >>
/etc/apache2/apache2.conf  
RUN echo "AddType application/x-httpd-php .php" >> /etc/apache2/apache2.conf  
RUN echo "AddType application/x-httpd-php-source .phps" >>
/etc/apache2/apache2.conf  
  
RUN wget http://wordpress.org/latest.tar.gz  
RUN tar xzvf latest.tar.gz wordpress  
RUN cd wordpress  
  
#RUN sudo rsync -avz . /var/www/html  
RUN cp -r wordpress/* /var/www/html  
RUN cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.php  
  
RUN sed -i "s/database_name_here/wordpress/g" /var/www/html/wp-config.php  
RUN sed -i "s/username_here/root/g" /var/www/html/wp-config.php  
RUN sed -i "s/password_here/root/g" /var/www/html/wp-config.php  
RUN sed -i "s/localhost/127.0.0.1/g" /var/www/html/wp-config.php  
  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
EXPOSE 3306 80  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  
  

