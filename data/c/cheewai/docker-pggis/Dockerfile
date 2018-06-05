# PostgreSQL GIS stack  
#  
# This image includes the following tools  
# - PostgreSQL 9.5  
# - PostGIS 2.2 with raster, topology and sfcgal support, PL/R  
# - OGR Foreign Data Wrapper  
# - PgRouting  
# - PDAL master  
# - PostgreSQL PointCloud version master  
#  
# Version 1.7  
  
FROM phusion/baseimage  
MAINTAINER Vincent Picavet, vincent.picavet@oslandia.com  
  
ARG PG_VER=9.5  
ARG POSTGIS_VER=2.2.0  
ARG GEOS_VER=3.5.0  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
#RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
  
# Use APT postgresql repositories  
# packages needed for compilation  
# application packages  
WORKDIR /tmp  
RUN apt-get update && apt-get install -y curl wget ca-certificates \  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main
${PG_VER}" > /etc/apt/sources.list.d/pgdg.list && wget --quiet -O -
https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \  
&& apt-get update \  
&& apt-get install -y autoconf build-essential cmake docbook-mathml docbook-
xsl libboost-dev libboost-thread-dev libboost-filesystem-dev libboost-system-
dev libboost-iostreams-dev libboost-program-options-dev libboost-timer-dev
libcunit1-dev libgdal-dev libgeos++-dev libgeotiff-dev libgmp-dev libjson0-dev
libjson-c-dev liblas-dev libmpfr-dev libopenscenegraph-dev libpq-dev libproj-
dev libxml2-dev postgresql-server-dev-${PG_VER} xsltproc git build-essential
wget libcgal-dev postgresql-common postgresql-contrib-${PG_VER}
postgresql-${PG_VER}-plr \  
&& echo download and compile CGAL, SFCGAL \  
&& git clone https://github.com/Oslandia/SFCGAL.git \  
&& cd SFCGAL && cmake . && make -j3 && make install \  
&& cd /tmp && rm -Rf SFCGAL \  
&& echo Download and install GEOS ${GEOS_VER} \  
&& wget http://download.osgeo.org/geos/geos-${GEOS_VER}.tar.bz2 &&\  
tar -xjf geos-${GEOS_VER}.tar.bz2 &&\  
cd geos-${GEOS_VER} &&\  
./configure && make && make install &&\  
cd .. && rm -Rf geos-${GEOS_VER} geos-${GEOS_VER}.tar.bz2 \  
&& echo Download and compile PostGIS ${POSTGIS_VER} \  
&& wget http://download.osgeo.org/postgis/source/postgis-${POSTGIS_VER}.tar.gz
\  
&& tar -xvzf postgis-${POSTGIS_VER}.tar.gz \  
&& cd postgis-${POSTGIS_VER} && ./configure --with-
sfcgal=/usr/local/bin/sfcgal-config --with-geosconfig=/usr/local/bin/geos-
config \  
&& make && make install \  
&& cd /tmp && rm -Rf postgis-${POSTGIS_VER}.tar.gz postgis-${POSTGIS_VER} \  
&& echo Download and compile pgrouting \  
&& git clone https://github.com/pgRouting/pgrouting.git &&\  
cd pgrouting &&\  
mkdir build && cd build &&\  
cmake -DWITH_DOC=OFF -DWITH_DD=ON .. &&\  
make -j3 && make install \  
&& cd /tmp && rm -Rf pgrouting \  
&& echo Download and compile ogr_fdw \  
&& git clone https://github.com/pramsey/pgsql-ogr-fdw.git &&\  
cd pgsql-ogr-fdw &&\  
make && make install && \  
cd .. && rm -Rf pgsql-ogr-fdw \  
&& echo Compile PDAL \  
&& git clone https://github.com/PDAL/PDAL.git pdal \  
&& mkdir PDAL-build && \  
cd PDAL-build && \  
cmake ../pdal && \  
make -j3 && \  
make install \  
&& rm -Rf pdal && rm -Rf PDAL-build \  
&& echo Compile PointCloud \  
&& git clone https://github.com/pramsey/pointcloud.git \  
&& cd pointcloud && ./autogen.sh && ./configure && make -j3 && make install \  
&& cd /tmp && rm -Rf pointcloud \  
&& echo get compiled libraries recognized \  
&& ldconfig \  
&& echo clean packages \  
&& apt-get remove -y --purge autotools-dev libgeos-dev libgif-dev libgl1-mesa-
dev libglu1-mesa-dev libgnutls-dev libgpg-error-dev libhdf4-alt-dev
libhdf5-dev libicu-dev libidn11-dev libjasper-dev libjbig-dev libjpeg8-dev
libjpeg-dev libjpeg-turbo8-dev libkrb5-dev libldap2-dev libltdl-dev liblzma-
dev libmysqlclient-dev libnetcdf-dev libopenthreads-dev libp11-kit-dev
libpng12-dev libpthread-stubs0-dev librtmp-dev libspatialite-dev
libsqlite3-dev libssl-dev libstdc++-4.8-dev libtasn1-6-dev libtiff5-dev
libwebp-dev libx11-dev libx11-xcb-dev libxau-dev libxcb1-dev libxcb-dri2-0-dev
libxcb-dri3-dev libxcb-glx0-dev libxcb-present-dev libxcb-randr0-dev libxcb-
render0-dev libxcb-shape0-dev libxcb-sync-dev libxcb-xfixes0-dev libxdamage-
dev libxdmcp-dev libxerces-c-dev libxext-dev libxfixes-dev libxshmfence-dev
libxxf86vm-dev linux-libc-dev manpages-dev mesa-common-dev libgcrypt11-dev
unixodbc-dev uuid-dev x11proto-core-dev x11proto-damage-dev x11proto-dri2-dev
x11proto-fixes-dev x11proto-gl-dev x11proto-input-dev x11proto-kb-dev
x11proto-xext-dev x11proto-xf86vidmode-dev xtrans-dev zlib1g-dev \  
&& apt-get remove -y --purge autoconf build-essential cmake docbook-mathml
docbook-xsl libboost-dev libboost-filesystem-dev libboost-timer-dev libcgal-
dev libcunit1-dev libgdal-dev libgeos++-dev libgeotiff-dev libgmp-dev
libjson0-dev libjson-c-dev liblas-dev libmpfr-dev libopenscenegraph-dev libpq-
dev libproj-dev libxml2-dev xsltproc git build-essential wget \  
&& apt-get remove -y --purge automake m4 make \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# ---------- SETUP --------------  
  
# add a baseimage PostgreSQL init script  
RUN mkdir /etc/service/postgresql  
ADD postgresql.sh /etc/service/postgresql/run  
  
# # Adjust PostgreSQL configuration so that remote connections to the  
# # database are possible.  
# RUN echo "host all all 0.0.0.0/0 md5" >>
/etc/postgresql/${PG_VER}/main/pg_hba.conf  
  
# # And add ``listen_addresses`` to
``/etc/postgresql/${PG_VER}/main/postgresql.conf``  
# RUN echo "listen_addresses='*'" >>
/etc/postgresql/${PG_VER}/main/postgresql.conf  
#  
# # Expose PostgreSQL  
# EXPOSE 5432  
  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/data", "/etc/postgresql", "/var/log/postgresql",
"/var/lib/postgresql"]  
  
# add database setup upon image start  
ADD pgpass /root/.pgpass  
RUN chmod 700 /root/.pgpass  
RUN mkdir -p /etc/my_init.d  
ADD init_db_script.sh /etc/my_init.d/init_db_script.sh  
ADD init_db.sh /root/init_db.sh  

