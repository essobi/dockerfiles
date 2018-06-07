FROM eboraas/apache-php:latest  
  
RUN cd /tmp \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends unzip curl php5-curl php5-gd
php5-mysql \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -o ioncube.tar.gz
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& tar -xvvzf ioncube.tar.gz \  
&& mkdir /usr/lib/php5/ioncube \  
&& mv ioncube/ioncube_loader_lin_5.6.so /usr/lib/php5/ioncube/ioncube.so \  
&& rm -Rf ioncube.tar.gz ioncube \  
&& bash -c "echo zend_extension = /usr/lib/php5/ioncube/ioncube.so >
/etc/php5/apache2/conf.d/00-ioncube.ini" \  
&& bash -c "echo zend_extension = /usr/lib/php5/ioncube/ioncube.so >
/etc/php5/cli/conf.d/00-ioncube.ini" \  
&& sed --in-place "s/^upload_max_filesize.*$/upload_max_filesize = 10M/"
/etc/php5/apache2/php.ini  

