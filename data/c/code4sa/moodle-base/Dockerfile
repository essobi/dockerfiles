## Roughly based on https://github.com/jda/docker-moodle/  
  
FROM ubuntu:14.04  
MAINTAINER Code For South Africa <info@code4sa.org>  
  
ADD ./foreground.sh /etc/apache2/foreground.sh  
  
RUN DEBIAN_FRONTEND=noninteractive\  
apt-get update && \  
apt-get -y install \  
apache2 \  
curl \  
libapache2-mod-php5 \  
libcurl3 \  
libcurl3-dev \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-intl \  
php5-pgsql \  
php5-xmlrpc \  
postfix \  
pwgen \  
supervisor \  
unzip \  
wget && \  
echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | \  
tee /etc/apt/sources.list.d/newrelic.list && \  
wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
apt-get update && \  
apt-get -y install newrelic-php5 && \  
rm -f /var/www/html/index.html && \  
cd /tmp && \  
wget https://download.moodle.org/download.php/direct/stable31/moodle-
latest-31.tgz && \  
tar -xf moodle-latest-31.tgz && \  
mv /tmp/moodle/* /var/www/html/ && \  
chown -R www-data:www-data /var/www/html && \  
chmod +x /etc/apache2/foreground.sh  

