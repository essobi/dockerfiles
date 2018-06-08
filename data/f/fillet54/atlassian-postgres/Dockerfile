FROM fillet54/postgres  
  
# Add Confluence DB and User  
RUN echo "CREATE ROLE confluenceadmin with CREATEROLE login superuser PASSWORD
'password1';" | \  
sudo -u postgres -H /usr/pgsql-${PGMAJOR}/bin/postgres --single -c
config_file=${PGDATA}/postgresql.conf -D ${PGDATA}  
RUN echo "CREATE DATABASE confluence;" | \  
sudo -u postgres -H /usr/pgsql-${PGMAJOR}/bin/postgres --single -c
config_file=${PGDATA}/postgresql.conf -D ${PGDATA}  
RUN echo "GRANT ALL PRIVILEGES ON DATABASE confluence to confluenceadmin;" | \  
sudo -u postgres -H /usr/pgsql-${PGMAJOR}/bin/postgres --single -c
config_file=${PGDATA}/postgresql.conf -D ${PGDATA}  
  

