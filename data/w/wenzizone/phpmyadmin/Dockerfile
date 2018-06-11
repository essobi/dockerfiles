FROM wenzizone/base  
MAINTAINER wenzizone <wenzizone@126.com>  
RUN apt-get update && \  
apt-get install -y apache2 php5 phpmyadmin && \  
apt-get clean  
  
RUN ln -s /etc/phpmyadmin/apache.conf /etc/apache2/sites-
enabled/001-phpmyadmin.conf  
ADD config-db.php /etc/phpmyadmin/config-db.php  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

