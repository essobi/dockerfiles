FROM postgres:9.5  
MAINTAINER F4<contact@f4-group.com>  
  
#postgis required packages, PG_MAJOR from parent container  
#lib building packages  
#for address_standardizer  
RUN apt-get -y update && apt-get -y install \  
build-essential wget postgresql-server-dev-$PG_MAJOR libxml2-dev libjson0-dev
\  
cmake libboost-dev libgmp-dev libmpfr-dev libboost-thread-dev libboost-system-
dev \  
libpcre3-dev  
  
ADD build-and-install-postgis.sh /build-and-install-postgis.sh  
  
RUN POSTGIS_VERSION=2.2.2 \  
GEOS_VERSION=3.5.0 \  
GDAL_VERSION=2.1.1 \  
PROJ_VERSION=4.9.2 \  
CGAL_VERSION=4.6.3 \  
SFCGAL_VERSION=1.3.0 \  
/build-and-install-postgis.sh  
  
RUN POSTGIS_VERSION=2.4.0 \  
GEOS_VERSION=3.6.2 \  
GDAL_VERSION=2.2.2 \  
PROJ_VERSION=4.9.3 \  
CGAL_VERSION=4.10.1 \  
SFCGAL_VERSION=1.3.2 \  
/build-and-install-postgis.sh  
  
RUN rm /build-and-install-postgis.sh  
  
ADD postgis-template.sh /docker-entrypoint-initdb.d/postgis-template.sh  

