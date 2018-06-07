FROM debian:jessie  
MAINTAINER Fernando Mayo <fernando@tutum.co>, Feng Honglin <hfeng@tutum.co>  
  
#my little hack  
#configuring my custom enviroments for bash script > run.sh  
#ENV HTTP_DOCUMENTROOT /app  
#ENV HTTP_DOCUMENTROOT /var/www/html  
#ENV PACKAGE_URL https://github.com/litzinetz-
de/OpenVoucher/archive/0.4.2.tar.gz  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install supervisor git apache2 libapache2-mod-php5 mysql-server
php5-mysql pwgen wget net-tools iptables nano sudo php-apc php5-mcrypt && \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
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
  
# Configure /app folder with sample app  
#RUN git clone https://github.com/fermayo/hello-world-lamp.git /app  
#RUN rm -fr /var/www/html && ln -s /var/www /var/www/html  
#RUN echo "www-data ALL=(ALL) NOPASSWD: /sbin/iptables" >> /etc/sudoers  
#RUN sed 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf  
#adding my own little hack  
######################################################################################################################  
#ENV PACKAGE_URL https://github.com/litzinetz-
de/OpenVoucher/archive/0.4.2.tar.gz  
#ADD ${PACKAGE_URL} package.tar.gz  
#RUN tar -zxf package.tar.gz  
#RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html && cp
-pr OpenVoucher-*/src/* /app/ && rm -rf /app/.htaccess && rm -rf OpenVoucher-*
&& chown -R www-data:www-data /app  
#########################################################################################################################  
#Enviornment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
# Add volumes for MySQL  
VOLUME ["/etc/mysql", "/var/lib/mysql", "/var/www" ]  
  
EXPOSE 80 3306  
CMD ["/run.sh"]  

