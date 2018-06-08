FROM centos:7  
MAINTAINER Sergey Bondarev <s.bondarev@southbridge.ru>  
  
RUN rpm -Uvh http://rpms.southbridge.ru/southbridge-rhel7-stable.rpm && \  
rpm -Uvh http://yum.newrelic.com/pub/newrelic/el5/x86_64/newrelic-
repo-5-3.noarch.rpm && \  
yum -y install epel-release southbridge-php56-release && \  
yum -y update && \  
yum -y install supervisor bash cronie ssmtp nginx maxscale wget zip bzip2
p7zip php php-fpm php-xdebug php-opcache php-mcrypt php-gd php-mbstring php-
intl php-mysqlnd php-pdo php-xml php-pecl-zip php-process php-pecl-redis-2.2.7
php-pecl-memcache php-pecl-memcached dos2unix php-bcmath php-soap newrelic-
php5 && \  
(echo; echo "opcache.enable_cli=1") >> /etc/php.d/10-opcache.ini && \  
##  
# Install composer  
# source: https://getcomposer.org/download/  
##  
curl -L https://getcomposer.org/installer -o composer-setup.php && php
composer-setup.php && rm composer-setup.php && mv composer.phar
/usr/local/bin/composer && chmod +rx /usr/local/bin/composer && \  
\  
rm -f /etc/yum.repos.d/*.rpm; rm -fr /var/cache/*; rm -f
/etc/php.d/15-xdebug.ini && \  
mkdir -p /var/cache/nginx && \  
localedef -i ru_RU -f UTF-8 ru_RU.UTF-8 && \  
for x in `ls /usr/share/locale | grep -v -e ^en -e ^ru -e ^locale`; do rm -fr
/usr/share/locale/$x; done && \  
for x in `ls /usr/share/i18n/locales/ | grep -v -e ^en -e ^ru`; do rm -fr
/usr/share/i18n/locales/$x; done && \  
rm -fr /usr/share/locale/ca* /usr/share/locale/den /usr/share/locale/men
/usr/share/locale/wen /usr/share/locale/zen && \  
cd /usr/lib/locale && localedef \--list-archive | grep -v -e ^en -e ^ru |
xargs localedef \--delete-from-archive && \  
mv -f locale-archive locale-archive.tmpl && \  
build-locale-archive && \  
rm -f /etc/localtime && \  
ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \  
echo "date.timezone = Europe/Moscow" > /etc/php.d/991-timezone.ini && \  
rm -fr /usr/share/doc/* /usr/share/man/* /usr/share/groff/* /usr/share/info/*
/usr/share/lintian/* /usr/share/linda/* /var/cache/man/* && \  
echo "Done install..."  
# test tools  
#RUN yum -y install mc bind-utils  
  
RUN NR_INSTALL_SILENT='true' NR_INSTALL_PATH='/usr/sbin' newrelic-install
install  
  
##  
# Add Project files like nginx and php-fpm processes and configs  
# Also custom scripts and bashrc  
##  
COPY system-root/ /  
  
ENV TERM="xterm" \  
DB_HOST="" \  
DB_NAME="" \  
DB_USER=""\  
DB_PASSWORD=""\  
# Set defaults which can be overriden  
DB_PORT="3306" \  
# Set defaults for redis  
REDIS_PORT="6379" \  
REDIS_DATABASE="0" \  
REDIS_SCHEME="tcp" \  
# Cronlock is used to stop simultaneous cronjobs in clusterised environments  
CRONLOCK_HOST="" \  
# This is for your project root  
PROJECT_ROOT="/srv/www/php-app"\  
# This is used by nginx and php-fpm  
WEB_ROOT="/srv/www/php-app/htdocs"\  
# This can be overidden by you, it's just default for us  
TZ="Europe/Moscow"  
  
WORKDIR /srv/www  
EXPOSE 80  
ENTRYPOINT ["/docker-entrypoint.sh"]  

