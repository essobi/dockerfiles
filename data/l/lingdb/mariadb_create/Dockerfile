FROM mariadb:latest  
  
MAINTAINER Jakob Runge <runjak@gmail.com>  
  
LABEL lingdb="mariadb_create" \  
version="1.2.2" \  
documentation="https://github.com/lingdb/container/wiki/mariadb#the-
mariadbcreate-container"  
  
COPY create.sh /create.sh  
  
RUN mkdir /create && \  
chmod u+x /create.sh  
  
ENTRYPOINT /create.sh  

