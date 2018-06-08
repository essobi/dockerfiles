FROM postgres:9.5  
  
MAINTAINER "Gord Lea <jgordonlea@gmail.com>"  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
postgresql-server-dev-9.5 \  
libxml2-dev \  
libgdal-dev \  
libproj-dev \  
libjson0-dev \  
xsltproc \  
docbook-xsl \  
docbook-mathml \  
libpcre3-dev \  
cmake \  
libcgal-dev \  
openscenegraph \  
libopenscenegraph-dev \  
imagemagick \  
wget  
  
#latest osgeo  
RUN wget http://download.osgeo.org/geos/geos-3.5.0.tar.bz2; \  
tar xfj geos-3.5.0.tar.bz2; \  
cd geos-3.5.0; \  
./configure; \  
make -j; \  
make install; \  
cd ..; \  
rm -rf geos-3.5.0*  
  
#latest sfcgal  
RUN wget https://github.com/Oslandia/SFCGAL/archive/v1.2.0.tar.gz; \  
tar vzxf v1.2.0.tar.gz; \  
cd SFCGAL-1.2.0; \  
cmake .; \  
make -j 2; \  
make install; \  
cd ..; \  
chmod 755 /usr/local/lib/libSFCGAL.*; \  
rm -rf v1.2.0.tar.gz; \  
rm -rf SFCGAL-1.2.0  
  
RUN wget http://download.osgeo.org/postgis/source/postgis-2.2.0.tar.gz; \  
tar xvzf postgis-2.2.0.tar.gz; \  
cd postgis-2.2.0; \  
./configure --with-raster --with-topology --with-sfcgal=/usr/local; \  
make -j; \  
make install; \  
cd ..; \  
rm -rf postgis-2.2.0*  
  
RUN ldconfig  
  
ADD update-pgconf.sh /docker-entrypoint-initdb.d/  

