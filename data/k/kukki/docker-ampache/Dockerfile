FROM alpine  
MAINTAINER Jimmy Koo <kukkiz@gmail.com>  
  
ENV aVersion 3.8.2  
#This is MySQL admin password  
ENV MYSQL_PASS fAk3Pa55w0Rd  
  
RUN apk add --update apache2 apache2-utils  
RUN apk add mysql mysql-client  
RUN apk add php5  
RUN apk add php5-xml php5-json php5-pdo php5-pdo_mysql php5-curl php5-iconv
php5-apache2 php5-openssl php5-zlib php5-gd php5-gettext  
RUN apk add openrc wget unzip inotify-tools  
  
WORKDIR /  
  
# Switch these two for local debug purpose  
ADD
https://github.com/ampache/ampache/releases/download/${aVersion}/ampache-${aVersion}_all.zip
/ampache_all.zip  
#COPY ampache_all.zip /ampache_all.zip  
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh  
ADD run.sh /run.sh  
ADD my.cnf /etc/mysql/my.cnf  
ADD 001-ampache.conf /etc/apache2/conf.d/001-ampache.conf  
  
RUN mkdir -p /etc/mysql/conf.d && \  
unzip -q /ampache_all.zip -d /var/www/localhost/ampache && \  
chown -R apache:www-data /var/www && \  
chown -R mysql:mysql /var/lib/mysql && \  
chmod 755 /*.sh && \  
sed -i 's/#\\(.*rewrite_module.*\\)/\1/g' /etc/apache2/httpd.conf && \  
echo 'PidFile /var/run/apache2.pid' >> /etc/apache2/httpd.conf && \  
echo '20 8 * * * apache www-data
/var/www/localhost/ampache/bin/catalog_update.inc' >> /etc/crontab  
RUN sed -i 's/\\(post_max_size\\).*/\1 = 50M/g' /etc/php5/php.ini  
RUN sed -i 's/\\(upload_max_filesize\\).*/\1 = 30M/g' /etc/php5/php.ini  
  
VOLUME ["/etc/mysql/conf.d", "/var/lib/mysql", "/media", "/var/www/config",
"/var/www/themes"]  
  
EXPOSE 80  
EXPOSE 3306  
CMD ["/run.sh"]  

