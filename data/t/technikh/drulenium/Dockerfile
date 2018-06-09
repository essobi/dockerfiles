FROM debian:jessie  
MAINTAINER Wouter Admiraal <wad@wadmiraal.net>  
ENV DEBIAN_FRONTEND noninteractive  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install packages. http://serverfault.com/questions/690639/api-get-error-
reading-from-server-under-docker  
RUN apt-get clean  
RUN apt-get update  
RUN apt-get install -y \  
vim \  
git \  
apache2 \  
php5-cli \  
php5-mysql \  
php5-gd \  
php5-curl \  
php5-xdebug \  
libapache2-mod-php5 \  
curl \  
mysql-server \  
mysql-client \  
openssh-server \  
phpmyadmin \  
wget \  
unzip \  
imagemagick \  
postfix \  
supervisor  
RUN apt-get clean  
  
# Install Composer.  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install Drush 8 (master) as phar.  
RUN wget http://files.drush.org/drush.phar  
RUN mv drush.phar /usr/local/bin/drush && chmod +x /usr/local/bin/drush  
  
# Setup PHP.  
RUN sed -i 's/display_errors = Off/display_errors = On/'
/etc/php5/apache2/php.ini  
RUN sed -i 's/display_errors = Off/display_errors = On/' /etc/php5/cli/php.ini  
  
# Setup Apache.  
# In order to run our Simpletest tests, we need to make Apache  
# listen on the same port as the one we forwarded. Because we use  
# 8080 by default, we set it up for that port.  
RUN sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf  
RUN sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www/'
/etc/apache2/sites-available/000-default.conf  
RUN echo "Listen 8080" >> /etc/apache2/ports.conf  
RUN sed -i 's/VirtualHost \\*:80/VirtualHost \\*:\\*/' /etc/apache2/sites-
available/000-default.conf  
RUN a2enmod rewrite  
  
# Setup PHPMyAdmin  
RUN echo -e "\n# Include PHPMyAdmin configuration\nInclude
/etc/phpmyadmin/apache.conf\n" >> /etc/apache2/apache2.conf  
RUN sed -i -e "s/\/\/
\$cfg\\['Servers'\\]\\[\$i\\]\\['AllowNoPassword'\\]/\$cfg\\['Servers'\\]\\[\$i\\]\\['AllowNoPassword'\\]/g"
/etc/phpmyadmin/config.inc.php  
RUN sed -i -e
"s/\$cfg\\['Servers'\\]\\[\$i\\]\\['\\(table_uiprefs\|history\\)'\\].*/\$cfg\\['Servers'\\]\\[\$i\\]\\['\1'\\]
= false;/g" /etc/phpmyadmin/config.inc.php  
  
# Setup MySQL, bind on all addresses.  
RUN sed -i -e 's/^bind-address\s*=\s*127.0.0.1/#bind-address = 127.0.0.1/'
/etc/mysql/my.cnf  
  
# Setup SSH.  
RUN echo 'root:root' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd  
RUN mkdir -p /root/.ssh/ && touch /root/.ssh/authorized_keys  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# Setup Supervisor.  
RUN echo -e '[program:apache2]\ncommand=/bin/bash -c "source
/etc/apache2/envvars && exec /usr/sbin/apache2
-DFOREGROUND"\nautorestart=true\n\n' >> /etc/supervisor/supervisord.conf  
RUN echo -e '[program:mysql]\ncommand=/usr/bin/pidproxy
/var/run/mysqld/mysqld.pid /usr/sbin/mysqld\nautorestart=true\n\n' >>
/etc/supervisor/supervisord.conf  
RUN echo -e '[program:sshd]\ncommand=/usr/sbin/sshd -D\n\n' >>
/etc/supervisor/supervisord.conf  
  
# Setup XDebug.  
RUN echo "xdebug.max_nesting_level = 300" >>
/etc/php5/apache2/conf.d/20-xdebug.ini  
RUN echo "xdebug.max_nesting_level = 300" >>
/etc/php5/cli/conf.d/20-xdebug.ini  
  
# Install Drupal.  
RUN rm -rf /var/www  
RUN cd /var && \  
drush dl drupal-7.44 && \  
mv /var/drupal* /var/www  
RUN mkdir -p /var/www/sites/default/files && \  
chmod a+w /var/www/sites/default -R && \  
mkdir /var/www/sites/all/modules/contrib -p && \  
mkdir /var/www/sites/all/modules/custom && \  
mkdir /var/www/sites/all/themes/contrib -p && \  
mkdir /var/www/sites/all/themes/custom && \  
chown -R www-data:www-data /var/www/  
RUN /etc/init.d/mysql start && \  
cd /var/www && \  
drush site-install -y standard --db-url=mysql://root:@localhost/drupal --site-
name=Drulenium --account-pass=admin  
RUN /etc/init.d/mysql start && \  
cd /var/www && \  
drush dl drulenium -y && \  
drush en drulenium drulenium_local_selenium -y && \  
drush vset --yes drulenium_vr_release_imagemagick_path '/usr/bin' && \  
drush vset --yes drulenium_vr_config_image_server_opt 'local' && \  
drush en libraries -y && \  
drush vr-download-webdriver && \  
drush vr-download-blockly && \  
drush dl admin_menu devel && \  
drush en -y admin_menu  
  
EXPOSE 80 3306 22  
CMD exec supervisord -n  

