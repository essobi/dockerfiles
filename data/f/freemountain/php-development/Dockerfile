FROM debian:jessie  
  
ENV RELEASE_DATE 2015-07-03  
ENV DEBIAN_FRONTEND noninteractive  
ENV APACHE_HTTPD "exec /usr/sbin/apache2"  
ENV TERM xterm  
ENV APACHE_LOG_DIR "/var/log/apache2/"  
RUN apt-get -qq update  
#RUN apt-get -y install  
RUN apt-get -qq install \  
nano apache2 php5 ssmtp libapache2-mod-php5 php5-mysql php5-json php5-curl
php5-gd \  
mysql-client mysql-server wget git\  
&& \  
apt-get clean  
  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
ADD 000-app.conf /etc/apache2/sites-available/000-app.conf  
RUN ln -s /etc/apache2/sites-available/000-app.conf /etc/apache2/sites-
enabled/000-app.conf  
ADD 001-adminer.conf /etc/apache2/sites-available/001-adminer.conf  
RUN ln -s /etc/apache2/sites-available/001-adminer.conf /etc/apache2/sites-
enabled/001-adminer.conf  
RUN a2enmod rewrite  
  
#add start script  
ADD ./start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
  
#config mysql  
RUN rm /etc/mysql/my.cnf  
ADD my.cnf /etc/mysql/my.cnf  
  
#create mysql user with DATABASE  
ADD create_user.sql /create_user.sql  
#RUN /usr/sbin/mysqld && mysql -u root < /create_user.sql  
#install adminer  
RUN mkdir /usr/share/adminer  
RUN wget "http://www.adminer.org/latest.php" -O /usr/share/adminer/index.php  
RUN echo "Listen 88" >> /etc/apache2/ports.conf  
  
VOLUME ["/var/www", "/var/lib/mysql"]  
  
EXPOSE 80  
EXPOSE 88  
EXPOSE 3306  
CMD ["/usr/local/bin/start.sh"]  

