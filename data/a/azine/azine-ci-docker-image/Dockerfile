FROM ubuntu:16.04  
# set environment variables  
ENV ROOTPASSWD 'INSERT_A_PASSWORD_HERE'  
ENV LANG 'en_US.UTF-8'  
ENV LANGUAGE 'en_US:en'  
ENV LC_ALL 'en_US.UTF-8'  
# add some files to the image  
ADD required-packages /tmp/required-packages  
ADD timezone /etc/timezone  
ADD bashpimp ~/.bashrc  
  
# update package repositories  
RUN apt-get update \  
  
# install some packages required for next step  
&& apt-get install -y wget software-properties-common tzdata debconf locales \  
  
# generate locales & set timezone  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure -f noninteractive tzdata \  
  
# add php5-repo and mysql-5.6 repos & update package repositories  
&& add-apt-repository -y ppa:ondrej/php \  
&& add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe' \  
&& apt-get update \  
  
# prepare for mysql & phpmyadmin installation  
&& echo "mysql-server-5.6 mysql-server/root_password password ${ROOTPASSWD}" |
debconf-set-selections \  
&& echo "mysql-server-5.6 mysql-server/root_password_again password
${ROOTPASSWD}" | debconf-set-selections \  
&& echo "phpmyadmin phpmyadmin/dbconfig-install boolean true" | debconf-set-
selections \  
&& echo "phpmyadmin phpmyadmin/app-password-confirm password ${ROOTPASSWD}" |
debconf-set-selections \  
&& echo "phpmyadmin phpmyadmin/mysql/admin-pass password ${ROOTPASSWD}" |
debconf-set-selections \  
&& echo "phpmyadmin phpmyadmin/mysql/app-pass password ${ROOTPASSWD}" |
debconf-set-selections \  
&& echo "phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2" |
debconf-set-selections \  
  
  
# install from package list & clear chache  
&& apt-get install -y $(cat /tmp/required-packages) \  
&& apt-get clean \  
  
  
# install npm packages  
&& npm install uglifyjs -g \  
&& npm install uglifycss -g \  
  
  
# install pear modules  
# && pear config-set auto_discover 1  
# && pear channel-discover pear.phpqatools.org  
# && pear install phpqatools/PHP_CodeBrowser  
# && pear install pear/Text_Highlighter-beta  
# && pear install --alldeps PHP_CodeSniffer  
# && pear channel-discover components.ez.no  
# && pear install ezc/ConsoleTools  
# && pear channel-discover pear.phpdoc.org  
# && pear install --alldeps phpdoc/phpDocumentor-alpha  
# && pecl config-set preferred_state beta  
# && pecl install imagick  
# && pecl config-set preferred_state stable  
# && pear channel-discover pear.phpmd.org  
# && pear channel-discover pear.pdepend.org  
# && pear install --alldeps phpmd/PHP_PMD  
# install composer  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv -f composer.phar /usr/local/bin/composer \  
&& chmod a+x /usr/local/bin/composer \  
  
  
# install phpunit  
&& wget https://phar.phpunit.de/phpunit.phar \  
&& chmod +x phpunit.phar \  
&& mv phpunit.phar /usr/local/bin/phpunit  
  
  
# add apache php & xdebug configuration  
ADD php.ini /etc/php/5.6/cli/php.ini  
ADD php.ini /etc/php/5.6/apache2/php.ini  
ADD xdebug.ini /etc/php/5.6/mods-available/xdebug.ini  
ADD application.apache.conf /etc/apache2/sites-available/000-application.conf  
ADD application-ssl.apache.conf /etc/apache2/sites-available/000-application-
ssl.conf  
  
# enable apache virtual hosts for application, application-ssl  
RUN make-ssl-cert generate-default-snakeoil --force-overwrite \  
&& chmod -f a+rx /etc/ssl/private/* /etc/ssl/certs/* \  
&& a2enmod ssl vhost_alias rewrite \  
&& a2dissite default-ssl.conf \  
&& a2dissite 000-default.conf \  
&& a2ensite 000-application-ssl.conf \  
&& a2ensite 000-application.conf \  
  
# setup app folders  
&& mkdir /app  
WORKDIR /app  
  
# expose ports for http, https & mysql  
EXPOSE 80 443 3306  

