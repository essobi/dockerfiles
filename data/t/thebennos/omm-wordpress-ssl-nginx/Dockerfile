FROM nginx:latest  
#FROM ubuntu:15.10  
MAINTAINER Benjamin Wenderoth <b.wenderoth@gmail.com>  
  
# Surpress Upstart errors/warning  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update System first before we do something  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Add sources for latest nginx  
RUN apt-get install -y wget sudo  
RUN wget -q http://nginx.org/keys/nginx_signing.key -O- | sudo apt-key add -  
RUN echo deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx >>
/etc/apt/sources.list  
RUN echo deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx >>
/etc/apt/sources.list  
  
# Update System  
RUN apt-get update && apt-get -y upgrade  
  
# Basic Requirements  
RUN apt-get -y install nginx php5-fpm pwgen python-setuptools curl git unzip
vim  
  
# Install Extra PHP Modules  
RUN apt-get -y install php5-curl php5-gd php5-intl php-pear php5-imagick
php5-imap php5-mcrypt php5-memcache php5-pspell php5-recode php5-sqlite
php5-tidy php5-xmlrpc php5-xsl php5-pgsql php5-mongo php5-mysqlnd
php5-mysqlnd-ms  
  
# Adding Github Clone  
# Token = e07a15e5635c022ec7492ffa493a21e863705af3  
# Clone our private GitHub Repository  
# repo = https://github.com/thebennos/omm_dataworker.git  
RUN git clone -b 0.5-beta1
https://e07a15e5635c022ec7492ffa493a21e863705af3:x-oauth-
basic@github.com/thebennos/omm_dataworker.git /myapp/  
RUN cp -R /myapp/* /usr/share/nginx/html  
# RUN chown app:app -R /home/app/ #hopefully not needed  
# tweak nginx config  
RUN sed -i -e"s/worker_processes 1/worker_processes 5/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size
100m/" /etc/nginx/nginx.conf && \  
sed -i "s/.*conf\\.d\/\\*\\.conf;.*/&\n include \/etc\/nginx\/sites-
enabled\/\\*;/" /etc/nginx/nginx.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Install LE's ACME client for domain validation and certificate generation
and renewal  
RUN git clone https://github.com/letsencrypt/letsencrypt  
RUN mkdir -p /tmp/le  
# Opcode config  
RUN sed -i -e"s/^;opcache.enable=0/opcache.enable=1/" /etc/php5/fpm/php.ini  
RUN sed -i
-e"s/^;opcache.max_accelerated_files=2000/opcache.max_accelerated_files=4000/"
/etc/php5/fpm/php.ini  
  
# tweak php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 128M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/max_execution_time\s*=\s*30/max_execution_time = 600/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/memory_limit\s*=\s*128M/memory_limit = 512M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/display_errors\s*=\s*Off/display_errors = On/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
&& \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i 's/access_log.*/access_log \/dev\/stdout;/g' /etc/nginx/nginx.conf && \  
sed -i 's/error_log.*/error_log \/dev\/stdout info;/g' /etc/nginx/nginx.conf  
  
# fix ownership of sock file for php-fpm as our version of nginx runs as nginx  
RUN sed -i -e "s/user = www-data/user = nginx/g" /etc/php5/fpm/pool.d/www.conf
&& \  
sed -i -e "s/group = www-data/group = nginx/g" /etc/php5/fpm/pool.d/www.conf
&& \  
sed -i -e "s/listen.owner = www-data/listen.owner = nginx/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/listen.group = www-data/listen.group = nginx/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php5/fpm/pool.d/www.conf  
# RUN find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
# nginx site conf  
RUN rm -Rf /etc/nginx/conf.d/* && \  
mkdir -p /etc/nginx/sites-available/ && \  
mkdir -p /etc/nginx/sites-enabled/ && \  
mkdir -p /etc/nginx/ssl/  
ADD ./nginx-site.conf /etc/nginx/sites-available/default.conf  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
# add test PHP file  
ADD ./index.php /usr/share/nginx/html/index.php  
RUN chown -Rf www-data:nginx /usr/share/nginx/html/  
#RUN chmod 755 /usr/share/nginx/html/rankings  
#RUN chmod 777 /usr/share/nginx/html/rankings/latest_cache_id.php  
#RUN chown -Rf nginx.nginx /usr/share/nginx/html/  
# Push Migration Skript  
# NO directly Git acces in a container!!!!  
#Add git commands to allow container updating  
#ADD ./pull /usr/bin/pull  
#ADD ./push /usr/bin/push  
#RUN chmod 755 /usr/bin/pull  
#RUN chmod 755 /usr/bin/push  
# Supervisor Config  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD ./supervisord.conf /etc/supervisord.conf  
  
# Start Supervisord  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# Expose Ports  
EXPOSE 443  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  

