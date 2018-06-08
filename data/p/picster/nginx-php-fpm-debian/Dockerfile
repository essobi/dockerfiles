FROM debian:jessie  
  
MAINTAINER Jimmi Kristensen <picbox@gmail.com>  
  
# install packages  
RUN apt-get update && \  
apt-get -y install supervisor && \  
apt-get -y install nginx && \  
apt-get -y install php5-fpm && \  
apt-get -y install php5-mysql && \  
apt-get -y install php5-mcrypt && \  
apt-get -y install php5-xdebug && \  
apt-get -y install php5-mysqlnd && \  
apt-get -y install php5-curl && \  
apt-get -y install php-mail && \  
apt-get -y install php5-json && \  
apt-get -y install phpunit && \  
apt-get clean && \  
apt-get autoclean  
  
# prepare nginx  
RUN sed -i -e"s/worker_processes 1/worker_processes 5/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size
100m/" /etc/nginx/nginx.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# prepare php-fpm  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
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
/etc/php5/fpm/pool.d/www.conf  
  
# prepare ownership of php-fpm socket file  
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php5/fpm/pool.d/www.conf && \  
find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
# mycrypt conf  
RUN php5enmod mcrypt  
  
# nginx site conf  
RUN rm -Rf /etc/nginx/conf.d/* && \  
rm -Rf /etc/nginx/sites-enabled/default && \  
rm -Rf /etc/nginx/sites-available/default && \  
mkdir -p /etc/nginx/ssl/  
ADD ./default /etc/nginx/sites-available/default  
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
ADD ./index.php /usr/share/nginx/html/index.php  
RUN chown -Rf www-data.www-data /usr/share/nginx/html/  
  
# Supervisor Config  
ADD ./supervisord.conf /etc/supervisord.conf  
  
# Start Supervisord  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
CMD ["/bin/bash", "/start.sh"]  

