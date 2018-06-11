FROM mdillon/postgis:9.5  
MAINTAINER Wayner Barrios <waybarrios@gmail.com>  
  
# Copy init command.  
COPY init_db.sh /docker-entrypoint-initdb.d/  
  
ENV PGDATA=/var/lib/postgresql/data_docker  
  
# Shut up a warning emitted by docker-entrypoint.sh  
ENV POSTGRES_PASSWORD=postgres  
# Normally docker-entrypoint.sh hangs at the end, here we pass --version as  
# a kludge to keep it from hanging in the foreground during build time.  
RUN /docker-entrypoint.sh postgres --version  
  
# Since we already ran docker-entrypoint.sh at startup, it is redundant and  
# slow to run it again, so override the ENTRYPOINT from Postgres Dockerfile  
ENTRYPOINT []  
  
# Start the service like the entrypoint does after it is done with init  
CMD ["gosu", "postgres", "postgres"]  
  

