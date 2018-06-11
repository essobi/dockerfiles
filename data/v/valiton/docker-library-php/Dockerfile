FROM php:5.6  
RUN apt-get update && \  
apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev mcrypt libxml2-dev libxslt-dev libicu-dev xml-core mysql-client
unzip && \  
docker-php-ext-install iconv mcrypt && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd && \  
docker-php-ext-install mysql mysqli pdo pdo_mysql bcmath xml xsl intl soap &&
\  
echo "date.timezone=$TIMEZONE" > /usr/local/etc/php/conf.d/timezone.ini  
  
RUN mkdir /tmp/zendguardloader  
RUN cd /tmp/zendguardloader  
RUN apt-get install -y wget  
RUN cd /tmp/zendguardloader && \  
/usr/bin/wget http://downloads.zend.com/guard/7.0.0/zend-loader-
php5.6-linux-x86_64_update1.tar.gz && \  
tar xvf zend-loader-php5.6-linux-x86_64_update1.tar.gz && \  
cd `php -i | grep ^extension_dir | cut -d' ' -f 5` && \  
cp /tmp/zendguardloader/zend-loader-php5.6-linux-x86_64/ZendGuardLoader.so .
&& \  
echo zend_extension=$(php -i | grep ^extension_dir | cut -d' ' -f
5)/ZendGuardLoader.so > /usr/local/etc/php/conf.d/zendguardloader.ini && \  
echo zend_loader.enable=1 >> /usr/local/etc/php/conf.d/zendguardloader.ini &&
\  
echo zend.ze1_compatibility_mode = Off >>
/usr/local/etc/php/conf.d/zendguardloader.ini && \  
echo zend_loader.disable_licensing = 0 >>
/usr/local/etc/php/conf.d/zendguardloader.ini && \  
echo zend_loader.obfuscation_level_support = 3 >>
/usr/local/etc/php/conf.d/zendguardloader.ini && \  
rm -rf /tmp/zendguardloader/  
RUN cat /usr/local/etc/php/conf.d/zendguardloader.ini  
RUN php -v  
  
CMD ["echo", "'Done'"]  

