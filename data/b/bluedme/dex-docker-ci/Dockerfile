# official JDK, based on debian:jessie  
FROM java:openjdk-8-jdk  
  
#
------------------------------------------------------------------------------  
# Commons  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get install -y apt-transport-https software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  
  
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
&& gpg --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# make the "en_US.UTF-8" locale so utf-8 will be enabled by default  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
#
------------------------------------------------------------------------------  
# SBT  
ENV SBT_MAJOR 0.13  
ENV SBT_VERSION 0.13.8  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 \  
&& apt-get update \  
&& apt-get -y install sbt=$SBT_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
#
------------------------------------------------------------------------------  
# Node.js ( without curl shit | sudo bash )  
ENV NPM_DISTRO jessie  
ENV NPM_VERSION node_5.x  
  
RUN add-apt-repository -y -r ppa:chris-lea/node.js \  
&& rm -f /etc/apt/sources.list.d/chris-lea-node_js-*.list \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- \  
&& echo "deb https://deb.nodesource.com/$NPM_VERSION $NPM_DISTRO main" >
/etc/apt/sources.list.d/nodesource.list \  
&& echo "deb-src https://deb.nodesource.com/$NPM_VERSION $NPM_DISTRO main" >>
/etc/apt/sources.list.d/nodesource.list \  
&& apt-get update \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm install -g webpack mocha node-gyp  
  
#
------------------------------------------------------------------------------  
# Elastic Search  
# -- from https://github.com/docker-library/elasticsearch  
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add
-  
  
ENV ELASTICSEARCH_MAJOR 2.3  
ENV ELASTICSEARCH_VERSION 2.3.0  
ENV ELASTICSEARCH_REPO_BASE
http://packages.elasticsearch.org/elasticsearch/2.x/debian  
  
RUN echo "deb $ELASTICSEARCH_REPO_BASE stable main" >
/etc/apt/sources.list.d/elasticsearch.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends
elasticsearch=$ELASTICSEARCH_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
RUN for path in \  
/usr/share/elasticsearch/data \  
/usr/share/elasticsearch/logs \  
/usr/share/elasticsearch/config \  
/usr/share/elasticsearch/config/scripts \  
; do \  
mkdir -p "$path"; \  
chown -R elasticsearch:elasticsearch "$path"; \  
done  
  
COPY elastic-config /usr/share/elasticsearch/config  
COPY elastic-start-service.sh /root/elastic-start-service.sh  
  
EXPOSE 9200 9300  
#
------------------------------------------------------------------------------  
# PostgreSQL 9.4  
# -- https://github.com/docker-
library/postgres/tree/3f8e9784438c8fe54f831c301a45f4d55f6fa453  
ENV PG_MAJOR 9.4  
# explicitly set user/group IDs  
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999
postgres  
  
RUN apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 \  
&& echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main'
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update \  
&& apt-get install -y postgresql-common \  
&& sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-
common/createcluster.conf \  
&& apt-get install -y \  
postgresql-$PG_MAJOR \  
postgresql-contrib-$PG_MAJOR \  
&& rm -rf /var/lib/apt/lists/*  
  
# make the sample config easier to munge (and "correct by default")  
RUN mv -v /usr/share/postgresql/$PG_MAJOR/postgresql.conf.sample
/usr/share/postgresql/ \  
&& ln -sv ../postgresql.conf.sample /usr/share/postgresql/$PG_MAJOR/ \  
&& sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/share/postgresql/postgresql.conf.sample  
  
RUN mkdir -p /var/run/postgresql \  
&& chown -R postgres /var/run/postgresql  
  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
ENV PGDATA /var/lib/postgresql/data  
  
# VOLUME /var/lib/postgresql/data  
COPY pgsql-start-service.sh /root/pgsql-start-service.sh  
  
EXPOSE 5432  
#
------------------------------------------------------------------------------  
# Pre-Fetch Scala version & some dependencies  
COPY build.sbt hello.scala /  
COPY project /project  
RUN sbt compile \  
&& rm -rf build.sbt hello.scala project  
  
#
------------------------------------------------------------------------------  
# we're done  

