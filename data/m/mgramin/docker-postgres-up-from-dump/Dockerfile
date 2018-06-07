FROM postgres  
  
RUN mkdir -p /var/lib/postgresql-static/data  
ENV PGDATA /var/lib/postgresql-static/data  
  
RUN apt-get update  
RUN apt-get install wget unzip -y  
  
ARG DUMP_URI=https://edu.postgrespro.ru/demo_small.zip  
RUN wget --output-document=dbdump.zip $DUMP_URI  
RUN unzip dbdump.zip -d dbdump  
  
RUN echo "psql -U postgres -f /dbdump/demo_small.sql" > /docker-entrypoint-
initdb.d/run_dbdump.sh  

