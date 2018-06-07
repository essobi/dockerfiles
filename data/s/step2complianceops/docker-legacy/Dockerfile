FROM phusion/baseimage:0.9.16  
# Regenerate SSH host keys.  
# RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Set Timezone  
RUN echo "America/New_York" | sudo tee /etc/timezone  
RUN sudo dpkg-reconfigure --frontend noninteractive tzdata  
  
# remove any old packages  
#RUN add-apt-repository --remove ppa:ondrej/php-5.6  
# Update Package List  
RUN apt-get update  
  
# Install Some PPAs  
RUN apt-get install -y vim curl wget build-essential software-properties-
common git pdftk  
RUN apt-add-repository -y ppa:nginx/stable  
RUN apt-add-repository -y ppa:ondrej/php  
  
RUN apt-get update  
  
#------------------------------  
# Install and configure PHP-FPM  
#------------------------------  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends
php5.6-fpm php5.6-cli php5.6-dev php-pear \  
php5.6-mysqlnd php5.6-pgsql php5.6-sqlite \  
php5.6-apcu php5.6-json php5.6-curl php5.6-gd \  
php5.6-gmp php5.6-imap php5.6-mcrypt \  
php5.6-memcached php5.6-redis \  
php5.6-mbstring php5.6-xml  
  
# build the daemon  
RUN mkdir /etc/service/phpfpm  
ADD .deploy/devops/build/daemons/phpfpm.sh /etc/service/phpfpm/run  
RUN chmod +x /etc/service/phpfpm/run  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
RUN echo "/root/ec2/.composer" > /etc/container_environment/COMPOSER_HOME  
  
#-------------------------------  
# Install New Relic PHP Agent  
#-------------------------------  
# Install Agent  
RUN wget -O - https://download.newrelic.com/548C16BF.gpg | sudo apt-key add -  
RUN sudo sh -c 'echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list'  
RUN apt-get update  
RUN apt-get install -y --force-yes newrelic-php5  
  
#------------------------------  
# Install and configure Nginx  
#------------------------------  
RUN apt-get install -y --force-yes nginx  
  
# Create default app directory  
RUN rm -rf /var/www  
ADD . /var/www  
  
ADD .deploy/devops/build/default /etc/nginx/sites-available/default  
ADD .deploy/devops/build/http_realip.conf /etc/nginx/conf.d/http_realip.conf  
  
# Shell script must run the daemon without letting it daemonize/fork it  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# build the daemon  
RUN mkdir /etc/service/nginx  
ADD .deploy/devops/build/daemons/nginx.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
  
#------------------------------  
# Install and configure Queue  
#------------------------------  
RUN mkdir /etc/service/queue  
ADD .deploy/devops/build/daemons/queue.sh /etc/service/queue/run  
RUN chmod +x /etc/service/queue/run  
  
#------------------------------  
# Startup Scripts  
#------------------------------  
# create script directory  
RUN mkdir -p /etc/my_init.d  
  
# add scripts  
ADD .deploy/devops/build/scripts/envars.sh /etc/my_init.d/01_envars.sh  
ADD .deploy/devops/build/scripts/composer.sh /etc/my_init.d/02_composer.sh  
ADD .deploy/devops/build/scripts/permissions.sh
/etc/my_init.d/03_permissions.sh  
ADD .deploy/devops/build/scripts/php-fpm.sh /etc/my_init.d/04_php-fpm.sh  
ADD .deploy/devops/build/scripts/newrelic.sh /etc/my_init.d/05_newrelic.sh  
ADD .deploy/devops/build/scripts/cron.sh /etc/my_init.d/06_cron.sh  
ADD .deploy/devops/build/scripts/dot_env.sh /etc/my_init.d/07_dot_env.sh  
  
# update script permissions  
RUN chmod +x /etc/my_init.d/*  
  
#------------------------------  
# Finish and Cleanup  
#------------------------------  
EXPOSE 80  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

