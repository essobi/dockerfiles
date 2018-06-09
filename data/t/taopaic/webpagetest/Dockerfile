FROM ubuntu:15.10  
MAINTAINER TaopaiC <pctao.tw@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y apache2 php5-gd php5-curl php-apc libapache2-mod-php5 \  
imagemagick libjpeg-progs libimage-exiftool-perl sqlite3 \  
ffmpeg curl && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee
/etc/apt/sources.list.d/newrelic.list && \  
curl https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
echo newrelic-php5 newrelic-php5/application-name string "NEWRELIC_APP_NAME" |
debconf-set-selections && \  
echo newrelic-php5 newrelic-php5/license-key string "NEWRELIC_LICENSE_KEY" |
debconf-set-selections && \  
apt-get update && \  
apt-get install -y newrelic-php5 && \  
rm -rf /var/lib/apt/lists/* && \  
php5dismod newrelic  
  
ENV NEWRELIC_APP_NAME "WebPageTest"  
ENV NEWRELIC_LICENSE_KEY ""  
ENV WPT_VERSION 2.19  
RUN DIR=$(mktemp -d) && \  
rm /var/www/html/index.html | true && \  
cd ${DIR} && \  
curl -L -Os https://github.com/WPO-
Foundation/webpagetest/archive/WebPageTest-${WPT_VERSION}.tar.gz && \  
tar xvf WebPageTest-${WPT_VERSION}.tar.gz && \  
cd webpagetest-WebPageTest-${WPT_VERSION} && \  
cp -r www/* /var/www/html/ && \  
rm -rf ${DIR}  
  
RUN a2enmod expires headers rewrite php5  
  
RUN sed -ri '\  
s/zlib.output_compression = Off/zlib.output_compression = On/g; \  
s/upload_max_filesize = 2M/upload_max_filesize = 10M/g; \  
s/post_max_size = 8M/post_max_size = 15M/g; \  
s/memory_limit = 128M/memory_limit = -1/g' /etc/php5/apache2/php.ini  
  
RUN mkdir -p \  
/var/www/html/tmp \  
/var/www/html/dat \  
/var/www/html/results \  
/var/www/html/work/jobs \  
/var/www/html/work/video \  
/var/www/html/logs \  
/var/log/webpagetest \  
/data/archive && \  
chown www-data:www-data \  
/var/www/html/tmp \  
/var/www/html/dat \  
/var/www/html/results \  
/var/www/html/work/jobs \  
/var/www/html/work/video \  
/var/www/html/logs \  
/var/log/webpagetest \  
/data/archive && \  
chmod 775 \  
/var/www/html/tmp \  
/var/www/html/dat \  
/var/www/html/results \  
/var/www/html/work/jobs \  
/var/www/html/work/video \  
/var/www/html/logs \  
/var/log/webpagetest \  
/data/archive  
  
COPY locations.ini /var/www/html/settings/locations.ini  
COPY connectivity.ini /var/www/html/settings/connectivity.ini  
COPY settings.ini /var/www/html/settings/settings.ini  
  
COPY apache_default.conf /etc/apache2/conf-enabled/000_default.conf  
  
VOLUME ["/var/www/html/results", "/var/www/html/dat" "/data/archive"]  
EXPOSE 80  
CMD /bin/bash -c '\  
[ ! -z "$NEWRELIC_LICENSE_KEY" ] && sed -ri "\  
s/newrelic.appname =.*/newrelic.appname = \"$NEWRELIC_APP_NAME\"/g; \  
s/newrelic.license =.*/newrelic.license = \"$NEWRELIC_LICENSE_KEY\"/g; \  
" /etc/php5/mods-available/newrelic.ini && php5enmod newrelic || php5dismod
newrelic && \  
chown www-data:www-data /var/www/html/results && \  
source /etc/apache2/envvars && exec /usr/sbin/apache2 -DFOREGROUND'  

