FROM ubuntu:14.04  
MAINTAINER Samsul Maarif <hay@samsul.web.id>  
  
EXPOSE 80 443  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Database info  
#ENV MYSQL_HOST 127.0.0.1  
#ENV MYSQL_USER opensid  
#ENV MYSQL_PASSWORD opensid  
#ENV MYSQL_DB opensid  
#ENV OPENSID_URL http://192.168.59.103  
ADD ./foreground.sh /etc/apache2/foreground.sh  
  
RUN apt-get update \  
&& apt-get -y install mysql-client pwgen python-setuptools curl git unzip
apache2 \  
php5-gd libapache2-mod-php5 postfix wget supervisor curl vim-nox libcurl3 \  
libcurl3-dev php5-curl php5-xmlrpc php5-intl php5-mysql git-core php5 \  
&& rm -rf /var/www/html \  
&& git clone https://github.com/eddieridwan/OpenSID.git /var/www/html
--depth=1 \  
&& cp -a /var/www/html/desa-contoh /var/www/html/desa \  
&& chown -R www-data:www-data /var/www/html \  
&& chmod +x /etc/apache2/foreground.sh  
  
COPY database.php /var/www/html/desa/config/database.php  
  
#RUN a2enmod ssl && a2ensite default-ssl # if using proxy, don't need actually
secure connection  
VOLUME ["/var/www/html"]  
  
CMD ["/etc/apache2/foreground.sh"]  

