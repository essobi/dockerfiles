# from https://www.drupal.org/requirements/php#drupalversions  
FROM php:5.6-apache  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev
libxml2-dev \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip soap  
  
RUN apt-get -y install vim php5-xdebug php5-dev php-pear bzip2 git php-apc
php5-memcache \  
memcached curl imagemagick php5-imagick mysql-client rsyslog net-tools
php5-common \  
graphviz pv php5-xsl  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get -yq install nullmailer  
  
RUN echo 'local0.* /var/log/drupal.log' >> /etc/rsyslog.conf  
  
# Make mail relay work  
#RUN echo "dc_eximconfig_configtype='internet'" > /etc/exim4/update-
exim4.conf.conf && \  
# echo "dc_other_hostnames=''" >> /etc/exim4/update-exim4.conf.conf && \  
# echo "dc_local_interfaces=''" >> /etc/exim4/update-exim4.conf.conf && \  
# echo "dc_readhost=''" >> /etc/exim4/update-exim4.conf.conf && \  
# echo "dc_relay_domains='*'" >> /etc/exim4/update-exim4.conf.conf && \  
# echo "dc_minimaldns='false'" >> /etc/exim4/update-exim4.conf.conf && \  
# echo "dc_relay_nets='0.0.0.0/48'" >> /etc/exim4/update-exim4.conf.conf && \  
# echo "dc_smarthost=''" >> /etc/exim4/update-exim4.conf.conf && \  
# echo "CFILEMODE='644'" >> /etc/exim4/update-exim4.conf.conf && \  
# echo "dc_use_split_config='false'" >> /etc/exim4/update-exim4.conf.conf && \  
# echo "dc_hide_mailname=''" >> /etc/exim4/update-exim4.conf.conf && \  
# echo "dc_mailname_in_oh='true'" >> /etc/exim4/update-exim4.conf.conf && \  
# echo "dc_localdelivery='mail_spool'" >> /etc/exim4/update-exim4.conf.conf &&
\  
# echo "local-development.dev" >> /etc/mailname && \  
# /usr/sbin/update-exim4.conf  
# Route mail to mailcatcher SMTP via nullmailer  
RUN echo "mail smtp -p 1025" > /etc/nullmailer/remotes  
  
WORKDIR /var/www/html  
  
# Xhprof  
ADD ./conf/xhprof.ini /usr/local/etc/php/conf.d/xhprof.ini  
RUN pecl install xhprof-0.9.4  
RUN php5enmod xhprof  
RUN mkdir /tmp/xhprof  
RUN chmod 777 /tmp/xhprof  
RUN chown www-data.www-data /tmp/xhprof  
RUN chown www-data.www-data /usr/local/lib/php/xhprof_html  
  
# Drush  
RUN mkdir /root/.drush  
ADD ./conf/drushrc.php /root/.drush/drushrc.php  
# http://whaaat.com/installing-drush-8-using-composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> /root/.bashrc  
RUN export PATH="$HOME/.composer/vendor/bin:$PATH"  
RUN composer global require drush/drush:8.0.0-beta14  
RUN /root/.composer/vendor/bin/drush dl drush_situs  
  
# Adding php.ini conf.  
ADD ./conf/php.ini /usr/local/etc/php/php.ini  
ADD ./conf/php.cli.ini /etc/php5/cli/php.ini  
RUN echo 'export PHPRC=/etc/php5/cli/php.ini' >> /root/.bashrc  
  
# Adding xdebug conf and startup script.  
ADD conf/xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
ADD start.sh /start.sh  
RUN (chmod 750 /start.sh)  

