FROM ubuntu:14.04  
MAINTAINER Naina Johari <naina.johari379@webkul.com> <k.naina88@gmail.com>  
  
# Update existing packages & install LAMPSTACK  
RUN apt-get update  
RUN apt-get install -y lamp-server^ && \  
apt-get install -y wget unzip pwgen  
RUN apt-get install -y libapache2-mod-php5 php5-mcrypt php5-gd  
RUN apt-get install -y curl libcurl3 libcurl3-dev php5-curl php5-mcrypt  
  
# Download opencart  
ADD https://github.com/opencart/opencart/archive/2.0.1.1.zip /tmp/  
  
# Remove previous files of default document root  
RUN rm -rf /var/www/html/*  
  
# Extract Joomla  
RUN cd /tmp && unzip 2.0.1.1.zip  
RUN cd /tmp/opencart-2.0.1.1 && mv upload /var/www/html/cscart  
RUN cd /var/www/html/cscart && mv config-dist.php config.php  
RUn cd /var/www/html/cscart/admin && mv config-dist.php config.php  
  
# Grant permission of the directory to apache2  
RUN chown -R www-data:www-data /var/www/html && \  
chmod -R 755 /var/www/html  
  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
RUN php5enmod mcrypt  
  
ADD startupscript.sh /etc/startupscript.sh  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD adminer.php /var/www/html/cscart/  
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh  
RUN chmod 755 /create_mysql_admin_user.sh  
RUN ./create_mysql_admin_user.sh > /password.txt  
  
EXPOSE 80  
EXPOSE 3306  
CMD ["/usr/bin/supervisord"]  

