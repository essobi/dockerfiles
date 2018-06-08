# Development docker postgres database,  
# This is to mirror the current AWS postgres version, so pg_dump generates the
exact same output  
# Specific postgres version so it matches AWS postgres  
FROM postgres:9.3.20  
# Install necessary stuff  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential ca-certificates curl openssl wget \  
postgresql-server-dev-9.3 libv8-dev \  
  
# Add postgis (unfortunately, this is 2.3.1, not 2.1.8, but whatevah)  
postgresql-9.3-postgis-2.4 \  
postgresql-9.3-postgis-scripts \  
postgis\  
  
pgxnclient \  
  
# Clean apt cache for smaller docker  
# no apt-get allowed beyond this point  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pgxn install plv8=1.4.4  
# Prepare a spot for pgbadger  
RUN mkdir /var/lib/postgresql/pgbadgerlogs/  
RUN chmod 777 /var/lib/postgresql/pgbadgerlogs/  
  
  
ADD init/1_create_extensions.sql /docker-entrypoint-initdb.d/  
ADD init/2_demo.sh /docker-entrypoint-initdb.d/  
ADD init/3_pgbadger.sh /docker-entrypoint-initdb.d/  
  
# Prepare for PgBadger support  
COPY postgresql.pgbadger.conf $PGDATA/../  
VOLUME /var/lib/postgresql/pgbadgerlogs/  
  
EXPOSE 5432  
  
CMD ["postgres"]  

