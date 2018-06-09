FROM nguyenphuongthanhf/ubuntu1604:latest  
  
ENV FIRST_USER apache2  
# Add default apache2 user  
RUN useradd -u 1000 -m --shell /bin/bash $FIRST_USER && \  
echo "${FIRST_USER}:P@ssw0rd123456" | chpasswd  
  
ENV VOLUME_DATA /data  
ENV VOLUME_CONFIG $VOLUME_DATA/config  
ENV VOLUME_LOG $VOLUME_DATA/log  
ENV APP_TORAN_HOST toranproxy.anphabe.net  
ENV APP_TORAN_SOURCE_FILENAME toran-proxy-v1.5.4.tgz  
ENV APP_TORAN_SOURCE https://toranproxy.com/releases/toran-proxy-v1.5.4.tgz  
  
ENV APACHE2_CONFIG_FOLDER $VOLUME_DATA/apache2/config  
ENV APACHE2_DATA_FOLDER $VOLUME_DATA/apache2/www  
ENV APACHE2_LOG_FOLDER $VOLUME_DATA/apache2/log  
ENV PHP5_CONFIG_FOLDER $VOLUME_DATA/php/config  
ENV PHP5_LOG_FOLDER $VOLUME_DATA/php/log  
  
RUN DEBIAN_FRONTEND=noninteractive \  
&& apt-get install -y python-software-properties \  
&& add-apt-repository -y ppa:ondrej/php \  
&& apt-get update -y \  
&& apt-get install -y git apache2 libapache2-mod-xsendfile \  
&& a2enmod rewrite \  
&& a2enmod vhost_alias \  
&& a2enmod proxy \  
&& a2enmod proxy_http \  
&& adduser www-data $FIRST_USER \  
&& echo "ServerName localhost" >> /etc/apache2/apache2.conf \  
&& sed -e "s/www-data/${FIRST_USER}/g" -i /etc/apache2/envvars \  
&& mv /etc/apache2 /etc/apache2_origin \  
&& mkdir -p $APACHE2_CONFIG_FOLDER \  
&& rm $APACHE2_CONFIG_FOLDER -rf \  
&& ln -s /etc/apache2_origin $APACHE2_CONFIG_FOLDER \  
&& ln -s $APACHE2_CONFIG_FOLDER /etc/apache2 \  
&& mv /var/www /var/www_origin \  
&& mkdir -p $APACHE2_DATA_FOLDER \  
&& rm $APACHE2_DATA_FOLDER -rf \  
&& ln -s /var/www_origin $APACHE2_DATA_FOLDER \  
&& ln -s $APACHE2_DATA_FOLDER /var/www \  
&& chown $FIRST_USER:$FIRST_USER -h /var/www \  
&& rm /var/log/apache2 -R \  
&& mkdir -p $APACHE2_LOG_FOLDER \  
&& rm $APACHE2_LOG_FOLDER -rf \  
&& ln -s $APACHE2_LOG_FOLDER /var/log/apache2 \  
&& apt-get install -y libapache2-mod-php5.6 php5.6 php5.6-common php5.6-dom
php5.6-cli php5.6-dev php-pear php5.6-json php5.6-imagick php5.6-imap
php5.6-intl php5.6-mcrypt php5.6-memcached php5.6-redis php5.6-mongo
php5.6-xdebug php5.6-curl php5.6-mysqlnd php5.6-xcache php5.6-mcrypt
php5.6-oauth php5.6-gd \  
&& mv /etc/php /etc/php_origin \  
&& mkdir -p $PHP5_CONFIG_FOLDER \  
&& rm $PHP5_CONFIG_FOLDER -rf \  
&& ln -s /etc/php_origin $PHP5_CONFIG_FOLDER \  
&& ln -s $PHP5_CONFIG_FOLDER /etc/php \  
&& mkdir -p $PHP5_LOG_FOLDER \  
&& rm $PHP5_LOG_FOLDER -rf \  
&& ln -s $PHP5_LOG_FOLDER /var/log/php \  
&& sed -e "s/^short_open_tag .*$/short_open_tag = Off/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^disable_functions .*$/disable_functions = disk_free_space,
diskfreespace, leak, system, shell_exec, escapeshellcmd, proc_nice, dl,
symlink, show_source/g" -i /etc/php_origin/5.6/apache2/php.ini \  
&& export TMP=`echo "error_log\=${PHP5_LOG_FOLDER}/error.log" | sed -e
"s/\//\\\\\\\\\\\\\\\\\//g"` \  
&& sed -e "s/^\;error_log = php_errors\\.log$/$TMP/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^asp_tags .*$/asp_tags = Off/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^expose_php .*$/expose_php = Off/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^display_errors .*$/display_errors = Off/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^display_startup_errors .*$/display_startup_errors = Off/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^log_errors .*$/log_errors = On/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^memory_limit .*$/memory_limit = 150M/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^allow_url_fopen .*$/allow_url_fopen = On/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^allow_url_include .*$/allow_url_include = On/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^\;date\\.timezone .*$/date\\.timezone = \"Asia\/Ho_Chi_Minh\"/g"
-i /etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^safe_mode .*$/safe_mode = Off/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& sed -e "s/^max_execution_time .*$/max_execution_time = 60/g" -i
/etc/php_origin/5.6/apache2/php.ini \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN apt-get install -y git  
  
