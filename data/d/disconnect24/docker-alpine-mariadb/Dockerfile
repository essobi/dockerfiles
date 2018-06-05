FROM alpine:edge  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN addgroup -S mysql && adduser -S -g mysql mysql  
  
RUN apk add -U --no-cache gnupg  
  
# add gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apk add -U --no-cache wget ca-certificates \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-
amd64.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apk del ca-certificates wget  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN apk add -U --no-cache \  
# for MYSQL_RANDOM_ROOT_PASSWORD  
pwgen \  
# for mysql_ssl_rsa_setup  
openssl \  
# FATAL ERROR: please install the following Perl modules before executing
/usr/local/mysql/scripts/mysql_install_db:  
# File::Basename  
# File::Copy  
# Sys::Hostname  
# Data::Dumper  
perl \  
# For entrypoint  
bash \  
# for mysql_tzinfo_to_sql  
tzdata  
  
RUN apk add -U --no-cache mariadb mariadb-client \  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld \  
# don't reverse lookup hostnames, they are usually another container  
&& echo '[mysqld]\nskip-host-cache\nskip-name-resolve' > /etc/mysql/my.cnf  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s /usr/local/bin/docker-entrypoint.sh /entrypoint.sh \  
# ^ backwards compat  
&& chmod a+x /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

