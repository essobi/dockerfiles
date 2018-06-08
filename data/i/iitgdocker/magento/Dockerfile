FROM iitgdocker/php:5.6  
MAINTAINER "The Ignorant IT Guy" <iitg@gmail.com>  
  
RUN yum -y --nogpgcheck install \  
wget \  
which \  
php-ioncube-loader \  
php-xml \  
php-mysql \  
php-mcrypt \  
php-gd \  
php-soap \  
php-mbstring \  
php-pecl-redis && \  
yum clean all  
  
# Change PHP settings as recommended by Magento  
RUN sed -i -e 's/^max_execution_time = .*/max_execution_time = 18000/g' \  
-e 's/^zlib.output_compression = Off/; enable resulting html compression\nzlib.output_compression = on/g' /etc/php.ini  
RUN echo -e "; disable automatic session start\n; before autoload was
initialized\nflag session.auto_start = off\n\n; disable user agent
verification to not break multiple image upload\nsuhosin.session.cryptua =
Off" >>/etc/php.d/40-suhosin.ini  
  
# Copy magento installer to container  
COPY magento.tar.gz /tmp/magento.tar.gz  
  
# Download and install magento  
RUN tar zxvf /tmp/magento.tar.gz -C /tmp >/dev/null && \  
mv /tmp/magento/* /tmp/magento/.htaccess /var/www/html && \  
rm -rvf /tmp/magento*  
  
# TLSv1 is disabled, make sure we tell CURL not to use it and instead use TLS
1.2.  
# Magento connect uses curl and will fail without this change.  
RUN sed -i "s/\$this->curlOption(CURLOPT_SSL_CIPHER_LIST,
'TLSv1');/#\$this->curlOption(CURLOPT_SSL_CIPHER_LIST, 'TLSv1');\\\n
\$this->curlOption(CURLOPT_SSLVERSION, CURL_SSLVERSION_TLSv1_2);/g"
/var/www/html/downloader/lib/Mage/HTTP/Client/Curl.php  
  
RUN chown -R apache:apache /var/www/html  
  
# Make the cron files executable.  
# For some dumb reason these need to be world executable  
# for some modules like stock in the channel to shut up.  
RUN chmod 755 /var/www/html/cron.sh  
RUN chmod 755 /var/www/html/cron.php  
  
# stock in the channel keeps looking for php5 which of course, doesn't exist.  
# added redirect...  
RUN ln -s /usr/bin/php /usr/bin/php5  
  
EXPOSE 80  
EXPOSE 443  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
CMD ["/run.sh"]  

