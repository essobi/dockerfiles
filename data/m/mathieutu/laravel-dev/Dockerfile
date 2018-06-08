FROM ubuntu  
MAINTAINER Mathieu TUDISCO <dev@mathieutu.ovh>  
#Inpired by richarvey/nginx-php-fpm  
# Add sources and update  
RUN apt-get update && apt-get -y install software-properties-common  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && apt-get update -y  
RUN apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor nginx git
curl vim zip  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php7.1-fpm
php7.1-mysqlnd php7.1-curl php7.1-gd php7.1-intl php7.1-mcrypt php7.1-sqlite
php-xdebug php7.1-cli php-imagick php-mbstring php-xml  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && echo
"deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN DEBIAN_FRONTEND=noninteractive apt-get install nodejs yarn  
  
RUN curl -s https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
RUN echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
# tweak nginx config  
RUN sed -i -e"s/worker_processes 1/worker_processes 5/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size
100m/" /etc/nginx/nginx.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# tweak php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php/7.1/fpm/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/7.1/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/7.1/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-
fpm.conf && \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php/7.1/fpm/pool.d/www.conf  
  
RUN echo "xdebug.remote_handler=dbgp" >> /etc/php/7.1/fpm/conf.d/20-xdebug.ini  
RUN echo "xdebug.remote_port=9000" >> /etc/php/7.1/fpm/conf.d/20-xdebug.ini  
RUN echo "xdebug.remote_connect_back=0" >>
/etc/php/7.1/fpm/conf.d/20-xdebug.ini  
RUN echo "xdebug.remote_log=/tmp/xdebug.log" >>
/etc/php/7.1/fpm/conf.d/20-xdebug.ini  
RUN echo "xdebug.remote_autostart=false " >>
/etc/php/7.1/fpm/conf.d/20-xdebug.ini  
  
# tweak php-cli config  
RUN sed -i -e "a xdebug.max_nesting_level=500" /etc/php/7.1/cli/php.ini  
  
# fix ownership of sock file for php-fpm  
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
find /etc/php/7.1/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
# mycrypt conf  
RUN phpenmod mcrypt  
  
# nginx site conf  
RUN rm -Rf /etc/nginx/conf.d/* && \  
rm -Rf /etc/nginx/sites-available/default && \  
rm -Rf /etc/nginx/sites-enabled/default && \  
mkdir -p /etc/nginx/ssl/  
ADD conf/nginx-site.conf /etc/nginx/sites-available/default.conf  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
  
# Supervisor Config  
ADD conf/supervisord.conf /etc/supervisord.conf  
  
# Fix socket file  
RUN mkdir -p /run/php/ && chown -Rf www-data.www-data /run/php  
  
# Script for Supervisor  
ADD scripts/start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# Setup Volume  
VOLUME ["/usr/share/nginx/html"]  
WORKDIR /usr/share/nginx/html  
  
# add PHPinfo file  
ADD src/index.php /usr/share/nginx/html/index.php  
RUN chown -Rf www-data:www-data /usr/share/nginx/  
  
# add aliases and path  
ADD .bashrc /root/.bashrc  
  
# Expose Ports  
EXPOSE 443  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  

