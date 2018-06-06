  
FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ARG DVWA_VERSION=master  
  
# Download and install dependencies  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y debconf-utils wget \  
&& echo mysql-server-5.5 mysql-server/root_password password p@ssw0rd |
debconf-set-selections \  
&& echo mysql-server-5.5 mysql-server/root_password_again password p@ssw0rd |
debconf-set-selections \  
&& apt-get -y install apache2 mysql-server mysql-client php5 php5-mysql
php5-gd \  
&& wget https://github.com/ethicalhack3r/DVWA/archive/$DVWA_VERSION.tar.gz -O
/tmp/dvwa.tar.gz \  
&& tar xfz /tmp/dvwa.tar.gz --strip-components=1 -C /var/www/html \  
&& rm -rf /var/www/html/index.html \  
&& rm -rf /tmp/dvwa.tar.gz \  
&& apt-get purge -y debconf-utils wget \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure MySQL  
RUN set -xe \  
&& echo "[client]\nuser=root\npassword=p@ssw0rd" > /root/.my.cnf \  
&& sed -i "s/.*bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/my.cnf \  
&& sed -i "s/^#general_log*/general_log/" /etc/mysql/my.cnf \  
&& sed -i "/skip-external-locking/a secure-file-priv=" /etc/mysql/my.cnf \  
&& service mysql start \  
&& mysql -e "CREATE DATABASE dvwa" \  
&& mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY
'p@ssw0rd'"  
  
# Configure application  
RUN set -xe \  
&& chmod -R 777 /var/www/html/hackable/uploads/
/var/www/html/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt \  
&& chmod 777 /var/www/html/ \  
&& sed -i 's/allow_url_include = Off/allow_url_include = On/g'
/etc/php5/apache2/php.ini \  
&& sed -i "s/^.*recaptcha_public_key.* = '';/\$_DVWA[ 'recaptcha_public_key' ]
= getenv('RECAPTCHA_PUBLIC_KEY');/g" /var/www/html/config/config.inc.php \  
&& sed -i "s/^.*recaptcha_private_key' ].* = '';/\$_DVWA[
'recaptcha_private_key' ] = getenv('RECAPTCHA_PRIVATE_KEY');/g"
/var/www/html/config/config.inc.php  
  
EXPOSE 80 3306  
COPY run.sh /  
CMD ["/run.sh"]  

