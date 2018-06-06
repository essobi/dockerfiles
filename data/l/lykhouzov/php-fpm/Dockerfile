FROM centos:7  
  
MAINTAINER Aleksandr Lykhouzov <lykhouzov@gmail.com>  
  
ENV MAGE_ROOT=/var/www/html/magento MAGE_CRON_EXPR="*/10 * * * *"
HOSTNAME=magento.loc SERVER_LISTEN_PORT=80 TERM=xterm  
COPY ./docker-entrypoint.sh /  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm; \  
rpm --import https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7;\  
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm; \  
rpm --import https://mirror.webtatic.com/yum/RPM-GPG-KEY-webtatic-el7;\  
yum -y swap -- remove fakesystemd -- install systemd systemd-libs; \  
yum -y update; yum clean all; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;\  
  
yum install -y crontabs which git yum-cron logrotate rsyslog \  
php70w-fpm php70w-devel php70w-ftp php70w-opcache php70w-imap php70w-mysql \  
php70w-curl php70w-gd php70w-mcrypt php70w-xmlrpc \  
php70w-xsl php70w-pear php70w-phar php70w-posix php70w-mbstring \  
php70w-soap php70w-xmlreader php70w-xmlwriter \  
php70w-zlib php70w-zip php70w-dom \  
php70w-tokenizer php70w-ctype php70w-intl \  
g++ make gcc gcc-c++ sqlite-devel \  
&& /usr/bin/yum clean all \  
#Xdebug setup  
&& curl -O https://xdebug.org/files/xdebug-2.5.0.tgz \  
&& tar -zxvf xdebug-2.5.0.tgz && rm -f xdebug-2.5.0.tgz \  
&& cd xdebug-2.5.0 && phpize \  
&& ./configure && make && make install \  
&& echo 'zend_extension=xdebug.so;' >> /etc/php.d/xdebug.ini \  
&& echo 'xdebug.remote_enable=1;' >> /etc/php.d/xdebug.ini \  
&& echo 'xdebug.remote_host=127.0.0.1;' >> /etc/php.d/xdebug.ini \  
&& echo 'xdebug.remote_connect_back=1 # Not safe for production servers;' >>
/etc/php.d/xdebug.ini\  
&& echo 'xdebug.remote_port=9900;' >> /etc/php.d/xdebug.ini\  
&& echo 'xdebug.remote_handler=dbgp;' >> /etc/php.d/xdebug.ini\  
&& echo 'xdebug.remote_mode=req;' >> /etc/php.d/xdebug.ini\  
&& echo 'xdebug.remote_autostart=0;' >> /etc/php.d/xdebug.ini\  
&& cd ../ && rm -rf xdebug-2.5.0 \  
#&& rm -f /etc/php-fpm.d/www.conf \  
&& sed -i 's/listen = 127.0.0.1:9000/listen = 0.0.0.0:9000/g' /etc/php-
fpm.d/www.conf \  
&& sed -i 's/listen.allowed_clients = 127.0.0.1/;listen.allowed_clients =
127.0.0.1/g' /etc/php-fpm.d/www.conf \  
&& sed -i 's/;php_flag\\[display_errors\\] = off/php_flag\\[display_errors\\]
= on/g' /etc/php-fpm.d/www.conf \  
&& sed -i 's/;php_admin_value\\[error_log\\] = \/var\/log\/fpm-
php.www.log/php_admin_value[error_log] = \/var\/log\/php-fpm\/www-error.log/g'
/etc/php-fpm.d/www.conf \  
&& sed -i 's/;php_admin_flag\\[log_errors\\] =
on/php_admin_flag\\[log_errors\\] = on/g' /etc/php-fpm.d/www.conf \  
&& sed -i 's/;catch_workers_output = yes/catch_workers_output = yes/g'
/etc/php-fpm.d/www.conf \  
## yum-cron  
&& sed -i 's/;apply_updates = no/apply_updates = yes/g' /etc/yum/yum-cron.conf
\  
# Install ioncube  
&& curl -O
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& tar -zxvf ioncube_loaders_lin_x86-64.tar.gz \  
&& cp ioncube/ioncube_loader_lin_7.0.so ioncube/ioncube_loader_lin_7.0_ts.so
/usr/lib64/php/modules/ \  
&& rm -rf ioncube ioncube_loaders_lin_x86-64.tar.gz \  
&& echo 'zend_extension=ioncube_loader_lin_7.0.so' > /etc/php.d/ioncube.ini \  
# forward request and error logs to docker log collector  
&& rm -f /var/log/php-fpm/www-error.log \  
&& ln -sf /dev/stdout /var/log/php-fpm/www-error.log \  
&& systemctl enable php-fpm.service \  
&& chown root:root /docker-entrypoint.sh && chmod 775 /docker-entrypoint.sh \  
&& curl http://files.magerun.net/n98-magerun-latest.phar -o /usr/bin/magerun \  
&& chmod +x /usr/bin/magerun \  
&& cd /etc/ && git clone -b php7 https://github.com/phpredis/phpredis.git \  
&& cd phpredis && /usr/bin/phpize \  
&& ./configure && make && make install \  
&& cp /etc/phpredis/modules/redis.so /usr/lib64/php/modules/ \  
&& echo 'extension=redis.so' > /etc/php.d/redis.ini \  
&& cd / && rm -rf /etc/phpredis \  
### logrotate repo  
&& echo $'compress\n\  
"/var/www/html/magento/var/log/*.log"{\n\  
rotate 15\n\  
size 5M\n\  
daily\n\  
missingok\n\  
notifempty\n\  
sharedscripts\n\  
olddir archive/\n\  
}\n\  
' | tee /etc/logrotate.d/magento  
  
VOLUME [ "/sys/fs/cgroup" ]  
EXPOSE 9000 9900  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/sbin/init"]  

