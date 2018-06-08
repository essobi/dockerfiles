FROM postgres:9.3.10  
MAINTAINER Jakob Runge <runjak@gmail.com>  
  
LABEL lingdb="postgres_create" \  
version="1.1.2" \  
documentation="https://github.com/lingdb/container/wiki/postgres#the-
postgrescreate-container"  
  
COPY create.sh /  
  
RUN mkdir /create && \  
chmod u+x /create.sh  
  
ENTRYPOINT /create.sh  

