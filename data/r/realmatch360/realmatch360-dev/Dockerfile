FROM ubuntu:latest  
MAINTAINER Silvan Adrian <silvan.adrian@gmail.com>  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-client mysql-
server apache2 libapache2-mod-php5 pwgen python-setuptools vim-tiny php5-mysql
git  
RUN easy_install supervisor  
ADD ./scripts/start.sh /start.sh  
ADD ./scripts/wordpress.sql /wordpress.sql  
ADD ./scripts/foreground.sh /etc/apache2/foreground.sh  
ADD ./configs/supervisord.conf /etc/supervisord.conf  
ADD ./configs/000-default.conf /etc/apache2/sites-available/000-default.conf  
ADD ./content/ /content/  
RUN rm -rf /var/www/  
RUN git clone https://github.com/Realmatch360/realmatch360.git  
ADD https://wordpress.org/latest.tar.gz /wordpress.tar.gz  
RUN tar xvzf /wordpress.tar.gz  
RUN mv /wordpress /var/www/  
RUN mv realmatch360 /var/www/wp-content/themes/  
RUN cp -R /content/plugins/* /var/www/wp-content/plugins  
RUN mv -v /content/uploads/ /var/www/wp-content/  
RUN chown -R www-data:www-data /var/www/  
RUN chmod 755 /start.sh  
RUN chmod 755 /etc/apache2/foreground.sh  
RUN mkdir /var/log/supervisor/  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  

