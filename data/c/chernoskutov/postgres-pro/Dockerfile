# vim:set ft=dockerfile:  
FROM debian:stretch  
  
# make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by default  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
  
# Env section  
ENV PG_REPO_KEY GPG-KEY-POSTGRESPRO  
ENV GPG_KEY B42F6819007F00F88E364FD4036A9C25BF357DD4  
ENV PG_MAJOR 9.5  
ENV PG_MINOR 12.1  
ENV PG_RELEASE $PG_MAJOR.$PG_MINOR  
ENV PG_VERSION $PG_RELEASE-1.stretch.pro  
ENV GOSU_VERSION 1.10  
ENV LANG en_US.utf8  
  
# explicitly set user/group IDs  
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999
postgres  
  
# grab gosu for easy step-down from root  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates wget gnupg
dirmngr lsb-release \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& (gpg --keyserver ha.pool.sks-keyservers.net --recv-keys $GPG_KEY \  
|| gpg --keyserver pgp.mit.edu --recv-keys $GPG_KEY \  
|| gpg --keyserver keyserver.pgp.com --recv-keys $GPG_KEY) \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& wget --quiet -O -
http://repo.postgrespro.ru/pgpro-$PG_MAJOR/keys/$PG_REPO_KEY | apt-key add - \  
&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget gnupg dirmngr  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN mkdir /docker-entrypoint-init.d  
  
# Install pgpro  
RUN echo "deb http://repo.postgrespro.ru/pgpro-
archive/pgpro-$PG_RELEASE/debian $(lsb_release -cs) main" >
/etc/apt/sources.list.d/postgrespro.list \  
&& apt-get update \  
&& apt-get install -y postgrespro-common \  
&& sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-
common/createcluster.conf \  
&& apt-get install -y \  
postgrespro-$PG_MAJOR=$PG_VERSION \  
postgrespro-contrib-$PG_MAJOR=$PG_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
# make the sample config easier to munge (and "correct by default")  
RUN mv -v /usr/share/postgresql/$PG_MAJOR/postgresql.conf.sample
/usr/share/postgresql/ \  
&& ln -sv ../postgresql.conf.sample /usr/share/postgresql/$PG_MAJOR/ \  
&& sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/share/postgresql/postgresql.conf.sample  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql  
  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
ENV PGDATA /var/lib/postgresql/data  
VOLUME /var/lib/postgresql/data  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]

