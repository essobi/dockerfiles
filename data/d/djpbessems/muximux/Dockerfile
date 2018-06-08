FROM ubuntu:16.04  
  
COPY start.sh /usr/local/bin/muximux.sh  
VOLUME /mnt/config  
  
RUN apt-get update && \  
apt-get install -y \  
software-properties-common && \  
add-apt-repository "deb http://nl.archive.ubuntu.com/ubuntu/ xenial
multiverse" && \  
apt-get update && \  
apt-get install -y \  
git-core \  
lighttpd \  
php7.0 \  
php7.0-fpm \  
php-cgi && \  
rm -rf /var/lib/apt/lists/* && \  
sed -i 's:;cgi.fix_pathinfo=1:cgi.fix_pathinfo=1:' /etc/php/7.0/fpm/php.ini &&
\  
sed -i 's:"socket" => "/var/run/lighttpd/php.socket":"socket" =>
"/var/run/php/php7.0-fpm.sock":' /etc/lighttpd/conf-available/15-fastcgi-
php.conf && \  
sed -i 's:/var/www/html:/mnt/config/muximux/www:' /etc/lighttpd/lighttpd.conf
&& \  
mkdir -p /mnt/config/muximux/www && \  
chmod +x /usr/local/bin/muximux.sh && \  
lighttpd-enable-mod fastcgi && \  
lighttpd-enable-mod fastcgi-php && \  
service php7.0-fpm start && \  
apt-get remove -y \  
software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean -y  
  
EXPOSE 80  
  
CMD ["/usr/local/bin/muximux.sh"]  

