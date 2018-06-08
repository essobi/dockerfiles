FROM postgres:9.6  
  
RUN apt-get update && \  
apt-get install -y cmake pgxnclient postgresql-plpython-9.6 postgresql-server-
dev-9.6 g++ m4  
RUN pgxn install madlib=1.11  
# TODO clean up  

