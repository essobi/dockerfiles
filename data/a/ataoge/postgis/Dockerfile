# vim:set ft=dockerfile:  
FROM debian:jessie  
MAINTAINER Huang Tao <loveht@aliyun.com>  
  
# explicitly set user/group IDs  
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999
postgres  
  
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
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
ENV PG_MAJOR 9.5  
ENV PG_VERSION 9.5.3-1.pgdg80+1  
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
  
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql  
  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
ENV PGDATA /var/lib/postgresql/data  
VOLUME /var/lib/postgresql/data  
  
#full seach  
RUN apt-get update && apt-get install -y unzip wget gcc make postgresql-
server-dev-$PG_MAJOR \  
&& wget http://www.xunsearch.com/scws/down/scws-1.2.3.tar.bz2 \  
&& tar xvjf scws-1.2.3.tar.bz2 \  
&& wget https://github.com/amutu/zhparser/archive/master.zip -O zhparser.zip \  
&& unzip zhparser.zip  
  
RUN cd scws-1.2.3 && ./configure --prefix=/usr/local/lib/scws-1.2.3 && make &&
make install  
RUN cd zhparser-master && SCWS_HOME=/usr/local/lib/scws-1.2.3 make && make
install  
  
RUN apt-get remove -y unzip wget gcc make postgresql-server-dev-$PG_MAJOR  
  
#postgis  
ENV POSTGIS_MAJOR 2.2  
ENV POSTGIS_VERSION 2.2.2+dfsg-1.pgdg80+1  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR=$POSTGIS_VERSION \  
postgis=$POSTGIS_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

