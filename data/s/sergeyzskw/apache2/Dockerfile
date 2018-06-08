FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
apache2 \  
libapache2-mod-xsendfile && \  
a2enmod \  
rewrite \  
proxy \  
proxy_fcgi \  
headers && \  
sed -i 's/\/var\/www\/html/\/var\/www/' /etc/apache2/sites-
available/000-default.conf && \  
sed -i 's/\/var\/www\/html/\/var\/www/' /etc/apache2/sites-available/default-
ssl.conf && \  
echo '<FilesMatch \\\\.php$>\n\tSetHandler proxy:fcgi://dev-
php55:9000\n</FilesMatch>' > /etc/apache2/conf-available/phpfpm.conf && \  
a2enconf phpfpm && \  
rm -r /var/lib/apt/lists/*  
  
# Alternative solution: main disadventage is directory index is not working  
# sed -i '/DocumentRoot.*/a\\\n\tProxyPassMatch ^/(.+\\.php.*)$
fcgi://php55.local.com:9000/var/www/$1 timeout=1800' /etc/apache2/sites-
available/000-default.conf && \  
# sed -i '/DocumentRoot.*/a\\\n\t\tProxyPassMatch ^/(.+\\.php.*)$
fcgi://php55.local.com:9000/var/www/$1 timeout=1800' /etc/apache2/sites-
available/default-ssl.conf && \  
VOLUME /etc/apache2  
VOLUME /var/www  
VOLUME /var/log  
  
EXPOSE 80 443  
# We have big chance /var/log is already present but /var/log/apache2/ is not
exist  
# so we have to do a few more steps to get container working. It is assumed  
# all those steps are wrapped to SH-script  
COPY apache2-foreground.sh /usr/local/bin/  
  
CMD ["apache2-foreground.sh"]  
  

