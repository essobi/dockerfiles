FROM mdillon/postgis:10  
MAINTAINER viet@openbeta.io  
  
RUN apt-get update \  
&& apt-get install -y \  
make gcc libpq-dev ca-certificates postgresql-server-dev-10 postgresql-contrib
pgxnclient \  
&& rm -rf /var/lib/apt/lists/* \  
&& pgxnclient install temporal_tables --verbose  
  
COPY ./init-extension.sh /docker-entrypoint-initdb.d/temporal_tables.sh

