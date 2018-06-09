FROM postgres:9.5  
MAINTAINER Gael Abadin (github.com/elcodedocle)  
  
ENV POSTGRES_MAJOR 9.5  
ENV POSTGIS_MAJOR 2.2  
ENV POSTGIS_VERSION 2.2.2+dfsg-1.pgdg80+1  
ENV PG_CONF_DIR /var/lib/postgresql/data  
ENV PG_CONF postgresql.conf  
ENV PG_CONF_HBA pg_hba.conf  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gpasswd -a postgres ssl-cert  
RUN cp -r /etc/ssl /tmp/ssl-copy/  
RUN chmod -R 0700 /etc/ssl  
RUN chown -R postgres /tmp/ssl-copy  
RUN rm -r /etc/ssl  
RUN mv /tmp/ssl-copy /etc/ssl  
RUN chmod 600 /etc/ssl/private/ssl-cert-snakeoil.key  
  
RUN mkdir -p /docker-entrypoint-initdb.d  
COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh  

