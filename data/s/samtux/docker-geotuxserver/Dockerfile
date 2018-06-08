FROM ubuntu:16.04  
MAINTAINER Samuel Fernando Mesa Giraldo <samuelmesa@gmail.com>  
# Base: Yves Jacolin <yjacolin@free.fr>  
ENV VERSION 2017-09-06  
ENV TERM xterm  
ENV APACHE_CONFDIR /etc/apache2  
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_PID_FILE $APACHE_RUN_DIR/apache2.pid  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV LANG C  
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid  
ENV PGSERVICEFILE /gisdata/projects/pg_service.conf  
ENV MAPCACHE_VERSION=rel-1-6-0  
ENV PYCSW_VERSION=2.0.3  
ENV LIZMAPVERSION 3.1.3  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key CAEB3DC3BDF7FB45
&& \  
echo "deb http://qgis.org/debian xenial main" >
/etc/apt/sources.list.d/qgis.list  
  
RUN apt-get update  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -qqy git cmake \  
software-properties-common g++ make build-essential \  
libaprutil1-dev libapr1-dev libpng12-dev libjpeg-dev \  
libcurl4-gnutls-dev libpcre3-dev libpixman-1-dev libgdal-dev \  
libgeos-dev libsqlite3-dev libdb5.3-dev libtiff-dev \  
apache2 apache2-dev libfcgi-dev libdb5.3 db-util \  
qgis-server libapache2-mod-fcgid libfcgi-dev \  
cgi-mapserver libmapserver-dev mapserver-bin python-mapscript  
  
# Install Mapcache itself  
RUN git clone https://github.com/mapserver/mapcache.git
/usr/local/src/mapcache && \  
cd /usr/local/src/mapcache && git checkout ${MAPCACHE_VERSION}  
  
# Compile Mapcache for Apache  
RUN mkdir /usr/local/src/mapcache/build && \  
cd /usr/local/src/mapcache/build && \  
cmake ../ -DCMAKE_INSTALL_PREFIX=/usr \  
-DCMAKE_VERBOSE_MAKEFILE=1 \  
-DWITH_PIXMAN=1 \  
-DWITH_SQLITE=1 \  
-DWITH_BERKELEY_DB=1 \  
-DWITH_TIFF=1 \  
-DWITH_TIFF_WRITE_SUPPORT=0 \  
-DWITH_GEOTIFF=0 \  
-DWITH_MAPSERVER=0 \  
-DWITH_PCRE=1 \  
-DWITH_APACHE=1 \  
-DWITH_VERSION_STRING=1 \  
-DWITH_CGI=1 \  
-DWITH_FCGI=1 \  
-DWITH_GEOS=1 \  
-DWITH_OGR=1 \  
-DWITH_MEMCACHE=1 \  
-DCMAKE_PREFIX_PATH="/etc/apache2" && \  
make && \  
make install  
  
# Force buit libraries dependencies  
RUN ldconfig  
RUN cp /usr/bin/mapserv /usr/lib/cgi-bin/  
  
# Create directories  
RUN mkdir /mapcache  
RUN mkdir /gisdata  
RUN mkdir /gisdata/projects  
RUN mkdir /gisdata/tiles  
RUN mkdir /gisdata/metadata  
ADD mapcache.xml /srv/mapcache.xml  
ADD mapcache.xml /mapcache/mapcache.xml  
  
# Install tileserver-php y Lizmap  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php7.0 libapache2-mod-
php7.0 \  
xauth curl libapache2-mod-fcgid php7.0-cgi php7.0-gd php7.0-sqlite \  
php7.0-curl php7.0-xmlrpc python-simplejson php7.0-xml unzip  
  
RUN a2enmod actions; a2enmod fcgid ; a2enmod ssl; a2enmod rewrite; a2enmod
headers; \  
a2enmod deflate; a2enmod php7.0  
  
COPY scripts/setup_lizmap.sh /usr/local/bin/setup_lizmap.sh  
RUN cd /var/www && git clone https://github.com/klokantech/tileserver-php.git  
ADD https://github.com/3liz/lizmap-web-client/archive/$LIZMAPVERSION.zip
/var/www/  
RUN /usr/local/bin/setup_lizmap.sh  
  
RUN cd /srv && git clone https://github.com/klokantech/tileserver-php.git  
  
