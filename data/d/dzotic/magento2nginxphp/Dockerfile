FROM devbeta/nginx-php1.8:1.8.0-php5.6.20  
MAINTAINER Jelastic  
RUN echo "clear_env = no" >> /etc/php-fpm.conf;  
RUN echo "1"; curl -fsSL "https://goo.gl/qTYpG8" -o
/tmp/libmcrypt-2.5.8-13.el7.x86_64.rpm;\  
curl -fsSL "https://goo.gl/k0ysMD" -o
/tmp/viber-4.2.2.6-8.el7.nux.x86_64.rpm;\  
yum -y install /tmp/viber-4.2.2.6-8.el7.nux.x86_64.rpm;  
RUN sed -i 's|;extension=intl.so|extension=intl.so|g' /etc/php.ini;  
RUN sed -i
's|.*extension=mysqlnd_ms.so|extension=mysqlnd_ms.so\nmysqlnd_ms.multi_master
= 1|g' /etc/php.ini;  
RUN sed -i 's|.*mysqlnd_ms.enable = 1|mysqlnd_ms.enable = 1|g' /etc/php.ini;  
RUN sed -i
's|.*mysqlnd_ms.config_file.*|mysqlnd_ms.config_file=/var/lib/jelastic/mysqlnd_ms.json|g'
/etc/php.ini;  
RUN curl -fsSL "https://goo.gl/akqUn3" -o /var/lib/jelastic/mysqlnd_ms.json;  
RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf2;\  
curl -fsSL "https://goo.gl/w4rDJD" -o /etc/nginx/nginx.conf;  
RUN sed -i 's|pm = dynamic|pm = ondemand|g' /etc/php-fpm.conf;\  
sed -i 's|pm.max_children = 50|pm.max_children = 16\npm.process_idle_timeout =
60s|g' /etc/php-fpm.conf;\  
sed -i 's|; Jelastic autoconfiguration mark||g' /etc/php-fpm.conf;  
RUN sed -i 's|.*extension=xsl.so|extension=xsl.so|g' /etc/php.ini;  
RUN sed -i 's|.*extension=gd.so|extension=gd.so|g' /etc/php.ini;\  
sed -i 's|memory_limit = 128M|memory_limit = 512M|g' /etc/php.ini;\  
sed -i
'465s|;session.save_path="tcp.*|session.save_path="tcp://MEMCACHE_1:11211,
tcp://MEMCACHE_2:11211"|g' /etc/php.ini;\  
sed -i '462s/;extension=memcache.so/extension=memcache.so/' /etc/php.ini;\  
sed -i '464s/;session.save_handler = memcache/session.save_handler =
memcache/' /etc/php.ini;\  
sed -i '468s/memcache.allow_failover = 0/memcache.allow_failover = 1/'
/etc/php.ini;\  
sed -i '469s/memcache.max_failover_attempts =
20;/memcache.max_failover_attempts = 2;/' /etc/php.ini;\  
sed -i '472i memcache.redundancy = 1;' /etc/php.ini;\  
sed -i '473i memcache.session_redundancy = 3;' /etc/php.ini;\  
sed -i '474i memcache.hash_strategy = "consistent";' /etc/php.ini;\  
sed -i 's|.*zend_extension=opcache.so|zend_extension=opcache.so|g'
/etc/php.ini;\  
sed -i 's|.*opcache.memory_consumption.*|opcache.memory_consumption = 512M ;
The size of the shared memory storage used by OPcache, in megabytes|g'
/etc/php.ini;\  
sed -i 's|.*opcache.max_accelerated_files.*|opcache.max_accelerated_files =
100000 ; Only numbers between 200 and 100000 are allowed. number in the set of
prime numbers that is bigger than the configured value|g' /etc/php.ini;\  
sed -i 's|.*opcache.validate_timestamps.*|opcache.validate_timestamps=1|g'
/etc/php.ini;\  
sed -i 's|.*opcache.revalidate_freq.*|opcache.revalidate_freq=2 ; How often to
check script timestamps for updates, in seconds. 0 will result in OPcache
checking for updates on every request. This configuration directive is ignored
if opcache.validate_timestamps is disabled.|g' /etc/php.ini;\  
sed -i 's|.*opcache.save_comments.*|opcache.save_comments=0|g' /etc/php.ini;\  
sed -i 's|.*opcache.enable_file_override.*|opcache.enable_file_override=0|g'
/etc/php.ini;\  
sed -i 's|.*opcache.enable_cli.*|opcache.enable_cli=0|g' /etc/php.ini;\  
sed -i
's|.*opcache.max_wasted_percentage.*|opcache.max_wasted_percentage=10|g'
/etc/php.ini;\  
sed -i
's|.*opcache.interned_strings_buffer.*|opcache.interned_strings_buffer=128|g'
/etc/php.ini;\  
sed -i
's|.*opcache.optimization_level.*|opcache.optimization_level=0x7FFFBFFF|g'
/etc/php.ini;  

