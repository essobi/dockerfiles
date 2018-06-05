FROM debian:jessie  
MAINTAINER simon@simonluijk.com  
  
RUN echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb ||
true";};' | tee /etc/apt/apt.conf.d/no-cache && \  
apt-get update -y && \  
apt-get dist-upgrade -y && \  
apt-get install -y apt-utils wget telnet curl cron && \  
apt-get clean && rm -rf /var/cache/apt/*  
  
ENV PG_VERSION=9.4  
ENV GIS_VERSION=2.1  
RUN apt-get install -y postgresql postgresql-client \  
postgis postgresql-$PG_VERSION-postgis-$GIS_VERSION && \  
apt-get clean && rm -rf /var/cache/apt/*  
  
ENV PGCONF /etc/postgresql/$PG_VERSION/main  
ENV PGDATA /var/lib/postgresql/$PG_VERSION/main  
ENV PGBIN /usr/lib/postgresql/$PG_VERSION/bin  
ENV PATH $PGBIN:$PATH  
  
RUN sed -ri "s/^#(listen_addresses\s*=\s*)\S+/\1'*'/"
"$PGCONF"/postgresql.conf  
RUN { echo; echo "host all all 0.0.0.0/0 trust"; } >> "$PGCONF"/pg_hba.conf  
  
VOLUME ["/var/log/postgresql", "/var/lib/postgresql"]  
  
EXPOSE 5432  
ADD start.sh /opt/start.sh  
ENTRYPOINT ["/opt/start.sh"]  

