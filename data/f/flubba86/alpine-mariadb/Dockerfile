# vim:set ft=dockerfile:  
FROM alpine:3.5  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN addgroup -S mysql && adduser -S -G mysql mysql  
  
RUN apk --no-cache add ca-certificates && update-ca-certificates && apk --no-
cache add tini openssl gnupg su-exec bash pwgen socat tzdata  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
ENV MARIADB_MAJOR 10.1  
ENV MARIADB_VERSION 10.1.21-r0  
  
RUN apk --no-cache add mariadb-common=${MARIADB_VERSION}
mariadb=${MARIADB_VERSION} mariadb-client=${MARIADB_VERSION}  
RUN echo -e 'http://dl-cdn.alpinelinux.org/alpine/v3.4/main' >>
/etc/apk/repositories  
RUN apk --no-cache add xtrabackup  
# delete the 3.4 repository  
RUN sed -i '$ d' /etc/apk/repositories  
  
# comment out any "user" entires in the MySQL config ("docker-entrypoint.sh"
or "--user" will handle user switching)  
RUN sed -ri 's/^user\s/#&/' /etc/mysql/my.cnf \  
#RUN sed -ri 's/^user\s/#&/' /etc/mysql/my.cnf /etc/mysql/conf.d/* \  
# purge and re-create /var/lib/mysql with appropriate ownership  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld && ln -s
/var/run/mysqld /run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld /run/mysqld \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld /run/mysqld  
  
# comment out a few problematic configuration values  
# don't reverse lookup hostnames, they are usually another container  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \  
&& echo -e 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 ==
"[mysqld]" && c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf
\  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh && ln -s
/usr/local/bin/docker-entrypoint.sh / # backwards compat  
ENTRYPOINT ["/sbin/tini","-v","--","/usr/local/bin/docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

