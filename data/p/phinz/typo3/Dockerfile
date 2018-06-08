FROM phinz/typo3:7-latest  
  
# install xdebug  
RUN pecl install xdebug  
  
# set recommended xdebug.ini settings  
# ! Please beware that remote_connect_back is on this !  
# ! will setup all the remote_ip and remote_port setup !  
# ! automatic. !  
RUN { \  
echo 'zend_extension="xdebug.so"'; \  
echo 'xdebug.remote_enable=1'; \  
echo 'xdebug.remote_connect_back=1'; \  
echo 'xdebug.max_nesting_level=400'; \  
echo 'xdebug.remote_log="/var/log/xdebug.log"'; \  
} > /usr/local/etc/php/conf.d/xdebug.ini  
  
# cleanup  
RUN rm -rf /tmp/* /var/tmp/*

