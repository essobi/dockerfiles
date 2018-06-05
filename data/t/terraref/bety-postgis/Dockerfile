FROM mdillon/postgis  
  
ENV PG_USER=postgres  
ENV POSTGRES_USER=bety  
ENV POSTGRES_DB=bety  
ENV POSTGRES_PASSWORD=bety  
  
RUN apt-get update -y && apt-get install curl vim -y && mkdir /bety && chown
postgres /bety  
  
COPY init-bety.sh /bety/  
COPY revoke_select_from_bety_user.sql /bety/  
COPY update.sh /bety/  
  
RUN ln -s /bety/update.sh /etc/cron.daily && \  
ln -s /bety/init-bety.sh /docker-entrypoint-initdb.d/zzbety.sh  

