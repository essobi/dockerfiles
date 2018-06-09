FROM ubuntu:14.04  
#FROM stencila/ubuntu-14.04  
MAINTAINER Xavier Barnada <xbarnada@gmail.com>  
RUN apt-get -y update  
RUN apt-get -y install python-dev npm  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list  
RUN apt-get -y update  
RUN apt-get -y install ca-certificates  
RUN apt-get -y install wget  
RUN wget --quiet --no-check-certificate -O -
https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >>
/etc/apt/sources.list  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get -y install postgresql-9.4 postgresql-contrib-9.4
postgresql-9.4-postgis-2.1 postgis  
RUN echo "host all all 0.0.0.0/0 trust" >>
/etc/postgresql/9.4/main/pg_hba.conf  
RUN service postgresql start && /bin/su postgres -c "createuser -d -s -r -l
docker" && /bin/su postgres -c "psql postgres -c \"ALTER USER docker WITH
ENCRYPTED PASSWORD 'docker'\"" && service postgresql stop  
RUN echo "listen_addresses = '*'" >> /etc/postgresql/9.4/main/postgresql.conf  
RUN echo "port = 5432" >> /etc/postgresql/9.4/main/postgresql.conf  
COPY style /style  
  
RUN echo "deb http://ppa.launchpad.net/mapnik/nightly-2.3/ubuntu trusty
main">>/etc/apt/sources.list  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 4F7B93595D50B6BA  
RUN apt-get update  
  
RUN apt-get -y install mapnik-input-plugin-gdal mapnik-input-plugin-ogr
mapnik-input-plugin-postgis mapnik-input-plugin-sqlite mapnik-input-plugin-osm
python-pip ttf-dejavu ttf-dejavu-core ttf-dejavu-extra ttf-unifont osm2pgsql
curl bzip2 unzip mapnik-utils gdal-bin  
  
COPY default.style /usr/share/osm2pgsql/default.style  
  
RUN npm install -g
https://github.com/gisce/carto/archive/extends_zoom_level.tar.gz  
RUN pip install https://github.com/TileStache/TileStache/archive/master.zip
sympy Blit uwsgi mapnik  
EXPOSE 5432  
ADD update.sh /update.sh  
RUN chmod 777 /update.sh  
  
ADD start.sh /start.sh  
ADD start_tilestache.py /start_tilestache.py  
ADD mapserver.cfg /mapserver.cfg  
  
RUN chmod 0755 /start.sh  
RUN chmod 0755 /start_tilestache.py  
  
CMD ["/start.sh"]  

