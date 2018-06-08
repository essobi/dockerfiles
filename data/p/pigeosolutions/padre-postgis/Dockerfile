######################################  
# PostGIS container for Padre1 instance  
# Contains 2 databases :  
# - geonetwork DB (created by geonetwork on first startup)  
# - geodata DB (postgis DB)  
######################################  
FROM camptocamp/postgis:9.6  
MAINTAINER Jean Pommier <jean.pommier@pi-geosolutions.fr>  
  
#set locale as documented in https://hub.docker.com/_/postgres/  
RUN localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias
fr_FR.UTF-8  
ENV LANG fr_FR.utf8  
  
ENV POSTGRES_USER postgres  
#ENV POSTGRES_DB geodata  
  
#Setup BD backup script (backups stored in /backups/)  
COPY ./backupPGSQL.sh /root/backupPGSQL.sh  
RUN chmod +x /root/backupPGSQL.sh  
  
#COPY ./pg_hba.conf $PGDATA/  
#RUN chmod 600 $PGDATA/pg_hba.conf  
  
ADD sql/*.sql /docker-entrypoint-initdb.d/  
ADD sh/*.sh /docker-entrypoint-initdb.d/  

