FROM whiledo/letsencrypt-apache-ubuntu  
MAINTAINER Kevin Krummenauer <kevin@whiledo.de>  
  
#Install packages as described here
http://www.ilias.de/docu/goto_docu_pg_64272_367.html  
#no mysql-client and no mysql-server, because they should run in a separate
Docker container  
RUN apt-get update && apt-get install -y \  
wget \  
git \  
zip \  
# apache2 \ #already installed in baseimage  
php5 \  
php5-gd \  
php5-mysql \  
php5-curl \  
php-auth \  
php-auth-http \  
php5-xsl \  
htmldoc \  
imagemagick \  
mysql-client \  
sendmail  
# openjdk-9-jdk #not needed most times, install it with apt-get install -y
openjdk-7-jdk if you need  
  
WORKDIR /data  
ADD resources /data/resources/base  
  
#Disable old settings  
RUN sed -i 's/max_execution_time/;max_execution_time/g'
/etc/php5/apache2/php.ini \  
&& sed -i 's/memory_limit/;memory_limit/g' /etc/php5/apache2/php.ini \  
  
&& sed -i 's/error_reporting/;error_reporting/g' /etc/php5/apache2/php.ini \  
&& sed -i 's/display_errors/;display_errors/g' /etc/php5/apache2/php.ini \  
  
&& sed -i 's/post_max_size/;post_max_size/g' /etc/php5/apache2/php.ini \  
&& sed -i 's/upload_max_filesize/;upload_max_filesize/g'
/etc/php5/apache2/php.ini \  
  
&& sed -i 's/session.gc_probability/;session.gc_probability/g'
/etc/php5/apache2/php.ini \  
&& sed -i 's/session.gc_divisor/;session.gc_divisor/g'
/etc/php5/apache2/php.ini \  
&& sed -i 's/session.gc_maxlifetime/;session.gc_maxlifetime/g'
/etc/php5/apache2/php.ini \  
&& sed -i 's/session.hash_function/;session.hash_function/g'
/etc/php5/apache2/php.ini \  
  
&& sed -i 's/allow_url_fopen/;allow_url_fopen/g' /etc/php5/apache2/php.ini \  
  
#Insert new settings, as described here
http://www.ilias.de/docu/goto_docu_pg_6531_367.html  
&& cat /data/resources/base/phpinisettings >> /etc/php5/apache2/php.ini  
  
#Then download ilias, unzip it and restart apache2  
RUN git clone https://github.com/ILIAS-eLearning/ILIAS.git
/data/resources/base/ilias \  
&& cd /data/resources/base/ilias/ \  
&& git checkout release_5-2 \  
&& mv /data/resources/base/ilias /var/www/html/ilias \  
&& rm -rf /data/resources/base/ilias  
  
#RUN unzip /data/resources/base/ILIAS-5.0.3.zip -d /var/www/html/ \  
#&& mv /var/www/html/ILIAS-5.0.3 /var/www/html/ilias \  
#&& rm /data/resources/base/ILIAS-5.0.3.zip  
  
RUN chown -R www-data:www-data /var/www/html/ilias \  
&& mkdir /opt/iliasdata \  
&& chown www-data:www-data /opt/iliasdata \  
&& chmod 751 /opt/iliasdata \  
  
&& mkdir /data/share \  
&& mv /data/resources/base/ilias.tar.gz /data/share/ \  
&& chown www-data:www-data /data/share \  
&& chmod 751 /data/share \  
  
&& chown www-data:www-data /data/resources/base/entrypoint.sh \  
&& chmod 751 /data/resources/base/entrypoint.sh \  
  
&& chown www-data:www-data /data/resources/base/createiliasdump.sh \  
&& chmod 751 /data/resources/base/createiliasdump.sh \  
&& chown www-data:www-data /data/resources/base/restoreilias.sh \  
&& chmod 751 /data/resources/base/restoreilias.sh \  
  
#Problem in LetsEncrypt when changing the DocumentRoot...  
#&& sed -i 's|/var/www/html|/var/www/html/ilias|g' /etc/apache2/sites-
enabled/000-default.conf \  
#...so we do a http redirect to /ilias  
&& rm /var/www/html/index.html \  
&& echo "<?php header('Location: ilias'); ?>" > /var/www/html/index.php  
  
ENV apachestartmode="FOREGROUND" \  
createdump="no" \  
restorefromdump="no"  
  
EXPOSE 80 443  
  
ENTRYPOINT ["/data/resources/base/entrypoint.sh"]  
  

