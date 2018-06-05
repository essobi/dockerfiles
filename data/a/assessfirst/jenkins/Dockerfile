FROM visibilityspots/jenkins-docker  
  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y sudo wget curl locales gnupg
make gettext git php-gettext \  
apt-transport-https lsb-release ca-certificates && \  
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
&& \  
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >>
/etc/apt/sources.list && \  
apt-get -q autoremove && \  
apt-get -q clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -f /var/cache/apt/*.bin  
  
# TIMEZONE  
RUN echo "Europe/Paris" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
RUN export LANGUAGE=fr_FR.UTF-8 && \  
export LANG=fr_FR.UTF-8 && \  
export LC_ALL=fr_FR.UTF-8 && \  
locale-gen fr_FR.UTF-8 && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
#node  
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -  
  
# INSTALL PHP  
RUN apt-get update; apt-get install -y php7.1 php7.1-cli php7.1-gd php7.1-imap
php7.1-mbstring php7.1-xml php7.1-curl php7.1-bz2 \  
php7.1-mcrypt php7.1-zip php7.1-mysqlnd php7.1-intl nodejs && \  
apt-get -q autoremove && \  
apt-get -q clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -f /var/cache/apt/*.bin  
  
#COMPOSER  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --install-dir=/usr/local/bin
--filename=composer  
  
# PRESTISSIMO  
RUN composer global require hirak/prestissimo  
  
#GULP  
RUN npm install -g gulp  

