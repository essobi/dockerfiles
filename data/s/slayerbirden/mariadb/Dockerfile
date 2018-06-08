FROM alpine:3.4  
MAINTAINER Oleg Kulik <okulik@gorillagroup.com>  
  
ENV TERM=xterm \  
TZ=America/Chicago  
  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apk add --no-cache --virtual .gosu-deps \  
dpkg \  
gnupg \  
ca-certificates \  
openssl \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apk del .gosu-deps  
  
RUN apk --update add \  
mariadb \  
mariadb-client \  
tzdata \  
bash \  
&& \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
RUN sed -ri 's/^user\s/#&/' /etc/mysql/my.cnf \  
# purge and re-create /var/lib/mysql with appropriate ownership  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld
/var/log/mysql \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld /var/log/mysql \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld  
  
VOLUME /var/lib/mysql  
  
COPY cnf/my.cnf /etc/mysql/my.cnf  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

