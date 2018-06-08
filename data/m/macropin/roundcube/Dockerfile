FROM debian:jessie  
  
MAINTAINER Andrew Cutler <macropin@gmail.com>  
  
EXPOSE 80 443  
ENV ROUNDCUBE_VERSION 1.2.7  
RUN apt-get update && \  
# Nice to have  
apt-get install -y vim && \  
# Install Requirements  
apt-get install -y apache2-mpm-prefork ca-certificates && \  
apt-get install -y php5 php-pear php5-mysql php5-pgsql php5-sqlite php5-mcrypt
php5-intl php5-ldap && \  
# Install Pear Requirements  
pear install mail_mime mail_mimedecode net_smtp net_idna2-beta auth_sasl
net_sieve crypt_gpg && \  
# Cleanup  
rm -rf /var/lib/apt/lists/*  
  
# Host Configuration  
COPY apache2.conf /etc/apache2/apache2.conf  
COPY mpm_prefork.conf /etc/apache2/mods-available/  
RUN rm /etc/apache2/conf-enabled/* /etc/apache2/sites-enabled/* && \  
a2enmod mpm_prefork deflate rewrite expires headers php5  
  
# Install Code from Git  
RUN apt-get update && \  
apt-get install -y git && \  
rm -rf /var/www/html/* && \  
cd /var/www/html && git clone https://github.com/roundcube/roundcubemail.git .
&& \  
git checkout tags/$ROUNDCUBE_VERSION && rm -rf installer .git && \  
# Cleanup  
apt-get remove -y git && apt-get -y autoremove && rm -rf /var/lib/apt/lists/*  
  
# App Configuration  
RUN . /etc/apache2/envvars && chown -R ${APACHE_RUN_USER}:${APACHE_RUN_GROUP}
/var/www/html/temp /var/www/html/logs  
COPY config.inc.php /var/www/html/config/config.inc.php  
  
# Add bootstrap tool  
ADD bootstrap.php /  
  
ADD entry.sh /  
ENTRYPOINT ["/entry.sh"]  
CMD [ "/usr/sbin/apache2ctl", "-D", "FOREGROUND", "-k", "start" ]  

