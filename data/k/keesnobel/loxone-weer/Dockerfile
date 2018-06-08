FROM ubuntu:14.04  
MAINTAINER keesnobel <keesnobel.nl@gmail.com>  
  
RUN apt-get update -y  
RUN apt-get -y install supervisor  
RUN apt-get -y install apache2  
RUN apt-get -y install libapache2-mod-php5  
RUN apt-get -y install cron  
RUN apt-get -y install perl  
RUN apt-get -y install curl  
RUN apt-get -y install openssl  
RuN apt-get clean  
  
ADD start.sh /start.sh  
ADD start-apache2.sh /start-apache2.sh  
RUN chmod 755 /*.sh  
RUN mkdir -p /etc/supervisor/conf.d  
ADD supervisor-apache2.conf /etc/supervisor/conf.d/apache2.conf  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
ADD apache-default.conf /etc/apache2/sites-available/000-default.conf  
  
RUN a2enmod cgi  
RUN a2enmod rewrite  
RUN a2enmod headers  
RUN a2enmod deflate  
RUN a2enmod env  
RUN a2enmod expires  
  
VOLUME /usr/lib/cgi-bin/  
VOLUME /var/www/  
  
ADD crontab /var/spool/cron/crontabs/root  
RUN chmod 0600 /var/spool/cron/crontabs/root  
CMD cron  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  

