# DOCKER-VERSION 1.5.0  
# VERSION 0.2  
FROM phusion/baseimage  
MAINTAINER julien-noblet  
  
  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
ENV PGSQL_VERSION 9.3  
ENV POSTGIS_MAJOR 2.1  
ENV POSTGIS_VERSION 2.1.7+dfsg-3~94.git954a8d0.pgdg80+1  
ENV OSM2PGSQL_VERSION 0.88.0  
ENV PG_PORT 5432  
ENV PG_USER gisuser  
ENV PG_DB gis  
EXPOSE $PG_PORT  
  
  
  
RUN apt-get update &&\  
apt-get install -y wget ca-certificates &&\  
apt-get install -y \  
postgresql-$PGSQL_VERSION \  
postgresql-contrib \  
postgresql-$PGSQL_VERSION-postgis-$POSTGIS_MAJOR \  
postgis\  
autoconf\  
automake\  
g++\  
git\  
make\  
libtool\  
liblua5.2-dev\  
lua5.2\  
libboost-dev\  
libboost-filesystem-dev\  
libboost-system-dev\  
libboost-thread-dev\  
libbz2-dev\  
libgeos++-dev\  
libgeos-dev\  
libpq-dev\  
libproj-dev\  
libprotobuf-c0-dev\  
protobuf-c-compiler\  
libxml2-dev\  
golang\  
unzip\  
&& apt-get clean\  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /root/src  
  
RUN /etc/init.d/postgresql restart &&\  
sudo -u postgres createuser $PG_USER &&\  
sudo -u postgres createdb --encoding=UTF8 --owner=$PG_USER $PG_DB &&\  
/etc/init.d/postgresql stop  
  
#RUN pg_createcluster --port=$PG_PORT -d /pg $PGSQL_VERSION pg  
RUN echo "host all all 0.0.0.0/0 md5" >>
/etc/postgresql/$PGSQL_VERSION/main/pg_hba.conf  
  
RUN echo "listen_addresses='*'" >>
/etc/postgresql/$PGSQL_VERSION/main/postgresql.conf  
VOLUME ["/data", "/etc/postgresql", "/var/log/postgresql",
"/var/lib/postgresql"]  
  
RUN /etc/init.d/postgresql restart &&\  
sudo -u postgres psql -d gis -f
/usr/share/postgresql/9.3/contrib/postgis-2.1/postgis.sql &&\  
sudo -u postgres psql -d gis -f
/usr/share/postgresql/9.3/contrib/postgis-2.1/spatial_ref_sys.sql &&\  
sudo -u postgres psql -d gis -f
/usr/share/postgresql/9.3/contrib/postgis-2.1/postgis_comments.sql &&\  
sudo -u postgres psql -d gis -c "GRANT SELECT ON spatial_ref_sys TO PUBLIC;"
&&\  
sudo -u postgres psql -d gis -c "GRANT ALL ON geometry_columns TO gisuser;"
&&\  
/etc/init.d/postgresql restart  
  
#ADD
https://github.com/openstreetmap/osm2pgsql/archive/$OSM2PGSQL_VERSION.tar.gz
/root/src/  
#ADD https://github.com/julien-noblet/download-
geofabrik/releases/download/v0.0.1/download-geofabrik-linux32.zip /root/src/  
#RUN cd /root/src/ &&\  
# tar -zxvf $OSM2PGSQL_VERSION.tar.gz &&\  
# cd osm2pgsql-$OSM2PGSQL_VERSION &&\  
# ./autogen.sh &&\  
# ./configure &&\  
# make &&\  
# make install &&\  
# cd /root/src/ &&\  
# unzip download-geofabrik-linux32.zip &&\  
# mv download-geofabrik /usr/bin/ \  
# && rm -rf /root/src  
ENV GOPATH=/root/go/  
  
RUN go get github.com/julien-noblet/download-geofabrik  
RUN go install github.com/julien-noblet/download-geofabrik  
RUN cd ~/go/src/github.com/julien-noblet/download-geofabrik &&\  
go build &&\  
mv download-geofabrik /usr/bin/  
  
RUN go get github.com/omniscale/imposm3  
RUN go install github.com/omniscale/imposm3  
RUN cd ~/go/src/github.com/omniscale/imposm3 &&\  
go build &&\  
cp imposm3 /usr/bin  
  
#RUN echo "localhost:$PG_PORT:*:pggis:pggis" > /root/.pgpass  
#RUN chmod 700 /root/.pgpass  
#RUN mkdir -p /etc/my_init.d  
#ADD init_db_script.sh /etc/my_init.d/init_db_script.sh  
#ADD init_db.sh /root/init_db.sh  
ENTRYPOINT ["/bin/bash"]  

