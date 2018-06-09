FROM tribalnova/ubuntu:1204  
MAINTAINER Nicolas Degardin <ndegardin@tribalnova.com>  
  
# Tools  
RUN echo 'deb http://ppa.launchpad.net/svn/ppa/ubuntu precise main' >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key A2F4C039  
RUN apt-get update && apt-get install -y nginx php5-cli php5 php5-fpm
php5-mcrypt php5-xdebug curl git subversion  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# SSH configuration  
ADD files/ssh/ssh_config /etc/ssh/ssh_config  
  
# Subversion  
ADD files/subversion/servers /etc/subversion/servers  
  
# nginx / PHP  
ADD files/nginx/nginx.conf /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
RUN mkdir /etc/nginx/sites-enabled/default  
ADD files/nginx/default.conf /etc/nginx/sites-enabled/default.conf  
ADD files/nginx/php.conf /etc/nginx/include.d/php.conf  
ADD files/php/xdebug.ini /etc/php5/conf.d/xdebug.ini  
  
# PHP-FPM  
ADD files/php/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ADD files/php/www.conf /etc/php5/fpm/pool.d/www.conf  
ADD files/php/php53.ini /etc/php5/fpm/php.ini  
RUN cp /etc/php5/fpm/php.ini /etc/php5/cli/php.ini  
  
# For Vagrant shared folder compatibility (UID/GID 1000 by default).  
# To be less arbitrary, the shared folder id could be guessed by using
something like "uid=`stat -c '%u' /var/www/shared_folder`"  
RUN usermod -u 1000 www-data  
#RUN groupmod -g 1000 www-data  
RUN mkdir -p /var/log/web  
RUN mkdir -p /var/www  
RUN chown -R www-data /var/log/web  
  
# XHPROF  
ENV XHPROF_GUI 0  
ADD files/xhgui/xhgui.conf /opt/docker/xhprof/xhgui.conf  
ADD files/xhgui/config.php /opt/docker/xhprof/config.php  
ADD files/xhprofio/xhprofio.conf /opt/docker/xhprof/xhprofio.conf  
ADD files/xhprofio/config.inc.php /opt/docker/xhprof/config.inc.php  
  
# Setup/startup scripts  
ADD files/install-web-php53-xhprof.sh /opt/docker/install-web-xhprof.sh  
ADD files/install-web-php53-devtools.sh /opt/docker/install-web-devtools.sh  
ADD files/startup-web-php53-dev.sh /opt/docker/startup-web-dev.sh  
ADD files/startup.sh /opt/docker/startup.sh  
  
EXPOSE 80  
EXPOSE 443  
WORKDIR ["/var/www"]  
VOLUME ["/var/log/web"]  
ENTRYPOINT ["/opt/docker/startup.sh"]  
CMD nginx

