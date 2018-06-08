FROM phusion/baseimage:0.9.16  
# Regenerate SSH host keys and allow ssh.  
RUN rm -f /etc/service/sshd/down  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Set Timezone  
RUN echo "America/New_York" | sudo tee /etc/timezone  
RUN sudo dpkg-reconfigure --frontend noninteractive tzdata  
  
# Update Package List  
RUN apt-get update  
  
# Install Some PPAs  
RUN apt-get install -y vim curl wget build-essential software-properties-
common git  
RUN apt-add-repository -y ppa:ondrej/php5-5.6  
  
#------------------------------  
# Install and configure PHP-FPM  
#------------------------------  
RUN apt-get update && apt-get install -y --force-yes php5-fpm php5-cli
php5-dev php-pear \  
php5-mysqlnd php5-pgsql php5-sqlite \  
php5-apcu php5-json php5-curl php5-gd \  
php5-gmp php5-imap php5-mcrypt \  
php5-memcached php5-redis \  
supervisor  
  
# Shell script must run the daemon without letting it daemonize/fork it  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf  
  
# Set listen port  
RUN sed -i 's/listen = \/var\/run\/php5-fpm.sock/listen = 9000/'
/etc/php5/fpm/pool.d/www.conf  
  
# FPM Tweaks  
RUN sed -i "s/;emergency_restart_threshold = 0/emergency_restart_threshold =
10/" /etc/php5/fpm/php-fpm.conf  
RUN sed -i "s/;emergency_restart_interval = 0/emergency_restart_interval =
1m/" /etc/php5/fpm/php-fpm.conf  
RUN sed -i "s/;process_control_timeout = 0/process_control_timeout = 10s/"
/etc/php5/fpm/php-fpm.conf  
  
# Security  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini  
  
# Add build scripts  
RUN mkdir /opt/build-scripts  
COPY build/scripts/max_children.sh /opt/build-scripts/max_children.sh  
COPY build/scripts/composer.sh /opt/build-scripts/composer.sh  
COPY build/scripts/file_permissions.sh /opt/build-scripts/file_permissions.sh  
COPY build/scripts/supervisor.sh /opt/build-scripts/supervisor.sh  
  
RUN chmod 777 /opt/build-scripts/file_permissions.sh  
RUN chmod 777 /opt/build-scripts/supervisor.sh  
RUN chmod 777 /opt/build-scripts/composer.sh  
  
# Add our crontab file  
ADD build/cron/crons.conf /root/crons.conf  
  
# PM Setup  
RUN sed -i "s/pm.max_children = 5/pm.max_children = 15/"
/etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/pm.start_servers = 2/pm.start_servers = 10/"
/etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/pm.min_spare_servers = 1/pm.min_spare_servers = 5/"
/etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/pm.max_spare_servers = 3/pm.max_spare_servers = 15/"
/etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/;pm.max_requests = 500/pm.max_requests = 500/"
/etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/;security.limit_extensions = .php .php3 .php4
.php5/security.limit_extensions = .php .html/" /etc/php5/fpm/pool.d/www.conf  
  
# build the daemon  
RUN mkdir /etc/service/phpfpm  
ADD build/daemons/phpfpm.sh /etc/service/phpfpm/run  
RUN chmod +x /etc/service/phpfpm/run  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
RUN echo "/root/ec2/.composer" > /etc/container_environment/COMPOSER_HOME  
  
#------------------------------  
# Startup Scripts  
#------------------------------  
# create script directory  
RUN mkdir -p /etc/my_init.d  
  
# add scripts  
ADD build/scripts/envars.sh /etc/my_init.d/01_envars.sh  
ADD build/scripts/php-fpm.sh /etc/my_init.d/02_php-fpm.sh  
  
# update script permissions  
RUN chmod +x /etc/my_init.d/*  
  
# Use the crontab file to start our cron jobs  
RUN crontab /root/crons.conf  
  
#------------------------------  
# Finish and Cleanup  
#------------------------------  
EXPOSE 9000  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

