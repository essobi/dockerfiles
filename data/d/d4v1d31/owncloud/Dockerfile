FROM alpine  
MAINTAINER David Elvers "david@d4v1d.eu"  
# set default variables for owncloud install  
ENV DBTYPE mysql  
ENV DBNAME owncloud  
ENV DBHOST mysqldb  
ENV DBUSER root  
ENV DBPASS password  
ENV ADMIN admin  
ENV ADMINPASS password  
  
# update alpine linux  
RUN apk update && apk upgrade  
RUN apk add bash unzip  
  
# add owncloud dependencies  
RUN apk add nginx php-fpm \  
php-ctype php-dom php-gd \  
php-iconv php-json php-xml \  
php-posix php-xmlreader \  
php-zip php-zlib \  
php-pdo php-pdo_mysql php-pdo_sqlite php-mysql\  
php-curl php-bz2 php-intl php-mcrypt php-openssl\  
php-ldap php-imap php-ftp\  
php-pcntl  
  
# clean apk cache  
RUN rm -rf /var/cache/apk/*  
  
# add owncloud  
ADD https://download.owncloud.org/community/owncloud-9.0.0.zip /tmp/  
RUN unzip -qq /tmp/owncloud-9.0.0.zip -d /  
  
# add contacts, calander and documents app  
ADD
https://github.com/owncloud/contacts/releases/download/v1.1.0.0/contacts.tar.gz
/tmp/  
RUN tar -xzf /tmp/contacts.tar.gz -C /owncloud/apps/  
ADD
https://github.com/owncloud/documents/releases/download/v0.12.0/documents.zip
/tmp/  
RUN unzip -qq /tmp/documents.zip -d /owncloud/apps/  
ADD
https://github.com/owncloud/calendar/releases/download/v1.0/calendar.tar.gz
/tmp/  
RUN tar -xzf /tmp/calendar.tar.gz -C /owncloud/apps/  
  
# clean  
RUN rm /tmp/*  
  
# fix rights  
WORKDIR /owncloud/  
RUN chown -R root:nginx ./  
#RUN chown -R nginx:nginx ./tmp  
RUN chown -R nginx:nginx ./config  
  
# add nginx config  
ADD nginx.conf /etc/nginx/  
ADD php-fpm.conf /etc/php/  
ADD php.ini /etc/php/  
  
# add some script  
ADD start.sh /usr/bin/  
RUN chmod +x /usr/bin/start.sh  
ADD set_rights.sh /usr/bin/  
RUN chmod +x /usr/bin/set_rights.sh  
RUN ln /owncloud/occ /usr/bin/  
  
VOLUME ["/owncloud/config/","/owncloud/data/"]  
  
EXPOSE 80  
ENTRYPOINT ["start.sh"]  

