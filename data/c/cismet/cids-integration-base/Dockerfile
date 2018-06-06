FROM ubuntu:trusty  
  
MAINTAINER Jean-Michel Ruiz "jean.ruiz@cismet.de"  
LABEL de.cismet.cids.integration.base.name="cids-integration-base PostgeSQL
image" \  
de.cismet.cids.integration.base.version="postgres-9.0.3-2.0" \  
de.cismet.cids.integration.base.tag.docker="postgres-9.0.3-2.0" \  
de.cismet.cids.integration.base.tag.git="postgres-9.0.3-2.0" \  
de.cismet.cids.integration.base.descripton="PostgeSQL 9.0.3 Runtime Image v2"  
  
# ENV  
ENV POSTGRES_PASSWORD postgres  
ENV CIDS_INTEGRATION_BASE_DIR /cidsIntegrationBase  
ENV PG_DATA_DIR ${CIDS_INTEGRATION_BASE_DIR}/pg_data  
# files in the dumps folder are imported upon start from docker-volumes  
# if start parameter import is set  
ENV IMPORT_DIR /import/cidsIntegrationBase  
  
ENV PG_VERSION 9.0.3  
ENV GEOS_VERSION 3.3.5  
ENV PROJ4_VERSION 4.8.0  
ENV LIBXML_VERSION 2.9.4  
ENV POSTGIS_VERSION 1.5.5  
ENV LOCALE de_DE  
ENV ENCODING UTF-8  
ENV PGCLIENTENCODING UTF-8  
ENV PGPORT 5432  
WORKDIR /usr/local/  
  
# install dependencies  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& apt-get update \  
&& apt-get install -y build-essential gcc-4.7 libreadline6-dev libxml2-dev
locales zlib1g-dev curl autoconf xsltproc git libcunit1 libcunit1-doc
libcunit1-dev  
  
# locale  
RUN localedef -i $LOCALE -c -f $ENCODING -A /usr/share/locale/locale.alias
${LOCALE}.${ENCODING} \  
&& locale-gen ${LOCALE}.${ENCODING}  
  
# build & install postgresql  
# ADD
https://ftp.postgresql.org/pub/source/v${PG_VERSION}/postgresql-${PG_VERSION}.tar.bz2
src/  
RUN cd src/ ; curl -fsSL
https://ftp.postgresql.org/pub/source/v${PG_VERSION}/postgresql-${PG_VERSION}.tar.bz2
| tar -xj \  
&& cd postgresql-${PG_VERSION} ; ./configure CC='gcc-4.7 -m64'
\--prefix=/usr/local \--with-pgport=5432 \  
&& make \  
&& make install \  
&& make all \  
&& cd contrib ; make install \  
&& ldconfig \  
&& pwd  
  
# build & install geos  
# ADD http://download.osgeo.org/geos/geos-${GEOS_VERSION}.tar.bz2 src/  
RUN cd src/ ; curl -fsSL
http://download.osgeo.org/geos/geos-${GEOS_VERSION}.tar.bz2 | tar -xj \  
&& cd geos-${GEOS_VERSION} ; ./configure \  
&& make \  
&& make install \  
&& ldconfig \  
&& pwd  
  
# build & install proj4  
# ADD http://download.osgeo.org/proj/proj-${PROJ4_VERSION}.tar.gz src/  
RUN cd src/ ; curl -fsSL
http://download.osgeo.org/proj/proj-${PROJ4_VERSION}.tar.gz | tar -xz \  
&& cd proj-${PROJ4_VERSION} ; ./configure \  
&& make \  
&& make install \  
&& ldconfig \  
&& pwd  
  
# build & install LIBXML  
# ADD http://xmlsoft.org/sources/libxml2-${LIBXML_VERSION}.tar.gz src/  
RUN cd src/ ; curl -fsSL
http://xmlsoft.org/sources/libxml2-${LIBXML_VERSION}.tar.gz | tar -xz \  
&& cd libxml2-${LIBXML_VERSION} ; ./configure \  
&& make \  
&& make install \  
&& ldconfig  
  
# build & install postgis  
# ADD
http://download.osgeo.org/postgis/source/postgis-${POSTGIS_VERSION}.tar.gz
src/  
RUN cd src/ ; curl -fsSL
http://download.osgeo.org/postgis/source/postgis-${POSTGIS_VERSION}.tar.gz |
tar -xz \  
&& cd postgis-${POSTGIS_VERSION} ; ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig  
  
# create postgres user  
RUN groupadd postgres \  
&& useradd -r postgres -g postgres \  
&& echo "postgres:${POSTGRES_PASSWORD}" | chpasswd -e  
  
COPY cidsIntegrationBase ${CIDS_INTEGRATION_BASE_DIR}  
  
# create pg_data directory  
RUN mkdir -p import/cidsIntegrationBase \  
&& mkdir -p ${PG_DATA_DIR} \  
&& echo ${PG_DATA_DIR} \  
&& chown postgres:postgres ${PG_DATA_DIR} \  
&& chmod 700 ${PG_DATA_DIR}  
  
USER postgres  
# initdb  
RUN initdb \  
\--encoding=${ENCODING} \  
\--locale=${LOCALE}.${ENCODING} \  
\--lc-collate=${LOCALE}.${ENCODING} \  
\--lc-monetary=${LOCALE}.${ENCODING} \  
\--lc-numeric=${LOCALE}.${ENCODING} \  
\--lc-time=${LOCALE}.${ENCODING} \  
-D ${PG_DATA_DIR}  
  
USER root  
# conf  
RUN echo "host all all 0.0.0.0/0 md5" >> ${PG_DATA_DIR}/pg_hba.conf \  
&& echo "listen_addresses='*'" >> ${PG_DATA_DIR}/postgresql.conf  
  
USER postgres  
RUN pg_ctl -w -D ${PG_DATA_DIR} start \  
# set password  
&& psql -c "alter role postgres password '${POSTGRES_PASSWORD}'" \  
&& createdb template_postgis \  
# postgis template  
&& psql template_postgis -f src/postgis-${POSTGIS_VERSION}/postgis/postgis.sql
\  
&& psql template_postgis -f src/postgis-${POSTGIS_VERSION}/spatial_ref_sys.sql
\  
&& pg_ctl -w -D ${PG_DATA_DIR} stop  
  
USER root  
# clean up  
RUN apt-get remove --purge --auto-remove -y build-essential gcc-4.7
libreadline6-dev libxml2-dev zlib1g-dev autoconf xsltproc git libcunit1
libcunit1-doc libcunit1-dev \  
&& rm -rf /var/lib/apt/lists/* src/*  
  
# port  
EXPOSE 5432  
# data volume: disabled -> it should be mounted when creating the container!  
# VOLUME ${PG_DATA_DIR}  
# It is important to do it in the right order, because the files inside the
container  
# are only copied to the volume by the first container that uses it (and the
volume is still empty)  
# The VOLUME instruction in a Dockerfile will add one or more new volumes to
any containers created from the image.  
COPY import/container_ctl.sh /  
  
WORKDIR ${CIDS_INTEGRATION_BASE_DIR}  
  
# start  
ENTRYPOINT ["/container_ctl.sh"]  
CMD ["start"]

