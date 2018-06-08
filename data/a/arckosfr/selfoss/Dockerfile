FROM xataz/nginx:latest  
LABEL version="20160810/1"  
MAINTAINER arckosfr <contact@lemark.xyz>  
  
ENV UID=991 GID=991 VER=2.15  
EXPOSE 80  
VOLUME /var/www/html/data  
  
ADD
https://github.com/SSilence/selfoss/releases/download/${VER}/selfoss-${VER}.zip
/tmp/  
ADD files/run.sh /  
ADD files/cron /etc/periodic/15min/selfoss  
  
RUN apk add --update \  
musl \  
php5-fpm \  
php5-json \  
php5-zlib \  
php5-xml \  
php5-dom \  
php5-curl \  
php5-gd \  
php5-iconv \  
php5-mcrypt \  
php5-pdo \  
php5-pdo_sqlite\  
php5-ctype \  
unzip && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /var/www/html && \  
unzip /tmp/selfoss-*.zip -d /var/www/html && \  
cp -R /var/www/html/data /var/www/html/bkp &&\  
rm /tmp/selfoss-*.zip && \  
sed -ri 's#max_execution_time = 30#max_execution_time = 300#'
/etc/php5/php.ini && \  
chmod +x /run.sh /etc/periodic/15min/selfoss  
  
COPY files/selfoss.conf /sites-enabled/  
COPY files/php-fpm.conf /etc/php5/  
  
CMD ["tini","--","/run.sh"]  

