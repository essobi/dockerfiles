FROM postgres:9.6-alpine  
MAINTAINER Jeremy Nauta <jeremy@myshowpass.com>  
# Adapted from:  
# https://github.com/appropriate/docker-postgis  
# https://github.com/DanielDent/docker-postgres-replication  
# https://github.com/nebirhos/docker-postgres-replication  
  
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories; \  
echo "http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories; \  
echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories;  
  
# Common settings  
# Fixes error "max_wal_senders must be less than max_connections"  
ENV PG_MAX_CONNECTIONS 500  
ENV PG_WAL_KEEP_SEGMENTS 256  
ENV PG_MAX_WAL_SENDERS 100  
  
# Master/slave settings  
ENV REPLICATION_ROLE master  
ENV REPLICATION_USER replication  
ENV REPLICATION_PASSWORD ""  
  
# Slave settings  
ENV POSTGRES_MASTER_SERVICE_HOST localhost  
ENV POSTGRES_MASTER_SERVICE_DB postgres  
ENV POSTGRES_MASTER_SERVICE_USER postgres  
ENV POSTGRES_MASTER_SERVICE_PASSWORD ""  
ENV POSTGRES_MASTER_SERVICE_PORT 5432  
  
RUN apk add --no-cache gosu  
  
# PostGIS  
ENV POSTGIS_VERSION 2.4.0  
ENV POSTGIS_SHA256
afa91ef89f827de317c7d7fe259e4a2ca4a57837c94a08e9040cbba77ad3e938  
RUN set -ex \  
\  
&& apk add --no-cache --virtual .fetch-deps \  
ca-certificates \  
openssl \  
tar \  
\  
&& wget -O postgis.tar.gz
"https://github.com/postgis/postgis/archive/$POSTGIS_VERSION.tar.gz" \  
&& echo "$POSTGIS_SHA256 *postgis.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src/postgis \  
&& tar \  
\--extract \  
\--file postgis.tar.gz \  
\--directory /usr/src/postgis \  
\--strip-components 1 \  
&& rm postgis.tar.gz \  
\  
&& apk add --no-cache --virtual .build-deps \  
autoconf \  
automake \  
g++ \  
json-c-dev \  
libtool \  
libxml2-dev \  
make \  
perl \  
\  
&& apk add --no-cache --virtual .build-deps-testing \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \  
gdal-dev \  
geos-dev \  
proj4-dev \  
&& cd /usr/src/postgis \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& apk add --no-cache --virtual .postgis-rundeps \  
json-c \  
&& apk add --no-cache --virtual .postgis-rundeps-testing \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \  
geos \  
gdal \  
proj4 \  
&& cd / \  
&& rm -rf /usr/src/postgis \  
&& apk del .fetch-deps .build-deps .build-deps-testing  
  
COPY ./10-replication-config.sh /docker-entrypoint-initdb.d/  
COPY ./20-replication-setup.sh /docker-entrypoint-initdb.d/  
COPY ./30-initdb-postgis.sh /docker-entrypoint-initdb.d/  
COPY ./update-postgis.sh /usr/local/bin  
  
RUN chmod +x /docker-entrypoint-initdb.d/10-replication-config.sh \  
/docker-entrypoint-initdb.d/20-replication-setup.sh \  
/docker-entrypoint-initdb.d/30-initdb-postgis.sh \  
/usr/local/bin/update-postgis.sh  

