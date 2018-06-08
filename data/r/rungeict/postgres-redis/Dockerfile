FROM postgres:9.5.4  
  
RUN apt-get update \  
&& apt-get -y install git gcc make libhiredis-dev libpq-dev postgresql-server-
dev-9.5 \  
&& mkdir -p /inst/ \  
&& cd /inst \  
&& git clone https://github.com/pg-redis-fdw/redis_fdw.git \--branch
REL9_5_STABLE --single-branch \  
&& cd /inst/redis_fdw \  
&& PATH=/usr/local/postgresql/bin/:$PATH make USE_PGXS=1 \  
&& PATH=/usr/local/postgresql/bin/:$PATH make USE_PGXS=1 install \  
&& apt-get purge -y \--auto-remove git gcc make \  
&& rm -Rf /inst  

