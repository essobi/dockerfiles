FROM adite/base  
MAINTAINER tescom <tescom@atdt01410.com>  
  
# Install base packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -yq upgrade && \  
apt-get -yq install \  
mysql-client \  
apache2 \  
libapache2-mod-php5 \  
php5-apcu \  
php5-cli \  
php5-curl \  
php5-gd \  
php5-mcrypt \  
php5-mysql \  
php5-intl \  
php5-json \  
php5-sqlite \  
php5-mongo \  
php5-xsl \  
zip unzip gpsbabel acl && \  
rm -rf /var/lib/apt/lists/*  
  
# Add apache default.conf  
ADD default-vhost.conf /etc/apache2/sites-available/000-default.conf  
  
# Enable apache modules  
RUN a2enmod rewrite php5 vhost_alias headers  
  
# Add php config  
ADD php.ini /etc/php5/mods-available/overrides.ini  
  
# Enable php modules  
RUN php5enmod apcu curl gd mcrypt mongo mysql intl json xsl overrides/99  
  
# Install composer and drush  
RUN export COMPOSER_HOME=/usr/local/composer && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
composer global require drush/drush:6.5.0 && \  
composer global install && \  
ln -s /usr/local/composer/vendor/drush/drush/drush /usr/local/bin/drush  
  
# Fix drush dependency  
ADD http://download.pear.php.net/package/Console_Table-1.1.3.tgz /tmp/  
RUN tar xzf /tmp/Console_Table-1.1.3.tgz -C
/usr/local/composer/vendor/drush/drush/lib && \  
rm /tmp/Console_Table-1.1.3.tgz  
  
# Add verify_make drush module  
RUN mkdir -p /usr/share/drush/commands && \  
curl https://raw.githubusercontent.com/insiders/drush-verify-
make/master/verify_make.drush.inc -o
/usr/share/drush/commands/verify_make.drush.inc  
  
# Install dockerize  
RUN curl -sSL
https://github.com/jwilder/dockerize/releases/download/v0.0.2/dockerize-linux-
amd64-v0.0.2.tar.gz | tar -C /usr/local/bin -xzf -  
  
# Add run file  
ADD apache-run.sh /apache-run.sh  
RUN chmod 0500 /apache-run.sh  
  
#VOLUME ["/var/www"]  
#VOLUME ["/etc/apache2/sites-enabled"]  
EXPOSE 80  
#CMD ["/usr/sbin/apache2ctl", "-D", " FOREGROUND"]  
CMD ["/apache-run.sh"]  

