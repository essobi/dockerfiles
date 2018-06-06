#  
# Derived from  
# https://github.com/docker-library/mongo/tree/master/3.4  
# https://github.com/docker-library/postgres/tree/master/9.6  
#  
FROM debian:jessie  
  
################## Accounts ##############  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999
postgres  
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb  
  
################## Tools ##############  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
jq \  
numactl \  
&& rm -rf /var/lib/apt/lists/*  
  
# grab supervisor  
RUN set -x \  
&& apt-get update && apt-get install -y openssh-server apache2 supervisor \  
&& mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
# make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by default  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
RUN mkdir /docker-postgres-entrypoint-initdb.d  
RUN mkdir /docker-mongo-entrypoint-initdb.d  
  
################## GPG Keys ##############  
RUN set -ex; \  
# pub 4096R/ACCC4CF8 2011-10-13 [expires: 2019-07-02]  
# Key fingerprint = B97B 0AFC AA1A 47F0 44F2 44A0 7FCC 7D46 ACCC 4CF8  
# uid PostgreSQL Debian Repository  
key='B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8'; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
gpg --export "$key" > /etc/apt/trusted.gpg.d/postgres.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list  
  
ENV GPG_KEYS \  
# pub 4096R/A15703C6 2016-01-11 [expires: 2018-01-10]  
# Key fingerprint = 0C49 F373 0359 A145 1858 5931 BC71 1F9B A157 03C6  
# uid MongoDB 3.4 Release Signing Key <packaging@mongodb.com>  
0C49F3730359A14518585931BC711F9BA15703C6  
# https://docs.mongodb.com/manual/tutorial/verify-mongodb-packages/#download-
then-import-the-key-file  
RUN set -ex; \  
export GNUPGHOME="$(mktemp -d)"; \  
for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done; \  
gpg --export $GPG_KEYS > /etc/apt/trusted.gpg.d/mongodb.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list  
  
################## Postgres ##############  
ENV PG_MAJOR 9.6  
ENV PG_VERSION 9.6.4-1.pgdg80+1  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main'
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update \  
&& apt-get install -y postgresql-common \  
&& sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-
common/createcluster.conf \  
&& apt-get install -y \  
postgresql-$PG_MAJOR=$PG_VERSION \  
postgresql-contrib-$PG_MAJOR=$PG_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
# make the sample config easier to munge (and "correct by default")  
RUN mv -v /usr/share/postgresql/$PG_MAJOR/postgresql.conf.sample
/usr/share/postgresql/ \  
&& ln -sv ../postgresql.conf.sample /usr/share/postgresql/$PG_MAJOR/ \  
&& sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/share/postgresql/postgresql.conf.sample  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres:postgres
/var/run/postgresql && chmod g+s /var/run/postgresql  
  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
ENV PGDATA /var/lib/postgresql/data  
RUN mkdir -p "$PGDATA" && chown -R postgres:postgres "$PGDATA" && chmod 777
"$PGDATA" # this 777 will be replaced by 700 at runtime (allows semi-arbitrary
"--user" values)  
VOLUME /var/lib/postgresql/data  
EXPOSE 5432  
################## Mongo ##############  
ENV MONGO_MAJOR 3.4  
ENV MONGO_VERSION 3.4.4  
ENV MONGO_PACKAGE mongodb-org  
  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-
org/$MONGO_MAJOR main" > /etc/apt/sources.list.d/mongodb-org.list  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
${MONGO_PACKAGE}=$MONGO_VERSION \  
${MONGO_PACKAGE}-server=$MONGO_VERSION \  
${MONGO_PACKAGE}-shell=$MONGO_VERSION \  
${MONGO_PACKAGE}-mongos=$MONGO_VERSION \  
${MONGO_PACKAGE}-tools=$MONGO_VERSION \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/mongodb \  
&& mv /etc/mongod.conf /etc/mongod.conf.orig  
  
RUN mkdir -p /data/db /data/configdb \  
&& chown -R mongodb:mongodb /data/db /data/configdb  
VOLUME /data/db /data/configdb  
EXPOSE 27017  
################## Entrypoint (adapted) ##############  
COPY mongo-initdb.d /docker-mongo-entrypoint-initdb.d  
COPY postgres-initdb.d /docker-postgres-entrypoint-initdb.d  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY docker-mongo-entrypoint.sh /usr/local/bin/  
COPY docker-postgres-entrypoint.sh /usr/local/bin/  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/bin/supervisord"]  
#CMD ["/bin/sleep", "100"]  

