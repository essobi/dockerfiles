FROM tozd/runit:ubuntu-trusty  
  
EXPOSE 5432/tcp  
  
VOLUME /var/log/postgresql  
VOLUME /var/lib/postgresql  
  
ENV PGSQL_ROLE_1_USERNAME=  
ENV PGSQL_ROLE_1_PASSWORD=  
ENV PGSQL_ROLE_1_FLAGS LOGIN  
  
ENV PGSQL_DB_1_NAME=  
ENV PGSQL_DB_1_OWNER=  
ENV PGSQL_DB_1_ENCODING UNICODE  
ENV PGSQL_DB_1_LC_COLLATE=  
ENV PGSQL_DB_1_LC_CTYPE=  
ENV PGSQL_DB_1_TEMPLATE=DEFAULT  
ENV PGSQL_DB_1_POSTGIS=  
  
RUN apt-get update -q -q && \  
apt-get --yes --force-yes install wget ca-certificates && \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - && \  
apt-get update -q -q && \  
locale-gen --no-purge en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8 && \  
echo locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8 |
debconf-set-selections && \  
echo locales locales/default_environment_locale select en_US.UTF-8 | debconf-
set-selections && \  
dpkg-reconfigure locales && \  
apt-get --no-install-recommends --yes --force-yes install postgresql-9.5
postgresql-9.5-postgis-2.2 postgresql-9.5-postgis-2.2-scripts && \  
mkdir -m 700 /var/lib/postgresql.orig && \  
mv /var/lib/postgresql/* /var/lib/postgresql.orig/ && \  
echo 'mappostgres postgres postgres' >> /etc/postgresql/9.5/main/pg_ident.conf
&& \  
echo 'mappostgres root postgres' >> /etc/postgresql/9.5/main/pg_ident.conf &&
\  
echo 'host all all 0.0.0.0/0 md5' >> /etc/postgresql/9.5/main/pg_hba.conf && \  
echo 'hostssl all all 0.0.0.0/0 md5' >> /etc/postgresql/9.5/main/pg_hba.conf
&& \  
sed -r -i 's/local\s+all\s+postgres\s+peer/local all postgres peer
map=mappostgres/' /etc/postgresql/9.5/main/pg_hba.conf && \  
echo "include_dir = 'conf.d'" >> /etc/postgresql/9.5/main/postgresql.conf && \  
mkdir -p /var/run/postgresql/9.5-main.pg_stat_tmp && \  
chown postgres:postgres /var/run/postgresql/9.5-main.pg_stat_tmp  
  
COPY ./etc /etc  
COPY ./postgresql /etc/postgresql/9.5  

