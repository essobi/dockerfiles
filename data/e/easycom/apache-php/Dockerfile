FROM easycom/base:jessie  
MAINTAINER Frédéric T <xmedias@easycom.digital>  
  
ENV TOOLS_HTPASSWD easycom:P@ssw0rd  
ENV OPCACHE_MAX_MEMORY "128"  
ENV OPCACHE_MAX_FILES "12000"  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y --no-
install-recommends ca-certificates wget \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## ================================  
## Add non-free to source.list  
## ================================  
RUN echo 'deb http://ftp.fr.debian.org/debian/ jessie main contrib non-free' >
/etc/apt/sources.list \  
&& echo 'deb-src http://ftp.fr.debian.org/debian/ jessie main contrib non-
free' >> /etc/apt/sources.list \  
&& echo 'deb http://security.debian.org/ jessie/updates main' >>
/etc/apt/sources.list \  
&& echo 'deb-src http://security.debian.org/ jessie/updates main' >>
/etc/apt/sources.list  
  
## ================================  
## Add dotdeb repository to sources to get last version of apache and php for
jessie  
## ================================  
RUN echo 'deb http://packages.dotdeb.org jessie all' >
/etc/apt/sources.list.d/dotdeb.list \  
&& echo 'deb-src http://packages.dotdeb.org jessie all' >>
/etc/apt/sources.list.d/dotdeb.list \  
&& wget https://www.dotdeb.org/dotdeb.gpg \  
&& apt-key add dotdeb.gpg  
  
#RUN apt-get purge -y --auto-remove ca-certificates wget  
# =========================================  
# Update apt-cache and install Apache2  
# =========================================  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y --no-install-
recommends install \  
build-essential \  
unzip \  
ssmtp \  
apache2 \  
libapache2-mod-fastcgi \  
php7.0-fpm \  
php7.0-json \  
php7.0-dev \  
php7.0-imagick \  
php7.0-gd \  
php7.0-mcrypt \  
php7.0-curl \  
php7.0-mysql \  
php7.0-bz2 \  
php7.0-redis \  
php7.0-mbstring \  
php7.0-xml \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# =========================================  
# Activate Apache2 mod_rewrite  
# =========================================  
#-> Make the directory 'default' for the default vhost and tools directory to
handle some tools  
RUN mkdir -p /var/www/logs /var/www/_tools /var/www/htdocs \  
&& DEBIAN_FRONTEND=noninteractive a2enmod actions rewrite deflate headers  
  
# Configure apache to be in production mode for better security  
ADD ./common/security.conf /etc/apache2/conf-available/security.conf  
RUN a2enconf security  
  
# Configure servername to avoid alert in console  
RUN echo "ServerName $(cat /etc/hostname)" > /etc/apache2/conf-
available/servername.conf \  
&& a2enconf servername  
  
# Copy configuration file to secure /tools path by an htaccess // see
entrypoint to configure login/pass  
ADD ./common/common_tools.conf /etc/apache2/conf-available/common_tools.conf  
RUN a2enconf common_tools  
  
# Remove default configuration for virtuals hosts  
RUN mkdir _bak \  
&& mv /etc/apache2/sites-available/* _bak/ \  
&& mv _bak /etc/apache2/sites-available/ \  
&& rm -Rf /etc/apache2/sites-enabled/*  
  
# Add our configuration for default virtual host  
ADD ./common/vhost-default.conf /etc/apache2/sites-available/default.conf  
RUN chmod 655 /etc/apache2/sites-available/default.conf \  
&& a2ensite default  
  
# Copy "php7-fpm.conf" in Apache2 conf-available > Enable php for all sites  
ADD ./php7-fpm.conf /etc/apache2/conf-available/php7-fpm.conf  
ADD ./php7-fpm.pool /etc/php/7.0/fpm/pool.d/www.conf  
RUN chmod 655 /etc/apache2/conf-available/php7-fpm.conf \  
&& a2enconf php7-fpm  
  
# Install opcache monitoring interface  
RUN cd /tmp \  
&& wget https://github.com/PeeHaa/OpCacheGUI/archive/master.zip -O
OpCacheGUI.zip \  
&& unzip OpCacheGUI.zip && mv OpCacheGUI-* OpCacheGUI \  
&& echo -e "<?php\nnamespace OpCacheGUI;\nuse
OpCacheGUI\I18n\FileTranslator;\nuse
OpCacheGUI\Network\Router;\nerror_reporting(E_ALL);\nini_set('display_errors',
1);\nini_set('log_errors', 0);\nini_set('date.timezone',
'Europe/Paris');\n\$translator = new FileTranslator(__DIR__ . '/texts',
'fr');\n\$uriScheme = Router::QUERY_STRING;\n\$login = [ 'username' => '',
'password' => '', 'whitelist' => [ '*' ] ];" > OpCacheGUI/init.example.php \  
&& sed -i "s/-e <?php/<?php/" OpCacheGUI/init.example.php \  
&& mv OpCacheGUI /var/www/_tools/opcache  
  
RUN echo "<?php phpinfo();" > /var/www/_tools/info.php  
  
RUN cd /tmp \  
&& wget https://www.phpmyadmin.net/downloads/phpMyAdmin-latest-all-
languages.tar.gz \  
&& tar xfz phpMyAdmin* \  
&& rm phpMyAdmin*.tar.gz \  
&& mv phpMyAdmin* /var/www/_tools/pma  
ADD ./common/config.inc.php /var/www/_tools/pma/  
  
# Install Apache Pagespeed module  
RUN cd /tmp \  
&& wget https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-
stable_current_amd64.deb \  
&& dpkg -i mod-pagespeed-*.deb \  
&& apt-get -f install \  
&& rm mod-pagespeed-*.deb  
  
# =========================================  
# Reload Apache2  
# =========================================  
RUN mv /var/www/html/index.html /var/www/htdocs/ && rm -Rf /var/www/html \  
&& service php7.0-fpm stop && service apache2 stop && service php7.0-fpm start
&& service apache2 start  
  
# =========================================  
# Configure sendmail  
# =========================================  
# It permits to send email with custom sender address  
RUN sed -i s,#FromLineOverride=YES,FromLineOverride=YES, /etc/ssmtp/ssmtp.conf  
  
ADD docker-entrypoint.sh /usr/local/bin/  
ADD default-cmd.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh /usr/local/bin/default-cmd.sh  
  
## ================================  
## LAUNCH PART  
## ================================  
# Expose sockets  
EXPOSE 80 443  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
# Launch run script  
CMD ["default-cmd.sh"]  

