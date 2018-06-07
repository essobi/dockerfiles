FROM debian:8.2  
MAINTAINER Julian Waller <julian@tech.guildtv.co.uk>  
  
RUN apt-get update && apt-get install -y git wget curl php-pear php-xml-parser
php5-cli php5-common php5-curl php5-gd php5-intl php5-json php5-mcrypt
php5-mysqlnd php5-readline && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/var/lib/apt/cache/*.deb  
RUN apt-get update && apt-get install -y supervisor nginx php5-fpm && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/* /var/lib/apt/cache/*.deb  
  
#configure nginx and php  
RUN sed -i -e"s/worker_processes 1/worker_processes 5/" /etc/nginx/nginx.conf
# gets over written by start.sh to match cpu on container  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf \  
&& sed -i -e"s/keepalive_timeout 2/keepalive_timeout
2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# tweak php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1a/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini \  
&& sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 10G/g"
/etc/php5/fpm/php.ini \  
&& sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 10G/g"
/etc/php5/fpm/php.ini \  
&& sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf \  
&& sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf \  
&& sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php5/fpm/pool.d/www.conf  
  
# fix ownership of sock file for php-fpm as our version of nginx runs as nginx  
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php5/fpm/pool.d/www.conf \  
&& find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
# download src  
RUN mkdir -p /src && \  
cd /src && \  
wget -O -
"https://releases.wikimedia.org/mediawiki/1.26/mediawiki-1.26.2.tar.gz" | tar
--strip-components=1 -x -z  
  
# setup data mounts  
RUN mkdir -p /data && \  
mv /src/images /data/ && \  
ln -s /data/LocalSettings.php /src/ && \  
ln -s /data/images /src/  
  
# Supervisor Config  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
ADD nginx.conf /etc/nginx/sites-enabled/default  
  
EXPOSE 80  
CMD ["/start.sh"]  

