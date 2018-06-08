FROM postgres:9.6  
MAINTAINER Rafael Mello <merorafael@gmail.com>  
ENV PLV8_VERSION=v1.5.1 \  
PLV8_SHASUM="b577c26b4538e9e3e14d96760af53ad7ab516cf89bf5873f107a6faa8156c2c8
v1.5.1.tar.gz"  
RUN apt-get update \  
&& apt-get install -y \  
postgresql-${PG_MAJOR}-plv8 \  
postgresql-plperl-${PG_MAJOR} \  
postgresql-pltcl-${PG_MAJOR}  
RUN apt-get clean \  
&& rm -rf /tmp/build /var/lib/apt/lists/*  
  
RUN echo 'CREATE EXTENSION plv8;' > /docker-entrypoint-initdb.d/create-
plv8.sql \  
&& echo 'CREATE EXTENSION plperl;' > /docker-entrypoint-initdb.d/create-
plperl.sql \  
&& echo 'CREATE EXTENSION pltcl;' > /docker-entrypoint-initdb.d/create-
pltcl.sql  

