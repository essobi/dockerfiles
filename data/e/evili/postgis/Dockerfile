FROM centos:7  
ENV CENTOS_VERSION=7 \  
PG_VERSION=9.6 \  
PG_NODOT=96 \  
POSTGIS_VERSION=2  
ENV PGDATA /var/lib/pgsql/${PG_VERSION}/data/  
  
# Install postgresql and postgis from Postgresql.org  
RUN cd /tmp && \  
yum install -y epel-release && \  
curl -o pgdg.rpm
http://yum.postgresql.org/${PG_VERSION}/redhat/rhel-${CENTOS_VERSION}-x86_64/pgdg-
redhat${PG_NODOT}-${PG_VERSION}-1.noarch.rpm && \  
yum localinstall -y pgdg.rpm && \  
yum upgrade -y && \  
yum install -y \  
postgis${POSTGIS_VERSION}_${PG_NODOT} \  
postgis${POSTGIS_VERSION}_${PG_NODOT}-client \  
postgis${POSTGIS_VERSION}_${PG_NODOT}-utils \  
pgrouting_${PG_NODOT} \  
postgresql${PG_NODOT}-contrib \  
postgresql${PG_NODOT}-server  
  
# A modified postgresql-setup without a call to sysctl  
COPY postgresql-setup /usr/pgsql-${PG_VERSION}/bin/postgresql${PG_NODOT}-setup  
COPY postgresql-entrypoint.sh /  
  
# Prepare database dirs  
RUN /usr/pgsql-${PG_VERSION}/bin/postgresql${PG_NODOT}-setup initdb  
  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> ${PGDATA}/pg_hba.conf  
  
# Expose postgres  
EXPOSE 5432  
# username postgres  
USER postgres  
  
# PSQL  
ENV PSQL /usr/pgsql-${PG_VERSION}/bin/psql  
  
# Create postgis extensions  
# Create postgis superuser  
RUN /usr/pgsql-${PG_VERSION}/bin/pg_ctl start -D ${PGDATA} -w && \  
${PSQL} -c "CREATE USER postgis WITH PASSWORD 'postgis' SUPERUSER" && \  
${PSQL} -c "CREATE DATABASE postgis WITH OWNER postgis" && \  
${PSQL} -c "CREATE EXTENSION cube" postgis && \  
${PSQL} -c "CREATE EXTENSION earthdistance" postgis && \  
${PSQL} -c "CREATE EXTENSION postgis" postgis && \  
${PSQL} -c "CREATE EXTENSION postgis_topology" postgis && \  
${PSQL} -c "CREATE EXTENSION fuzzystrmatch" postgis && \  
${PSQL} -c "CREATE EXTENSION postgis_tiger_geocoder" postgis && \  
${PSQL} -c "CREATE EXTENSION pgrouting" postgis && \  
/usr/pgsql-${PG_VERSION}/bin/pg_ctl stop -D ${PGDATA} -w  
  
# Start postgresql server  
ENTRYPOINT ["/postgresql-entrypoint.sh"]  
CMD ["-i"]  
  
# Dbdir  
VOLUME ["/var/lib/pgsql"]  

