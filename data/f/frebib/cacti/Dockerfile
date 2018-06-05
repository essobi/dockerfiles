FROM alpine:3.5  
MAINTAINER Joe Groocock <frebib@gmail.com>  
  
ENV MYSQL_DATABASE=cacti \  
MYSQL_HOST=mysql \  
MYSQL_PORT=3306 \  
MYSQL_USER=cacti \  
MYSQL_PASSWORD=cacti \  
CACTI_HOME=/usr/share/cacti \  
URL_PATH=/cacti  
  
ARG BUILD_DEPS="curl tar"  
  
RUN apk --no-cache add $BUILD_DEPS php5 php5-fpm php5-snmp php5-mysql net-
snmp-tools mariadb-client && \  
curl -L http://www.cacti.net/downloads/cacti-latest.tar.gz | tar xz -C /tmp &&
\  
mv /tmp/cacti* $CACTI_HOME && \  
sed -i 's/memory_limit = 128M/memory_limit = 512M/g' /etc/php5/php.ini && \  
sed -i '\|include = \/etc\/php5\/fpm.d\/*\.conf|d; \  
s|\(error_log = \).*|\1/dev/stderr|; \  
s|\;\(access.log = \).*|\1/dev/stdout|; \  
s|\;\(chroot = \).*|\1/usr/share/cacti|; \  
s|\;\(pid = \).*|\1/tmp/php-fpm.pid|' /etc/php5/php-fpm.conf && \  
sed -i 's|\($database_default =\).*|\1 getenv("MYSQL_DATABASE");|; \  
s|\($database_hostname =\).*|\1 getenv("MYSQL_HOST");|; \  
s|\($database_username =\).*|\1 getenv("MYSQL_USER");|; \  
s|\($database_password =\).*|\1 getenv("MYSQL_PASSWORD");|; \  
s|\($database_port =\).*|\1 getenv("MYSQL_PORT");|; \  
s|\($url_path =\).*|\1 getenv("URL_PATH");|' $CACTI_HOME/include/config.php &&
\  
apk --no-cache del $BUILD_DEPS  
  
EXPOSE 9000/tcp  
  
ADD init.sh .  
ENTRYPOINT [ "./init.sh" ]  
CMD [ "php-fpm", "-F", "-g", "/tmp/php-fpm.pid" ]  

