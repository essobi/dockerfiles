FROM ubuntu  
  
MAINTAINER Maksim Ekimovskii <ekimovsky.maksim@gmail.com>  
  
# Add the PostgreSQL PGP key to verify their Debian packages.  
# It should be the same key as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
# Add PostgreSQL's repository. It contains the most recent stable release  
# of PostgreSQL, ``9.3``.  
# RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
# Set locales and test database  
RUN locale-gen --no-purge en_US.UTF-8  
ENV LC_ALL="en_US.UTF-8" POSTGIS_DB="test_db"  
RUN update-locale LANG=en_US.UTF-8  
  
# Install dependencies  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y python-software-properties \  
software-properties-common \  
postgresql-9.3 \  
postgresql-client-9.3 \  
postgresql-contrib-9.3 \  
postgresql-9.3-postgis-2.1  
  
# Adjust PostgreSQL configuration so that remote connections to the database
are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf
&& \  
echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
# Run all futher commands from postgres user  
USER postgres  
  
# Create new ROLE 'docker' with password 'docker'  
RUN /etc/init.d/postgresql start && \  
psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" && \  
createdb -O docker "$POSTGIS_DB"  
# Setup postgis extension  
RUN /etc/init.d/postgresql restart && \  
psql -d "$POSTGIS_DB" -c "CREATE EXTENSION postgis;" && \  
psql -d "$POSTGIS_DB" -c "CREATE EXTENSION postgis_topology;"  
# Expose the PostgreSQL port  
EXPOSE 5432  
  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
# Set the default command to run when starting the container  
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D",
"/var/lib/postgresql/9.3/main", "-c",
"config_file=/etc/postgresql/9.3/main/postgresql.conf"]  

