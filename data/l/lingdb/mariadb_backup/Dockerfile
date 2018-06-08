FROM mariadb:latest  
  
MAINTAINER Jakob Runge <runjak@gmail.com>  
  
LABEL lingdb="mariadb_backup" \  
version="1.2.2" \  
documentation="https://github.com/lingdb/container/wiki/mariadb#the-
mariadbbackup-container"  
  
COPY dumpdb.sh /dumpdb.sh  
  
RUN mkdir /backup && \  
chmod u+x /dumpdb.sh  
  
ENTRYPOINT /dumpdb.sh  

