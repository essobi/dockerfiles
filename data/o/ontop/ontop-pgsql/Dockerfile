# build with  
# docker build -t ontop_psql .  
# run with  
# docker run --name ontop_psql_running -p 5432:5432 -e
POSTGRES_PASSWORD=postgres2 -d ontop_psql  
FROM postgres:9.6.2  
RUN apt-get update && apt-get install -y wget  
  
# copying all SQL files to this folder will automatically put them in the
default DB  
COPY sql/*.sql /docker-entrypoint-initdb.d/  
  
COPY sql/*.dump /tmp/sql_scripts/  
  
COPY load-scripts-postgres.sh /docker-entrypoint-initdb.d/  
  
#get imdb database dump file  
RUN wget -P /tmp/sql_scripts/ -o log
http://obdavm.inf.unibz.it/dumps/imdbobda-pgsql.dump

