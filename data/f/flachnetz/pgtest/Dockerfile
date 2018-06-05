FROM postgres:10.1-alpine  
  
# move data away from the volume  
ENV PGDATA=/pg  
  
# run initdb to setup the database  
RUN /docker-entrypoint.sh postgres --version  
  
# directly start the postgres without running setup scripts  
USER postgres  
ENTRYPOINT ["/usr/local/bin/postgres", "-D", "/pg"]  

