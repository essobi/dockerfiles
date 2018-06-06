FROM ubuntu:12.04  
RUN apt-get update && apt-get install -y \  
apache2 \  
php5 \  
php5-cli \  
libapache2-mod-php5 \  
php5-gd \  
php5-pgsql \  
php5-mcrypt \  
ca-certificates \  
curl  
  
COPY apache_default /etc/apache2/sites-available/default  
RUN a2enmod rewrite  
  
RUN curl -SL https://github.com/edsondewes/docker-
ecidadeonline/releases/download/2.3.46/e-cidadeonline-2.3.46.tar.gz | tar -xz
-C /var/www/  
  
RUN mkdir /var/www/tmp \  
&& chown -R www-data.www-data /var/www/tmp \  
&& chmod -R 777 /var/www/tmp \  
&& mkdir /var/www/log \  
&& chown -R www-data.www-data /var/www/log \  
&& chown root.www-data /var/lib/php5 \  
&& chmod g+r /var/lib/php5 \  
&& useradd -d /home/dbseller -g www-data -k /etc/skel -m -s /bin/bash dbseller
\  
&& echo 'dbseller:dbseller' | chpasswd \  
&& chown -R dbseller.www-data /var/www/e-cidadeonline \  
&& chmod -R 775 /var/www/e-cidadeonline \  
&& chmod -R 777 /var/www/e-cidadeonline/tmp  
  
EXPOSE 80  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

