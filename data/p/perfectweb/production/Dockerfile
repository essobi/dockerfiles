FROM ubuntu  
MAINTAINER Alin Jurj <office@perfectweb.ro>  
  
USER root  
WORKDIR /root  
  
# variables setup  
ENV APPLICATION_ENV production  
ENV DEBIAN_FRONTEND noninteractive  
ENV PHP_INI /etc/php5/cli/php.ini  
ENV NGINX_VHOST_DIR /etc/nginx/vhosts  
ENV NGINX_VHOST ${NGINX_VHOST_DIR}/vhost.conf  
ENV START_MYSQL true  
ENV NGINX_CONF /etc/nginx/nginx.conf  
ENV FPM_POOL_CONF /etc/php5/fpm/pool.d/www.conf  
ENV HOME_DIR /root  
ENV PROJECTS_DIR /var/www/html  
ENV LOGS_DIR ${HOME_DIR}/logs  
ENV MAX_UPLOAD 4000M  
ENV OPENRESTY_VERSION ngx_openresty-1.9.3.1  
ENV IMAGEMAGICK_VERSION 6.9.2-4  
ENV INIT_SCRIPTS ;  
  
# ports  
EXPOSE 80 443 3306 6379 4730  
# add repositories  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository -y ppa:mc3man/trusty-media  
RUN add-apt-repository -y ppa:nginx/stable  
RUN add-apt-repository -y ppa:ondrej/php5-5.6  
RUN add-apt-repository -y ppa:ondrej/mysql-5.6  
  
RUN apt-get -y update  
RUN apt-get -y --force-yes dist-upgrade  
RUN apt-get -y --force-yes install luarocks libmagickwand-dev luajit gcc gpac
mysql-server-5.6 mysql-client-5.6 lynx libgd-dev libxslt-dev nginx unzip wget
ffmpeg gstreamer0.10-ffmpeg git locate nodejs npm telnet redis-server
libsphinxclient-dev php5 php5-redis php5-memcache php5-memcached php5-dev
php5-imagick php5-mcrypt php5-json php5-intl php5-curl php5-xsl php5-xmlrpc
php5-gd php5-cli php5-mysqlnd php5-xdebug php5-fpm php5-gearman php-
codesniffer php5-oauth php5-apcu htop nano postfix sphinxsearch gearman-job-
server openssh-server geoip-bin geoip-database geoip-dbg libgeoip-dev phpunit*  
RUN yes '' | pecl install -f sphinx  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN rm /etc/localtime ; ln -s /usr/share/zoneinfo/Europe/London /etc/localtime  
RUN npm install -g bower forever 'grunt-cli'  
  
RUN wget -O /usr/bin/composer https://getcomposer.org/composer.phar  
RUN chmod +x /usr/bin/composer  
  
RUN wget -O /usr/bin/behat https://github.com/downloads/Behat/Behat/behat.phar  
RUN chmod +x /usr/bin/behat  
  
RUN wget -O /usr/bin/phpunit https://phar.phpunit.de/phpunit.phar  
RUN chmod +x /usr/bin/phpunit  
  
RUN wget -O /usr/bin/phpcs
https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar  
RUN chmod +x /usr/bin/phpcs  
  
RUN wget -O /usr/bin/phpcbf
https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar  
RUN chmod +x /usr/bin/phpcbf  
  
RUN wget -O /usr/bin/phpmd http://static.phpmd.org/php/2.2.0/phpmd.phar  
RUN chmod +x /usr/bin/phpmd  
  
RUN wget -O /usr/bin/phing http://www.phing.info/get/phing-latest.phar  
RUN chmod +x /usr/bin/phing  
  
# setup logs and folders  
RUN ln -s ${PROJECTS_DIR} ${HOME_DIR}/html ; mkdir ${LOGS_DIR} ; echo '' >
${LOGS_DIR}/php.log  
  
