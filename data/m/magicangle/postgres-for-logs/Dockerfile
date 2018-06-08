FROM postgres:9.6  
# Install WAL-E and dependencies for PITR backups  
# postgresql-server-dev is necessary to install extensions  
# Install pgxn client to install Postgres extensions  
RUN apt-get update && apt-get install -y python3-pip python3.4 lzop pv
daemontools && \  
pip3 install wal-e[aws] && \  
apt-get install -y postgresql-server-dev-$PG_MAJOR=$PG_VERSION && \  
apt-get install -y pgxnclient && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install temporal tables extension for Postgres  
RUN pgxn install temporal_tables  
  
COPY postgresql.conf /postgresql.conf  
COPY pg_hba.conf /pg_hba.conf  
COPY init.sh /docker-entrypoint-initdb.d/init.sh  
  
RUN chmod 777 /postgresql.conf  
RUN chmod 777 /pg_hba.conf  
RUN chmod a+r /docker-entrypoint-initdb.d/*

