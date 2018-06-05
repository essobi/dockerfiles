FROM subak/php:5.4-base  
  
RUN curl -o /usr/local/lib/php/extensions/no-debug-non-
zts-20100525/ioncube.tgz
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz  
RUN tar zxfv /usr/local/lib/php/extensions/no-debug-non-
zts-20100525/ioncube.tgz -C /usr/local/lib/php/extensions/no-debug-non-
zts-20100525/ && \  
rm /usr/local/lib/php/extensions/no-debug-non-zts-20100525/ioncube.tgz  
RUN echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20100525/ioncube/ioncube_loader_lin_5.4.so' >
/usr/local/etc/php/conf.d/ext-ioncube.ini && \  
echo 'session.gc_probability = 0' >> /usr/local/etc/php/conf.d/ext-ioncube.ini  

