FROM postgres:9.5  
RUN apt-get update \  
&& apt-get install -y g++ make libv8-dev git-core postgresql-server-
dev-${PG_MAJOR} postgresql-plpython-${PG_MAJOR}  
  
ENV PLV8_VERSION 1.4.4  
RUN git clone https://github.com/plv8/plv8.git /usr/src/plv8 \  
&& cd /usr/src/plv8 \  
&& git checkout tags/v${PLV8_VERSION} \  
&& make all install  
  
RUN echo 'CREATE EXTENSION plv8;' > /docker-entrypoint-initdb.d/plv8.sql  
RUN echo 'CREATE EXTENSION plpythonu;' > /docker-entrypoint-
initdb.d/plpythonu.sql

