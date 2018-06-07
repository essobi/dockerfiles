FROM postgres  
RUN apt-get update  
RUN apt-get install -y -q postgresql-9.4 libpq-dev postgresql-client-9.4
postgresql-contrib-9.4  
RUN apt-get install -y vim  
  
RUN pg_createcluster 9.4 main --start  
  
USER postgres  
  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER depotica WITH SUPERUSER PASSWORD 'depotica';" &&\  
createdb -O depotica depotica  
  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.4/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf  
  
EXPOSE 5432  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
CMD ["/usr/lib/postgresql/9.4/bin/postgres", "-D",
"/var/lib/postgresql/9.4/main", "-c",
"config_file=/etc/postgresql/9.4/main/postgresql.conf"]  

