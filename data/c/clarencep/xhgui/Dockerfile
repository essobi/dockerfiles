FROM clarencep/lap7:centos7  
  
COPY . /root/docker  
  
RUN mkdir -p /etc/httpd/vhosts \  
&& cp -f /root/docker/httpd/0_default.conf /etc/httpd/vhosts/ \  
&& echo 'Include vhosts/*.conf' >> /etc/httpd/conf/httpd.conf \  
&& /usr/sbin/httpd -t \  
&& yum install -y zip unzip php71w-pear php71w-devel gcc make wget \  
&& yum install -y supervisor \  
&& cp /root/docker/supervisord/* /etc/supervisord.d \  
&& yum install -y mongodb-server openssl-devel \  
&& pecl install mongodb \  
&& echo 'extension=mongodb.so' > /etc/php.d/mongodb.ini \  
&& mkdir -p /var/www/xhgui \  
&& mkdir -p /data/mongodb \  
&& wget -O /tmp/xhgui.zip
https://github.com/clarencep/xhgui/archive/master.zip \  
&& unzip /tmp/xhgui.zip -d /tmp \  
&& cp -R /tmp/xhgui-master/* /var/www/xhgui/ \  
&& wget -O /tmp/composer.phar https://getcomposer.org/composer.phar \  
&& cd /var/www/xhgui \  
&& chown -R apache:apache * \  
&& php /tmp/composer.phar install --no-dev \  
&& php /tmp/composer.phar require \--update-no-dev alcaeus/mongo-php-
adapter:1.0 \  
&& chmod a+w cache storage \  
&& yum erase -y zip unzip php71w-pear php71w-devel gcc make wget \  
&& find /var/log -type f -print0 | xargs -0 rm -rf /root/docker
/root/.composer /tmp/* \  
&& yum clean all  
  
EXPOSE 80 27017  
  
CMD /usr/bin/supervisord -n  

