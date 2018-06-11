FROM gliderlabs/alpine:3.4  
MAINTAINER Daniel S. Reichenbach <daniel@kogitoapp.com>  
  
# Provide volume directory for initalizing databases  
RUN set -ex \  
&& mkdir /docker-entrypoint-initdb.d  
  
# Install MariaDB  
RUN set -ex \  
&& apk add --update bash tzdata mariadb mariadb-client && rm -rf
/var/cache/apk/* rm -rf /var/lib/mysql && mkdir /var/lib/mysql  
  
RUN set -ex \  
&& mkdir -p /run/mysqld/ && chown -R mysql:mysql /run/mysqld  
  
# Configure default behavior and users  
COPY my.cnf /etc/mysql/my.cnf  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
# Expose default MySQL port  
EXPOSE 3306  
# ... and of course, the daemon itself  
CMD ["mysqld"]  

