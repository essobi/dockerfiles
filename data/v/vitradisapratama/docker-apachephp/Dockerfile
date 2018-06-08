FROM ubuntu  
MAINTAINER Vitradisa Pratama (vitradisapratama@gmail.com)  
  
RUN apt-get update && apt-get install -y wget apache2 php5 php5-mysql
php5-pgsql php5-gd php5-memcache php5-xmlrpc libapache2-mod-php5 && rm -rf
/var/lib/apt/lists/*  
  
RUN pear install Net_Gearman-0.2.3  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

