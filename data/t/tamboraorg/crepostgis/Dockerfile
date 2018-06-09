# Adapted from mdillon/postgis:9.5  
#FROM postgres:9.5  
FROM tamboraorg/crepostgres  
MAINTAINER Michael Kahle <michael.kahle@yahoo.de>  
  
ENV POSTGIS_MAJOR 2.3  
#ENV POSTGIS_MAJOR 2.2  
#ENV POSTGIS_VERSION 2.3.2+dfsg-1~exp2.pgdg80+1  
#ENV POSTGIS_VERSION 2.3.2+dfsg-1~exp2.pgdg16.04+1  
#RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release
-sc) main universe restricted multiverse"  
RUN add-apt-repository ppa:ubuntugis/ppa  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
postgresql-$PG_VERSION-postgis-$POSTGIS_MAJOR  
RUN apt-get install -y --no-install-recommends \  
postgresql-$PG_VERSION-postgis-$POSTGIS_MAJOR-scripts  
RUN apt-get install -y --no-install-recommends \  
postgis  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /docker-entrypoint-initdb.d  
COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh  
COPY ./update-postgis.sh /usr/local/bin  

