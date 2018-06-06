FROM ubuntu:14.04  
MAINTAINER SERrex Labs <os@serrexlabs.com>  
  
RUN apt-get --fix-missing update  
RUN apt-get -y install apache2 php5 git curl php5-mcrypt php5-json php5-mysql
libapache2-mod-php5  
RUN apt-get -y install php5-common php5-curl php5-gd php5-dev  
RUN apt-get -y autoremove  
RUN apt-get clean  
  
RUN /usr/sbin/a2enmod rewrite  
  
RUN /usr/sbin/a2enmod socache_shmcb || true  
  
ADD 000-app.conf /etc/apache2/sites-available/  
  
RUN /usr/sbin/a2dissite '*' && /usr/sbin/a2ensite 000-app  
RUN /usr/bin/curl -sS https://getcomposer.org/installer |/usr/bin/php  
RUN /bin/mv composer.phar /usr/local/bin/composer  
RUN /bin/chown www-data:www-data -R /var/www  
RUN /usr/sbin/service apache2 restart  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

