FROM webdevops/php-apache:ubuntu-15.04  
  
RUN echo > /opt/docker/bin/service.d/dnsmasq.d/10-init.sh && \  
echo > /opt/docker/etc/supervisor.d/dnsmasq.conf && \  
echo > /opt/docker/bin/service.d/dnsmasq.sh  
  
RUN cd /tmp/ && \  
curl -O http://downloads.zend.com/guard/7.0.0/zend-loader-
php5.6-linux-x86_64.tar.gz && \  
tar zxvf zend-loader-php5.6-linux-x86_64.tar.gz && \  
mkdir -p /usr/local/lib/php/extensions/ && \  
cp zend-loader-php5.6-linux-x86_64/* /usr/lib/php5/20131226/ && \  
echo 'zend_extension=ZendGuardLoader.so' >> /etc/php5/fpm/php.ini && \  
echo 'zend_extension=ZendGuardLoader.so' >> /etc/php5/cli/php.ini && \  
rm -rf zend-loader-php5.6-linux-x86_64*  

