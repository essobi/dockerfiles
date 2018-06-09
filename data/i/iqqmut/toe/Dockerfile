FROM debian:7  
MAINTAINER Tuomas Jaakola <tuomas.jaakola@iki.fi>  
  
LABEL description="Environment for TOE"  
  
ENV TEST_MAP isle-of-man-latest  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && apt-get install -y
locales  
  
# Set the locale. This affects the encoding of the Postgresql template #
databases.  
ENV LANG C.UTF-8  
RUN update-locale LANG=C.UTF-8  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
bzip2 \  
curl \  
git \  
locales \  
mapnik-utils \  
nginx \  
osm2pgsql \  
php5-fpm \  
php5-gd \  
php5-sqlite \  
postgis \  
postgresql-9.1-postgis \  
postgresql-contrib-9.1 \  
python-cairo \  
python-cairo-dev \  
python-mapnik2 \  
python-urllib3 \  
python2.7-dev \  
subversion \  
supervisor \  
unzip \  
wget && \  
rm -rf /var/lib/apt/lists/* /var/tmp/*  
  
RUN cd /opt && \  
git clone https://github.com/iqqmut/toe && \  
# PHP QR Code library  
curl -L
http://sourceforge.net/projects/phpqrcode/files/releases/phpqrcode-2010100721_1.1.4.zip/download
> /tmp/phpqrcode.zip && \  
cd toe/export/lib && \  
unzip /tmp/phpqrcode.zip  
  
COPY config.php /opt/toe/  
COPY toe-export-config.php /opt/toe/export/config.php  
COPY nginx.conf /etc/nginx/  
COPY default.conf /etc/nginx/conf.d/  
COPY supervisord.conf /etc/supervisor/  
  
# tweak php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/display_errors = Off/display_errors = On/g" /etc/php5/fpm/php.ini
&& \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
&& \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php5/fpm/pool.d/www.conf  
  
# PostgreSQL tuning  
# http://wiki.openstreetmap.org/wiki/PostgreSQL  
RUN sed -i -e "s/shared_buffers = 32MB/shared_buffers = 128MB/g"
/etc/postgresql/9.1/main/postgresql.conf && \  
echo "maintenance_work_mem = 256MB" >>
/etc/postgresql/9.1/main/postgresql.conf && \  
echo "work_mem = 256MB" >> /etc/postgresql/9.1/main/postgresql.conf && \  
echo "autovacuum = off" >> /etc/postgresql/9.1/main/postgresql.conf && \  
# Allow all connections  
sed -i -e "s/peer/trust/g" /etc/postgresql/9.1/main/pg_hba.conf && \  
sed -i -e "s/md5/trust/g" /etc/postgresql/9.1/main/pg_hba.conf && \  
echo "listen_addresses='*'" >> /etc/postgresql/9.1/main/postgresql.conf  
  
# https://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/  
RUN mkdir /opt/osm && \  
cd /opt/osm && \  
svn co https://svn.openstreetmap.org/applications/rendering/mapnik mapnik-
style && \  
cd mapnik-style && \  
./get-coastlines.sh && \  
cd inc && \  
cp fontset-settings.xml.inc.template fontset-settings.xml.inc && \  
cp datasource-settings.xml.inc.template datasource-settings.xml.inc && \  
cp settings.xml.inc.template settings.xml.inc && \  
sed -i -e "s/%[(]symbols[)]/symbol/g" settings.xml.inc && \  
sed -i -e "s/%[(]epsg[)]s/900913/g" settings.xml.inc && \  
sed -i -e "s/%[(]world_boundaries[)]s/.\/world_boundaries\//g"
settings.xml.inc && \  
sed -i -e "s/%[(]prefix[)]s/planet_osm/g" settings.xml.inc && \  
sed -i -e "s/%[(]password[)]s//g" datasource-settings.xml.inc && \  
sed -i -e "s/%[(]host[)]s/localhost/g" datasource-settings.xml.inc && \  
sed -i -e "s/%[(]port[)]s//g" datasource-settings.xml.inc && \  
sed -i -e "s/%[(]user[)]s/gisuser/g" datasource-settings.xml.inc && \  
sed -i -e "s/%[(]dbname[)]s/gis/g" datasource-settings.xml.inc && \  
sed -i -e "s/%[(]estimate_extent[)]s/false/g" datasource-settings.xml.inc && \  
sed -i -e "s/%[(]extent[)]s/-20037508,-19929239,20037508,19929239/g"
datasource-settings.xml.inc  
  
# Install test map  
ADD http://download.geofabrik.de/europe/${TEST_MAP}.osm.pbf /opt/osm/maps/  
RUN chmod a+r -R /opt/osm/maps && \  
rm -rf /tmp/*  
  
USER postgres  
  
# http://wiki.openstreetmap.org/wiki/PostGIS/Installation  
RUN /etc/init.d/postgresql start && \  
psql --command "CREATE USER gisuser WITH SUPERUSER" && \  
createdb --encoding=UTF8 --owner=gisuser gis && \  
psql --username=postgres --dbname=gis -f
/usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql && \  
psql --username=postgres --dbname=gis -f
/usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql && \  
psql --username=postgres --dbname=gis -f
/usr/share/postgresql/9.1/contrib/postgis_comments.sql && \  
psql -d gis -c "GRANT SELECT ON spatial_ref_sys TO PUBLIC;" && \  
psql -d gis -c "GRANT ALL ON geometry_columns TO gisuser;" && \  
psql -d gis -c "CREATE EXTENSION hstore;"  
  
RUN /etc/init.d/postgresql start && \  
# wait for postgresql starting up  
sleep 10 && \  
osm2pgsql -k -U gisuser -d gis /opt/osm/maps/${TEST_MAP}.osm.pbf && \  
/etc/init.d/postgresql stop  
  
VOLUME ["/opt/toe"]  
  
EXPOSE 80  
USER root  
  
# Use supervisord to launch nginx and php5-fpm  
CMD ["/usr/bin/supervisord"]  

