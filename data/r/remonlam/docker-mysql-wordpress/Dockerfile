FROM mysql  
MAINTAINER Remon Lam <remon.lam@virtualclouds.info>  
  
ENV MYSQL_USER mysql  
  
COPY ./osx-start-db.sh /  
RUN chmod 755 /osx-start-db.sh  
  
ENTRYPOINT ["/osx-start-db.sh"]  

