FROM ubuntu:16.04  
MAINTAINER Niclas Hedam <niclas@frax.dk>  
WORKDIR /var/www  
  
# Install apache, PHP, and supplimentary programs. openssh-server, curl, and
lynx-cur are for debugging the container.  
RUN apt-get update -y && apt-get -y install software-properties-common python-
software-properties curl nano wget \  
&& LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php \  
&& apt-get update \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && echo
"deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && apt-get update -y &&
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
apache2 php7.1 php7.1-mysql php7.1-json php7.1-mbstring php7.1-gd php7.1-dom
php7.1-curl php7.1-zip libapache2-mod-php7.1 lynx-cur git supervisor wget
python-pip nodejs iputils-ping yarn mysql-client-5.7 \  
&& pip install supervisor-stdout && pip install devcron  
  
ADD apache2.conf /etc/apache2/apache2.conf  
ADD vhost.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Enable apache mods.  
RUN a2enmod php7.1; a2enmod expires; a2enmod rewrite; a2dismod mpm_event;
a2enmod mpm_prefork; sed -i "s/error_reporting = .*$/error_reporting = E_ERROR
| E_WARNING | E_PARSE/" /etc/php/7.1/apache2/php.ini  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
#Composer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --snapshot \  
&& rm -f /tmp/composer-setup.*  

