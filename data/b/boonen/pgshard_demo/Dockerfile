FROM gliderlabs/alpine:3.2  
MAINTAINER Jan Boonen <jan.boonen@geodan.nl>  
  
ENV POSTGIS_VERSION 2.2.0  
ENV GEOS_VERSION 3.5.0  
ENV PROJ4_VERSION 4.9.2  
ENV GDAL_VERSION 2.0.1  
ENV PG_SHARD_VERSION 1.2.3  
  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
# Install PostgreSQL and build Proj.4, GEOS, GDAL, PostGIS and PG_Shard from
sources. Then cleanup  
RUN apk update && \  
apk add curl libxml2 json-c libxml2-dev json-c-dev alpine-sdk autoconf
automake libtool \  
"postgresql@edge<9.5" "postgresql-contrib@edge<9.5" "postgresql-dev@edge<9.5"
&& \  
curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" && \  
chmod +x /usr/local/bin/gosu && \  
mkdir -p /tmp/build && cd /tmp/build && \  
curl -o postgis-${POSTGIS_VERSION}.tar.gz -sSL
http://download.osgeo.org/postgis/source/postgis-${POSTGIS_VERSION}.tar.gz &&
\  
curl -o geos-${GEOS_VERSION}.tar.gz -sSL
https://github.com/libgeos/libgeos/archive/${GEOS_VERSION}.tar.gz && \  
curl -o proj4-${PROJ4_VERSION}.tar.gz -sSL
https://github.com/OSGeo/proj.4/archive/${PROJ4_VERSION}.tar.gz && \  
curl -o gdal-${GDAL_VERSION}.tar.gz -sSL
http://download.osgeo.org/gdal/2.0.1/gdal-${GDAL_VERSION}.tar.gz && \  
curl -o pg_shard-${PG_SHARD_VERSION}.tar.gz -sSL
https://github.com/citusdata/pg_shard/archive/v${PG_SHARD_VERSION}.tar.gz && \  
export PATH=/usr/local/pgsql/bin/:$PATH && \  
tar xzf proj4-${PROJ4_VERSION}.tar.gz && \  
tar xzf geos-${GEOS_VERSION}.tar.gz && \  
tar xzf gdal-${GDAL_VERSION}.tar.gz && \  
tar xzf postgis-${POSTGIS_VERSION}.tar.gz && \  
tar xzf pg_shard-${PG_SHARD_VERSION}.tar.gz && \  
cd proj.4* && ./configure \--enable-silent-rules && make -s && make -s install
&& \  
cd ../libgeos* && ./autogen.sh && ./configure \--enable-silent-rules
CFLAGS="-D__sun -D__GNUC__" CXXFLAGS="-D__GNUC___ -D__sun" && make -s && make
-s install && \  
cd ../gdal* && ./configure \--enable-silent-rules \--with-static-
proj4=/usr/local/lib && make -s && make -s install && \  
cd ../postgis* && ./autogen.sh && ./configure \--enable-silent-rules \--with-
projdir=/usr/local && \  
echo "PERL = /usr/bin/perl" >> extensions/postgis/Makefile && \  
echo "PERL = /usr/bin/perl" >> extensions/postgis_topology/Makefile && make -s
&& make -s install && \  
cd ../pg_shard* && \  
make -s PG_CPPFLAGS="--std=c99 -Wall -Wextra -Wno-error -Wno-unused-parameter
-Iinclude -I/usr/include -Itest/include -I. -I./
-I/usr/include/postgresql/server -I/usr/include/postgresql/internal" && \  
make -s install && \  
apk del curl libxml2-dev json-c-dev alpine-sdk autoconf automake libtool git
postgresql-dev \--force && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/build  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
ENV LANG en_US.utf8  
ENV PGDATA /var/lib/postgresql/data  
  
VOLUME $PGDATA  
  
ADD assets/docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
  
CMD ["postgres"]  

