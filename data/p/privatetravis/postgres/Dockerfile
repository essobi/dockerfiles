FROM privatetravis/base  
MAINTAINER nick_schuch  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PG_VERSION 9.1  
ENV PG_USER postgres  
ENV PG_PASS postgres  
  
##  
# Packages.  
##  
RUN apt-get update  
RUN apt-get -y install postgresql postgresql-client postgresql-contrib  
  
##  
# Configuration.  
##  
RUN echo "host all all 0.0.0.0/0 trust" >>
/etc/postgresql/$PG_VERSION/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >>
/etc/postgresql/$PG_VERSION/main/postgresql.conf  
  
RUN service postgresql start && \  
su postgres sh -c "psql -c \"ALTER USER $PG_USER PASSWORD '$PG_PASS';\""  
  
##  
# Run tests.  
##  
ADD Rakefile Rakefile  
COPY spec spec  
RUN rake spec  
  
EXPOSE 5432  
CMD ["su", "postgres", "-c", "/usr/lib/postgresql/$PG_VERSION/bin/postgres -D
/var/lib/postgresql/$PG_VERSION/main/ -c
config_file=/etc/postgresql/$PG_VERSION/main/postgresql.conf"]  

