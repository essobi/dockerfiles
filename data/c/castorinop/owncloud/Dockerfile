FROM castorinop/apache-php  
  
#https://updates.owncloud.com/server/  
ENV VERSION 9.0.0  
#RUN apk add php-ctype php-dom php-gd php-iconv php-json php-xml php-posix
php-zip php-zlib  
#RUN apk add php-mysql php-pdo_mysql  
#missing php-fileinfo  
#RUN apk add php-curl php-bz2 php-intl php-mcrypt php-openssl  
#RUN apk add php-xcache  
RUN urpmi wget netcat-traditional  
RUN urpmi locales-es locales-en  
  
RUN mkdir /app  
RUN cd /app  
  
RUN echo DocumentRoot "/app/owncloud" >> /etc/httpd/conf/httpd.conf  
  
#FIXME: use https://download.owncloud.com/download/community/setup-
owncloud.php  
RUN cd /app && wget
http://download.owncloud.org/community/owncloud-${VERSION}.tar.bz2  
RUN cd /app && wget
http://download.owncloud.org/community/owncloud-${VERSION}.tar.bz2.md5  
  
RUN cd /app && md5sum owncloud-${VERSION}.tar.bz2  
RUN cd /app && tar jxf owncloud-${VERSION}.tar.bz2  
  
# APPS  
RUN mkdir -p /app/owncloud/apps/documents  
RUN curl -L https://github.com/owncloud/documents/archive/v8.2.1.tar.gz | tar
xz --strip-components=1 -C /app/owncloud/apps/documents  
  
RUN mkdir -p /app/owncloud/apps/galleryplus  
RUN curl -L
https://github.com/interfasys/galleryplus/archive/v14.3-stable8.2.tar.gz | tar
xz --strip-components=1 -C /app/owncloud/apps/galleryplus  
#RUN cd /app/owncloud/apps && tar xf v14.3-stable8.2.tar.gz && mv
galleryplus-14.3-stable8.2 galleryplus  
#config database  
#RUN apk add mysql-client  
#RUN mysql -u root -p "CREATE DATABASE owncloud; GRANT ALL ON owncloud.* TO
'owncloud'@'localhost' IDENTIFIED BY 'test123'; GRANT ALL ON owncloud.* #TO
'owncloud'@'db' IDENTIFIED BY 'test123'; FLUSH PRIVILEGES; EXIT"  
#config server  
add apache-owncloud.conf /etc/httpd/conf/webapps.d/owncloud.conf  
#RUN apk add php-fpm  
RUN echo "always_populate_raw_post_data = -1 " >> /etc/php.d/owncloud.ini  
RUN echo "post_max_size = 512M" >> /etc/php.d/owncloud.ini  
RUN echo "upload_max_filesize = 512M" >> /etc/php.d/owncloud.ini  
RUN echo 'default_charset = "UTF-8"' >> /etc/php.d/owncloud.ini  
  
#config owncloud  
#ADD config.php /app/owncloud/config/  
RUN mkdir /app/owncloud/data  
#RUN cd /app/owncloud/data && ln -s ../config/config.php .  
RUN chown -Rv apache:apache /app/owncloud  
#RUN apk add curl php-cli  
#RUN curl --data
"adminlogin=castorblex&adminpass=secret&directory=/app/owncloud/data&dbtype=mysql&dbuser=root&dbpass=&dbname=owncloud&dbhost=db&install=true&hasMySQL=1"
http://localhost  
EXPOSE 80  
VOLUME ["/app/owncloud/data"]  
VOLUME ["/app/owncloud/config"]  
  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
ENTRYPOINT ["/usr/local/bin/run"]  
  
RUN echo "always_populate_raw_post_data = 1" >> /etc/php.d/owncloud.ini  
RUN echo "safe_mode = Off" >> /etc/php.d/owncloud.ini  
  

