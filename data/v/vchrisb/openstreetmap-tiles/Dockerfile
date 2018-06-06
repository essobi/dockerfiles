## -*- docker-image-name: "homme/openstreetmap-tiles:latest" -*-  
##  
# The OpenStreetMap Tile Server  
#  
# This creates an image with containing the OpenStreetMap tile server stack as  
# described at  
# <http://switch2osm.org/serving-tiles/manually-building-a-tile-
server-12-04/>.  
#  
FROM phusion/baseimage  
  
# Set the locale. This affects the encoding of the Postgresql template  
# databases.  
ENV LANG C.UTF-8  
RUN update-locale LANG=C.UTF-8  
  
# Ensure `add-apt-repository` is present  
RUN apt-get update -y  
RUN apt-get install -y software-properties-common python-software-properties  
  
RUN apt-get install -y libboost-all-dev git-core tar unzip wget bzip2 build-
essential autoconf \  
libtool libxml2-dev libgeos-dev libgeos++-dev libpq-dev libbz2-dev libproj-dev
munin-node munin libprotobuf-c0-dev \  
protobuf-c-compiler libfreetype6-dev libpng12-dev libtiff5-dev libicu-dev
libgdal-dev libcairo-dev libcairomm-1.0-dev \  
apache2 apache2-dev libagg-dev liblua5.2-dev ttf-unifont lua5.1 liblua5.1-dev
libgeotiff-epsg jq  
  
# Install the osm2pgsql  
RUN apt-get install -y make cmake g++ libboost-dev libboost-system-dev
libboost-filesystem-dev libexpat1-dev zlib1g-dev libbz2-dev libpq-dev libgeos-
dev libgeos++-dev libproj-dev lua5.2 liblua5.2-dev  
RUN cd /tmp && git clone git://github.com/openstreetmap/osm2pgsql.git  
RUN cd /tmp/osm2pgsql && \  
mkdir build && cd build && \  
cmake .. && make && \  
make install  
  
# Install the Mapnik library  
RUN apt-get -y install autoconf apache2-dev libtool libxml2-dev libbz2-dev
libgeos-dev libgeos++-dev libproj-dev gdal-bin libgdal1-dev libmapnik-dev
mapnik-utils python-mapnik  
  
# Verify that Mapnik has been installed correctly  
RUN python -c 'import mapnik'  
  
# Install mod_tile and renderd  
RUN cd /tmp && git clone https://github.com/openstreetmap/mod_tile.git  
RUN cd /tmp/mod_tile && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
make install-mod_tile && \  
ldconfig  
  
# Install the Carto and Mapnik stylesheet  
RUN cd /tmp && git clone https://github.com/gravitystorm/openstreetmap-
carto.git  
RUN cd /tmp/openstreetmap-carto && apt-get install -y npm nodejs-legacy && \  
npm install -g carto && \  
carto -v  
RUN cd /tmp/openstreetmap-carto && scripts/get-shapefiles.py  
  
# Install Fonts  
RUN apt-get install -y fonts-noto-cjk fonts-noto-hinted fonts-noto-unhinted
fonts-hanazono ttf-unifont  
  
# Create the files required for the mod_tile system to run  
RUN mkdir /var/run/renderd && chown www-data: /var/run/renderd  
RUN mkdir /var/lib/mod_tile && chown www-data /var/lib/mod_tile  
  
# Configure mod_tile  
RUN echo "LoadModule tile_module /usr/lib/apache2/modules/mod_tile.so" >
/etc/apache2/mods-available/mod_tile.load  
RUN a2enmod mod_tile  
  
# Configure renderd  
RUN sed -i "s|plugins_dir=.*|plugins_dir=$(mapnik-config --input-plugins)|"
/usr/local/etc/renderd.conf  
RUN sed -i "s|XML=.*|XML=/tmp/openstreetmap-carto/mapnik.xml|"
/usr/local/etc/renderd.conf  
  
# Configure Apache2  
ADD mod_tile.conf /etc/apache2/conf-available  
RUN a2enconf mod_tile  
  
# Add PostgreSQL client  
RUN apt-get install -y postgresql-client  
  
# Create an `apache2` `runit` service  
ADD apache2 /etc/sv/apache2  
RUN update-service --add /etc/sv/apache2  
  
# Create a `renderd` `runit` service  
ADD renderd /etc/sv/renderd  
RUN update-service --add /etc/sv/renderd  
  
# Clean up APT when done  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Expose the webserver and database ports  
EXPOSE 80  
# We need the volume for importing data from  
# VOLUME ["/data"]  
# Set the osm2pgsql import cache size in MB. Used in `run import`.  
ENV OSM_IMPORT_CACHE 800  
# Add the entrypoint  
ADD run.sh /usr/local/sbin/run  
ENTRYPOINT ["/sbin/my_init", "--", "/usr/local/sbin/run"]  
  
# Default to showing the usage text  
CMD ["startservices"]  