# php setup  
RUN rm /etc/php5/fpm/php.ini ; ln -s ${PHP_INI} /etc/php5/fpm/php.ini  
RUN sed -i.bak "s|error_log = \\(.*\\)|error_log = ${LOGS_DIR}/php\\.log|g"
/etc/php5/fpm/php-fpm.conf  
RUN sed -i.bak 's/short_open_tag = \\(.*\\)/short_open_tag = On/g' ${PHP_INI}  
RUN sed -i.bak 's/allow_url_fopen = \\(.*\\)/allow_url_fopen = Off/g'
${PHP_INI}  
RUN sed -i.bak 's/\;date\\.timezone =/date\\.timezone = \"Europe\/London\"/g'
${PHP_INI}  
RUN sed -i.bak 's/upload_max_filesize = \\(.*\\)/upload_max_filesize =
${MAX_UPLOAD}/g' ${PHP_INI}  
RUN sed -i.bak "s|\;error_log = \\(.*\\)|error_log = ${LOGS_DIR}/php\\.log|g"
${PHP_INI}  
RUN sed -i.bak 's/display_errors = \\(.*\\)/display_errors = Off/g' ${PHP_INI}  
RUN sed -i.bak 's/display_startup_errors = \\(.*\\)/display_startup_errors =
Off/g' ${PHP_INI}  
RUN sed -i.bak 's/error_reporting =\\(.*\\)/error_reporting = E_ALL \&
~E_DEPRECATED \& ~E_STRICT \& ~E_NOTICE/g' ${PHP_INI}  
RUN sed -i.bak 's/\;error_prepend_string =\\(.*\\)/error_prepend_string =
\"<pre>\"/g' ${PHP_INI}  
RUN sed -i.bak 's/\;error_append_string =\\(.*\\)/error_append_string =
\"<\/pre>\"/g' ${PHP_INI}  
RUN sed -i.bak 's/post_max_size =\\(.*\\)/post_max_size = ${MAX_UPLOAD}/g'
${PHP_INI}  
RUN echo 'extension=sphinx.so' >> ${PHP_INI}  
  
# some php extension changes  
RUN echo 'apc.enabled=1' >> /etc/php5/mods-available/apcu.ini  
RUN echo 'opcache.enable=1' >> /etc/php5/mods-available/opcache.ini  
  
# php-fpm  
RUN sed -i.bak 's/listen =\\(.*\\)/listen = \/var\/run\/php5-fpm\\.sock/g'
${FPM_POOL_CONF}  
RUN sed -i.bak 's/\;request_slowlog_timeout =\\(.*\\)/request_slowlog_timeout
= 10s/g' ${FPM_POOL_CONF}  
RUN sed -i.bak 's/\;catch_workers_output/catch_workers_output/g'
${FPM_POOL_CONF}  
RUN sed -i.bak "s|\;slowlog = log|slowlog = ${LOGS_DIR}|g" ${FPM_POOL_CONF}  
RUN sed -i.bak "s|\;access\\.log = log|access\\.log = ${LOGS_DIR}|g"
${FPM_POOL_CONF}  
RUN sed -i.bak "s/pm.max_children =\\(.*\\)/pm.max_children = 50/g"
${FPM_POOL_CONF}  
RUN sed -i.bak "s/pm.start_servers =\\(.*\\)/pm.start_servers = 10/g"
${FPM_POOL_CONF}  
RUN sed -i.bak "s/pm.min_spare_servers =\\(.*\\)/pm.min_spare_servers = 10/g"
${FPM_POOL_CONF}  
RUN sed -i.bak "s/pm.max_spare_servers =\\(.*\\)/pm.max_spare_servers = 10/g"
${FPM_POOL_CONF}  
RUN sed -i.bak 's/www-data/root/g' ${FPM_POOL_CONF}  
RUN sed -i.bak 's/--daemonize/--daemonize --allow-to-run-as-root /g'
/etc/init.d/php5-fpm  
  
# nginx setup  
RUN wget http://openresty.org/download/${OPENRESTY_VERSION}.tar.gz; wget
https://github.com/openresty/sregex/archive/master.zip; wget -O replace.zip
https://github.com/openresty/replace-filter-nginx-module/archive/master.zip  
RUN tar xvf ${OPENRESTY_VERSION}.tar.gz; unzip master.zip; unzip replace.zip  
RUN cd sregex-master; make; make install; rm -f /usr/sbin/nginx; mkdir -p
/var/lib/nginx/body  
RUN cd ${OPENRESTY_VERSION}; ./configure --with-cc-opt='-g -O2 -fPIE -fstack-
protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security
-D_FORTIFY_SOURCE=2' \--with-ld-opt='-Wl,-Bsymbolic-functions -fPIE -pie
-Wl,-z,relro -Wl,-z,now' \--prefix=/usr/share/nginx --conf-
path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-
log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-
path=/run/nginx.pid --http-client-body-temp-path=/var/lib/nginx/body --http-
fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-
path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-
uwsgi-temp-path=/var/lib/nginx/uwsgi --with-debug --with-pcre-jit --with-ipv6
--with-http_ssl_module --with-http_stub_status_module --with-
http_realip_module --with-http_auth_request_module --with-http_addition_module
--with-http_dav_module --with-http_geoip_module --with-http_gunzip_module
--with-http_gzip_static_module --with-http_image_filter_module --with-
http_spdy_module --with-http_sub_module --with-http_xslt_module --with-mail
--with-mail_ssl_module --add-module=../replace-filter-nginx-module-master
--with-ld-opt="-Wl,-rpath,/usr/local/lib" \--sbin-path=/usr/sbin/nginx  
RUN cd ${OPENRESTY_VERSION}; make; make install  
RUN rm -fr ${OPENRESTY_VERSION}.tar.gz master.zip replace.zip
${OPENRESTY_VERSION} sregex-master replace-filter-nginx-module-master  
  
