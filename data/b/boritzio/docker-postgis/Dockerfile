FROM boritzio/docker-base  
  
ENV PG_VERSION=9.6  
ENV POSTGIS_VERSION=2.3  
#postgres  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ "$(lsb_release
-sc)"-pgdg main" >> /etc/apt/sources.list.d/pgdg.list  
RUN curl -s https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -  
  
RUN apt-get update && apt-get install -y postgresql-$PG_VERSION postgresql-
contrib-$PG_VERSION postgis postgresql-$PG_VERSION-postgis-$POSTGIS_VERSION  
  
ADD pg_hba.conf /etc/postgresql/$PG_VERSION/main/pg_hba.conf  
ADD postgresql.conf /etc/postgresql/$PG_VERSION/main/postgresql.conf  
  
RUN sed -i "s/{{PG_VERSION}}/$PG_VERSION/"
/etc/postgresql/$PG_VERSION/main/postgresql.conf  
  
RUN mkdir -p /data  
  
ENV POSTGRES="/usr/lib/postgresql/$PG_VERSION/bin/postgres"  
ENV CONFIG_PATH="/etc/postgresql/$PG_VERSION/main/"  
VOLUME ["/data"]  
  
ADD configure_postgres.sh /etc/my_init.d/01_configure_postgres  
ADD bootstrap.sh /etc/my_init.d/09_bootstrap  
ADD start_postgres.sh /etc/my_init.d/99_start_postgres  
  
#cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

