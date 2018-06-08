FROM ssiegel/base-nginx  
MAINTAINER Stefan Siegel <ssiegel@sdas.net>  
  
RUN set -ex; \  
apt-get install imapproxy \  
php5-fpm php5-intl php5-json php5-sqlite php5-mcrypt php5-pspell \  
aspell-de aspell-en aspell-fr  
  
ADD imapproxy.service /etc/systemd/system/  
RUN set -ex; \  
sed -ri /etc/imapproxy.conf \  
-e 's@^listen_port .*@listen_port 143@' \  
-e 's@^force_tls .*@force_tls yes@' \  
-e 's@^#?tls_ca_path .*@tls_ca_path /usr/share/ssl/certs/@'; \  
systemctl enable imapproxy.service; \  
\  
printf '[PHP]\npost_max_size = 32M\nupload_max_filesize = 32M\n' >
/etc/php5/fpm/conf.d/50-max-upload.ini; \  
printf '[Date]\ndate.timezone = "%s"\n' "$(cat /etc/timezone)" >
/etc/php5/fpm/conf.d/50-timezone.ini; \  
\  
curl
http://master.dl.sourceforge.net/project/roundcubemail/roundcubemail/1.1.1/roundcubemail-1.1.1-complete.tar.gz
\  
| tar -xz --transform 's@^[^/]*@roundcube@x' \--exclude='*/installer' -C
/usr/share/nginx; \  
\  
mkdir /data; \  
chown -R www-data:www-data /data /usr/share/nginx/roundcube  
  
ADD container-boot.d /etc/container-boot.d/  
ADD nginx.conf /etc/nginx/conf.d/  
ADD config.tmpl.php /usr/share/nginx/roundcube/config/  
  
EXPOSE 80  
# VOLUME ["/data"]  