RUN echo "env MYSQL_PORT_3306_TCP_ADDR; user root; worker_processes auto;
worker_rlimit_nofile 65535; error_log ${LOGS_DIR}/nginx.error.log; events {
worker_connections 10240; } http { include mime.types; default_type
application/octet-stream; access_log ${LOGS_DIR}/nginx.access.log; sendfile
on; keepalive_timeout 65; gzip on; server { listen 80 default_server;
server_name _; location / { root html; index index.html index.htm; }
error_page 500 502 503 504 /50x.html; location = /50x.html { root html; } }
include ${NGINX_VHOST_DIR}/*.conf; }" > ${NGINX_CONF}  
RUN mkdir /var/cache/nginx ; mkdir ${NGINX_VHOST_DIR}  
RUN echo 'server {' >> ${NGINX_VHOST}  
RUN echo "client_max_body_size ${MAX_UPLOAD};" >> ${NGINX_VHOST}  
RUN echo 'server_name
"~^(?<project>.*?[a-z0-9]+)\\.?(?<tld>[a-z0-9\\.]{2,5})?(\\.)local$";' >>
${NGINX_VHOST}  
RUN echo 'index index.php index.html index.htm;' >> ${NGINX_VHOST}  
RUN echo "root ${PROJECTS_DIR}/\$project/public;" >> ${NGINX_VHOST}  
RUN echo 'location / { try_files $uri $uri/ /index.php?$query_string; }' >>
${NGINX_VHOST}  
RUN echo "location ~ \\.php { include ${NGINX_VHOST_DIR}/../fastcgi.conf; }}"
>> ${NGINX_VHOST}  
  
RUN echo 'fastcgi_pass unix:/var/run/php5-fpm.sock; \nfastcgi_intercept_errors
on; \nfastcgi_index index.php; \ninclude fastcgi_params;' >>
${NGINX_VHOST_DIR}/../fastcgi.conf  
  
# sphinxsearch  
RUN cp /etc/sphinxsearch/sphinx.conf.sample /etc/sphinxsearch/sphinx.conf ;
sed -i.bak 's/START=\\(.*\\)/START=yes/g' /etc/default/sphinxsearch  
  
# sshd  
RUN passwd -d root  
RUN sed -i.bak 's/\\(.*\\)PermitRootLogin\\(.*\\)/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
RUN sed -i.bak 's/\\(.*\\)UsePAM\\(.*\\)/UsePAM no/g' /etc/ssh/sshd_config  
RUN sed -i.bak 's/\\(.*\\)PermitEmptyPasswords\\(.*\\)/PermitEmptyPasswords
yes/g' /etc/ssh/sshd_config  
RUN sed -i.bak 's/\\(.*\\)IgnoreUserKnownHosts\\(.*\\)/IgnoreUserKnownHosts
yes/g' /etc/ssh/sshd_config  
  
RUN echo '#!/bin/bash\nservice ssh restart ; service postfix restart ; service
nginx restart ; service php5-fpm restart ; service redis-server restart' >
${HOME_DIR}/run.sh  
RUN echo 'if [[ $START_GEARMAN != "false" ]]; then service gearman-job-server
restart; fi' >> ${HOME_DIR}/run.sh  
RUN echo 'if [[ $START_SPHINX != "false" ]]; then service sphinxsearch restart
; indexer --rotate --all; fi \n (crontab -l 2>/dev/null; echo "30 * * * *
indexer --rotate --all")| crontab -' >> ${HOME_DIR}/run.sh  
RUN echo 'if [[ $START_MYSQL != "false" ]]; then service mysql restart; fi' >>
${HOME_DIR}/run.sh  
RUN echo 'for i in $(echo $INIT_SCRIPTS | tr ";" "\\\n")\ndo\n\tsh $i\ndone'
>> ${HOME_DIR}/run.sh  
RUN echo 'tail -f logs/* & /bin/bash' >> ${HOME_DIR}/run.sh  
RUN chmod 0755 ${HOME_DIR}/run.sh  
  
# imagemagick  
RUN wget
http://www.imagemagick.org/download/ImageMagick-${IMAGEMAGICK_VERSION}.tar.gz
; tar xzvf ImageMagick-${IMAGEMAGICK_VERSION}.tar.gz ; cd
ImageMagick-${IMAGEMAGICK_VERSION} ; ./configure
--prefix=/opt/imagemagick-${IMAGEMAGICK_VERSION} && make && make install ; rm
-rf /root/ImageMagick*  
  
# mysql  
RUN echo '[mysqld] \n max_allowed_packet=600M' >> /etc/mysql/conf.d/mysql.cnf  
  
# lua  
RUN luarocks install --server=http://rocks.moonscript.org magick  
  
# clean up  
RUN apt-get clean ; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/*.bak
/root/tmp ; updatedb  
  
ENTRYPOINT ${HOME_DIR}/run.sh  

