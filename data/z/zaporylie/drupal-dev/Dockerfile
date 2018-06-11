FROM zaporylie/drupal:1  
MAINTAINER Jakub Piasecki <jakub@piaseccy.pl>  
  
# Development tools  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install
php5-dev php5-xdebug libpcre3-dev libssh2-php \  
&& sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php5/fpm/php.ini \  
&& sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php5/cli/php.ini \  
&& sed -ri 's/^memory_limit\s*=\s*.*/memory_limit = 192M/g'
/etc/php5/fpm/php.ini \  
&& sed -ri 's/^max_execution_time\s*=\s*.*/max_execution_time = 300/g'
/etc/php5/fpm/php.ini \  
&& mkdir -p /app/output \  
&& chown www-data:www-data /app/output \  
&& echo 'xdebug.remote_enable = 1' >> /etc/php5/mods-available/xdebug.ini \  
&& echo 'xdebug.remote_connect_back = 1' >> /etc/php5/mods-
available/xdebug.ini \  
&& echo 'xdebug.idekey = "vagrant"' >> /etc/php5/mods-available/xdebug.ini \  
&& echo 'xdebug.remote_log="/var/log/xdebug/xdebug.log"' >> /etc/php5/mods-
available/xdebug.ini \  
&& echo 'xdebug.profiler_enable_trigger = 1' >> /etc/php5/mods-
available/xdebug.ini \  
&& echo 'xdebug.profiler_output_dir="/app/output"' >> /etc/php5/mods-
available/xdebug.ini \  
&& echo 'xdebug.trace_enable_trigger = 1' >> /etc/php5/mods-
available/xdebug.ini \  
&& echo 'xdebug.trace_output_dir = "/app/output"' >> /etc/php5/mods-
available/xdebug.ini \  
&& echo 'xdebug.max_nesting_level = 1000' >> /etc/php5/mods-
available/xdebug.ini \  
&& composer global require drupal/coder \  
&& echo 'alias drupalcs="phpcs
--standard=$HOME/.composer/vendor/drupal/coder/coder_sniffer/Drupal
--extensions=\"php,module,inc,install,test,profile,theme,js,css,info,txt\""'
>> /root/.bashrc \  
&& echo 'alias drupalcs-bp="phpcs
--standard=$HOME/.composer/vendor/drupal/coder/coder_sniffer/DrupalPractice
--extensions=\"php,module,inc,install,test,profile,theme,js,css,info,txt\""'
>> /root/.bashrc \  
&& echo 'alias drupalcs-fix="phpcbf
--standard=$HOME/.composer/vendor/drupal/coder/coder_sniffer/Drupal
--extensions=\"php,module,inc,install,test,profile,theme,js,css,info,txt\""'
>> /root/.bashrc \  
&& mkdir -p /app/output  
  
RUN wget -O - https://packagecloud.io/gpg.key | sudo apt-key add - \  
&& echo "deb http://packages.blackfire.io/debian any main" | sudo tee
/etc/apt/sources.list.d/blackfire.list \  
&& sudo apt-get update \  
&& sudo apt-get install blackfire-php \  
&& echo "extension=blackfire.so\nblackfire.agent_socket=\${BLACKFIRE_PORT}" >
/etc/php5/mods-available/blackfire.ini  
  
COPY ./conf /root/conf/  
  
ENV DRUPAL_TEST_CS 0  
ENV DRUPAL_TEST_CS_PATH "/app/drupal"  
ENV DEV_MODULE XDEBUG  
  
EXPOSE 80 22 9000  

