FROM debian:stretch  
  
RUN set -ex; \  
if ! command -v gpg > /dev/null; then \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
gnupg \  
dirmngr \  
; \  
rm -rf /var/lib/apt/lists/*; \  
fi  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PG_MAJOR 10  
ENV PG_VERSION PostgresPro 10.1.1  
ENV LANG ru_RU.utf8  
ENV LC_ALL ru_RU.UTF-8  
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999
postgres  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
\  
fetchDeps=' \  
ca-certificates \  
wget \  
lsb-release \  
'; \  
apt-get update; \  
apt-get install -y --no-install-recommends $fetchDeps; \  
rm -rf /var/lib/apt/lists/*; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true  
  
# make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by default  
# ENV LANG en_US.utf8  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN sh -c 'echo "deb http://repo.postgrespro.ru/pgpro-10/debian $(lsb_release
-cs) main" > /etc/apt/sources.list.d/postgrespro.list' && \  
wget --quiet -O - http://repo.postgrespro.ru/pgpro-10/keys/GPG-KEY-POSTGRESPRO
| apt-key add - && \  
apt-get update && \  
apt-get install -y postgrespro-std-10-server postgrespro-std-10-client
postgrespro-std-10-libs  
  
RUN apt-get purge -y --auto-remove $fetchDeps  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres:postgres
/var/run/postgresql && chmod 2777 /var/run/postgresql  
  
ENV PATH /opt/pgpro/std-10/bin:$PATH  
ENV PGDATA /var/lib/pgpro/std-10/data  
# this 777 will be replaced by 700 at runtime (allows semi-arbitrary "--user"
values)  
RUN mkdir -p "$PGDATA" && chown -R postgres:postgres "$PGDATA" && chmod 777
"$PGDATA"  
VOLUME /var/lib/pgpro/std-10/data  
  
RUN localedef -i ru_RU -f UTF-8 ru_RU.UTF-8  
  
RUN pg-wrapper links update  
  
#copy dict  
# COPY ru-dict/* /usr/share/postgresql/9.6/tsearch_data/  
# COPY en-dict/* /usr/share/postgresql/9.6/tsearch_data/  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh  
# backwards compat  
RUN ln -s usr/local/bin/docker-entrypoint.sh /  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

