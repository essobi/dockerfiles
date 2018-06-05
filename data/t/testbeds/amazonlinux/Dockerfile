FROM testbeds/amazonlinux:2014.03  
ENV STACK_PHP_EXTENSION_DIR=/usr/lib64/php/modules \  
STACK_PHP_CONFIG_DIR=/etc/php.d \  
STACK_APACHE_LOG=/var/log/httpd/error_log \  
STACK_APACHE_ENV_FILE=/etc/sysconfig/httpd \  
STACK_APACHE_CONFIG_DIR=/etc/httpd/conf.d  
  
RUN sed -i 's/releasever=latest/#releasever=latest/' /etc/yum.conf  
RUN rpm --rebuilddb && yum -y install unzip wget sudo which ca-certificates
httpd php php-pecl-memcache php-pecl-memcached php-mysql php-pgsql php-pdo  
RUN yum clean all -y  
  
# disable requiretty for sudo  
RUN echo "Defaults !requiretty" >> /etc/sudoers  
  
# apache and php  
RUN printf '#!/bin/bash\nif [ -z "$(pgrep -f "httpd -k")" ]; then httpd -k
start; sleep 1; fi\n' > /bin/stack_apache_start  
RUN printf '#!/bin/bash\npkill -f httpd; while [ -n "$(pgrep -f "httpd -k")"
]; do sleep 1; done\n' > /bin/stack_apache_stop  
RUN chmod +x /bin/stack_apache_*  
  
# bats framework  
RUN wget https://github.com/sstephenson/bats/archive/master.zip  
RUN unzip master.zip  
RUN bats-master/install.sh /usr/local  
RUN rm -rf bats-master/ master.zip  
  
# php-redis (build from source)  
RUN rpm --rebuilddb && yum -y install php-devel gcc  
RUN wget https://github.com/phpredis/phpredis/zipball/master -O phpredis.zip  
RUN unzip phpredis.zip  
RUN cd phpredis-phpredis-* && phpize && ./configure && make && make install  
RUN echo "extension=redis.so" > $STACK_PHP_CONFIG_DIR/redis.ini  
RUN rm -rf phpredis*  
  
# php-mongo  
RUN rpm --rebuilddb && yum -y install php-devel php-pear gcc make openssl-
devel  
RUN pecl install mongo  
RUN echo "extension=mongo.so" > $STACK_PHP_CONFIG_DIR/mongo.ini  

