FROM ubuntu  
  
RUN apt-get update  
  
#install apache mysql php  
RUN apt-get install -y apache2 php5 libapache2-mod-php5 php5-mcrypt mysql-
server php5-mysql libapache2-mod-auth-mysql curl  
RUN php5enmod mcrypt  
  
#install composer  
RUN curl -sS https://getcomposer.org/installer | sudo php -- --install-
dir=/usr/local/bin --filename=composer  
  
#install phpmyadmin  
RUN apt-get -y install phpmyadmin  
COPY phpmyadmin.conf /etc/apache2/sites-available/phpmyadmin.conf  
COPY config.inc.php /etc/phpmyadmin/config.inc.php  
RUN sed -i -e "6i Listen 8080" /etc/apache2/ports.conf  
WORKDIR /etc/apache2/sites-available  
RUN a2ensite phpmyadmin.conf  
COPY phpmyadmin.sql /root/phpmyadmin.sql  
RUN /bin/bash -c "/usr/bin/mysqld_safe &" && \  
sleep 5 && \  
mysql -u root -e "CREATE DATABASE phpmyadmin" && \  
mysql -u root phpmyadmin < /root/phpmyadmin.sql  
  
#enable rewrite  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
#clean cache  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /root/*  
  
#set auto-load  
WORKDIR /root  
COPY run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
  
EXPOSE 22 80 443 8080  
CMD /root/run.sh

