FROM alpine:latest  
  
RUN addgroup -S mysql && adduser -Sg mysql mysql  
  
RUN set -x \  
&& apk update \  
&& apk add -u --no-cache \  
bash \  
mariadb \  
mariadb-client \  
pwgen \  
su-exec \  
tzdata \  
&& sed -ri 's/^user\s/#&/' /etc/mysql/my.cnf \  
# purge and re-create /var/lib/mysql with appropriate ownership  
&& rm -rf /var/lib/mysql \  
&& mkdir -p /var/lib/mysql /var/run/mysqld /run/mysqld \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld /run/mysqld \  
&& chmod 777 /var/run/mysqld /run/mysqld  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
# comment out a few problematic configuration values  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf  
  
RUN echo -e "\n!includedir /etc/mysql/conf.d" >> /etc/mysql/my.cnf  
COPY conf.d/* /etc/mysql/conf.d/  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backward compatibility  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

