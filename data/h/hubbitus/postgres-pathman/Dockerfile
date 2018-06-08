# https://hub.docker.com/_/postgres/  
FROM postgres:9.6  
MAINTAINER Pavel Alexeev  
  
COPY docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/  
COPY docker-entrypoint-after-initdb.sh /  
  
RUN echo '1) Install required packages' \  
&& apt-get update \  
&& apt-get install -y \  
gcc \  
git \  
make \  
postgresql-server-dev-9.6 \  
postgresql-plpython-9.6 \  
sed \  
&& echo '2) Install pg_pathman extension' \  
&& git clone https://github.com/postgrespro/pg_pathman
`#https://github.com/postgrespro/pg_pathman/blob/master/README.rus.md` \  
&& cd pg_pathman \  
&& make install USE_PGXS=1 \  
&& echo 'Hack postgres config after init (see FR @issue
https://github.com/docker-library/postgres/issues/232):' \  
&& sed -i.orig '/eval "gosu postgres initdb/a \\\n\t\tsource docker-
entrypoint-after-initdb.sh' /docker-entrypoint.sh \  
&& apt-get remove \--purge --auto-remove gcc git make postgresql-server-
dev-9.6 -y \  
&& rm -rf /var/lib/apt/lists/* /pg_pathman  