# Install Supervisor  
ENV SUPERVISOR_CONFIG_FOLDER $VOLUME_DATA/supervisor/config  
ENV SUPERVISOR_LOG_FOLDER $VOLUME_DATA/supervisor/log  
  
  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get -y update && \  
apt-get -y install supervisor && \  
apt-get -y clean  
# Create the Configuration Folder Structure  
RUN mv /etc/supervisor /etc/supervisor_origin && \  
mkdir -p $SUPERVISOR_CONFIG_FOLDER && \  
rm $SUPERVISOR_CONFIG_FOLDER -rf && \  
ln -s /etc/supervisor_origin $SUPERVISOR_CONFIG_FOLDER && \  
ln -s $SUPERVISOR_CONFIG_FOLDER /etc/supervisor && \  
# Create the Log Folder Structure  
rm /var/log/supervisor -rf && \  
mkdir -p $SUPERVISOR_LOG_FOLDER && \  
rm $SUPERVISOR_LOG_FOLDER -rf && \  
ln -s $SUPERVISOR_LOG_FOLDER /var/log/supervisor  
  
# start CRON using supervisord  
ADD z1_init_cron.sh /opt/docker-before-run/  
RUN mv /etc/crontab /etc/crontab_origin && \  
mkdir -p $VOLUME_CONFIG/cron && \  
ln -s /etc/crontab_origin $VOLUME_CONFIG/cron/crontab && \  
ln -s $VOLUME_CONFIG/cron/crontab /etc/crontab && \  
chmod +x /opt/docker-before-run/z1_init_cron.sh && \  
echo "\  
[program:cron] \n\  
command=/usr/sbin/cron -f \n\  
autostart=true \n\  
autorestart=true \  
" >> /etc/supervisor/conf.d/cron.conf && \  
echo "\  
[program:apache2] \n\  
command=/bin/bash -c \"source /etc/apache2/envvars && exec /usr/sbin/apache2
-DFOREGROUND\" \n\  
autostart=true \n\  
autorestart=true \  
" >> /etc/supervisor/conf.d/apache2.conf  
  
COPY parameters.yml /opt/  
COPY config.yml /opt/  
COPY z2_init_toranproxy.sh /opt/docker-before-run  
  
RUN sed -e "s/^\s+toran_host:.*$/toran_host: ${APP_TORAN_HOST}/g" -i
/opt/parameters.yml  
  
EXPOSE 443  
EXPOSE 80  
COPY run.sh /run.sh  
CMD ["/run.sh"]  
  