# Install TerriaMap  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs gdal-bin  
  
RUN cd /srv && git clone https://github.com/TerriaJS/TerriaMap.git && \  
cd /srv/TerriaMap && npm install && npm install -g gulp && npm run gulp  
  
# Install PyCSW  
# prepare log and data directory  
RUN mkdir -p /var/log/pycsw  
RUN chmod -R 777 /var/log/pycsw  
RUN mkdir -p /var/data/pycsw  
  
RUN apt-get install -y python-pip libxslt-dev libxml2-dev python-libxml2 && \  
cd /srv && git clone https://github.com/geopython/pycsw.git && \  
cd /srv/pycsw && git checkout ${PYCSW_VERSION} && \  
pip install -e . && pip install -r requirements-standalone.txt  
  
RUN apt-get install -y libapache2-mod-wsgi && a2enmod wsgi  
  
COPY default.cfg /srv/pycsw/default.cfg  
RUN echo "PATH=$PATH:/srv/pycsw/bin/bin" > /etc/environment  
RUN cd /srv/pycsw && ./bin/pycsw-admin.py -c setup_db -f default.cfg  
  
# Install QGIS Web Client 1  
RUN cd /srv && git clone https://github.com/qgis/qgis-web-client.git && \  
cp -rf /srv/qgis-web-client/projects /gisdata/projects/demo && \  
cp -rf /srv/qgis-web-client/data /gisdata/projects/data  
  
# Install QGIS Web Client 2  
RUN npm install -g yarn  
RUN apt-get install -y python-flask && pip install Flask-Cors && \  
cd /srv && git clone https://github.com/sourcepole/qwc2-server.git  
  
COPY app.wsgi /srv/qwc2-server/app.wsgi  
  
RUN cd /srv && git clone \--recursive https://github.com/qgis/qwc2-demo-
app.git && \  
cd /srv/qwc2-demo-app && yarn install && yarn prod && \  
cp -rfv assets /var/www/ && cp -rfv translations /var/www/ && cp -rfv prod
/var/www/qwc2  
  
# Install Mapstore2  
RUN cd /srv/ && git clone \--recursive https://github.com/geosolutions-
it/MapStore2.git && \  
cd /srv/MapStore2 && npm install -g docma && npm cache clean && npm install &&
\  
sed -i 's/--port 8081/--host 0.0.0.0 --port 3002/g'
/srv/MapStore2/package.json  
  
# Copy scripts and configuration files  
ADD gisserver.conf /etc/apache2/sites-available/gisserver.conf  
ADD mapcache.load /etc/apache2/mods-available/mapcache.load  
ADD scripts/apache2.sh /usr/local/bin/apache2.sh  
ADD scripts/terriamap.sh /usr/local/bin/terriamap.sh  
ADD scripts/mapstore2.sh /usr/local/bin/mapstore2.sh  
ADD scripts/metadata_database.sh /usr/local/bin/metadata_database.sh  
ADD scripts/metadata_import.sh /usr/local/bin/metadata_import.sh  
COPY site/ /var/www/  
RUN chown -R www-data:www-data /gisdata && chmod -R 777 /gisdata  
  
RUN a2enmod mapcache  
RUN a2dissite 000-default  
RUN a2ensite gisserver  
RUN a2enmod cgid  
  
RUN apt-get purge -y software-properties-common build-essential cmake ; \  
apt-get purge -y libfcgi-dev liblz-dev libpng-dev libgdal-dev libgeos-dev \  
libpixman-1-dev libsqlite0-dev libcurl4-openssl-dev \  
libaprutil1-dev libapr1-dev libjpeg-dev libdpkg-dev \  
libdb5.3-dev libtiff5-dev libpcre3-dev libfcgi-dev ; \  
apt-get autoremove -y ; \  
apt-get clean ; \  
rm -rf /var/lib/apt/lists/partial/* /tmp/* /var/tmp/* /usr/local/src/*  
  
RUN apt autoremove  
  
WORKDIR /gisdata  
VOLUME [ "/gisdata/projects", "/gisdata/tiles", "/mapcache/",
"/gisdata/metadata", "/var/www/tileserver-php" ]  
  
EXPOSE 3001  
EXPOSE 3002  
EXPOSE 80  
CMD ["bash", "apache2.sh"]  

