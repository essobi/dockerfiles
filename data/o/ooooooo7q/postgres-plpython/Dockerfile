FROM postgres:9.3  
RUN apt-get update && apt-get install -y postgresql-plpython-${PG_MAJOR}  
  
ENV POSTGIS_VERSION 2.1.8  
ENV POSTGIS_SHA256
7c2380b895fe7bda34c2e70deab3fcf4c12b13ab40d7501cdaa6fa36f1a6c662  
  
RUN apt-get install -y postgresql-server-dev-9.3 gcc wget libgeos-dev
libxml2-dev libproj-dev proj-data proj-bin libgdal-dev make \  
&& cd /tmp \  
&& wget -O postgis.tar.gz
"http://download.osgeo.org/postgis/source/postgis-${POSTGIS_VERSION}.tar.gz" \  
&& echo "$POSTGIS_SHA256 *postgis.tar.gz" | sha256sum -c - \  
&& tar xvzf postgis.tar.gz \  
&& cd "postgis-$POSTGIS_VERSION" \  
&& ./configure \  
&& make \  
&& make install \  
&& echo 'CREATE EXTENSION plpythonu;' > /docker-entrypoint-
initdb.d/plpythonu.sql \  
&& echo 'CREATE EXTENSION postgis;' > /docker-entrypoint-
initdb.d/plpythonu.sql \  
&& echo 'CREATE EXTENSION fuzzystrmatch;' > /docker-entrypoint-
initdb.d/plpythonu.sql  

