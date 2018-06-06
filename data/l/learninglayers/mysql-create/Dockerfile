FROM learninglayers/base  
  
MAINTAINER István Koren  
  
RUN apt-get -y install mysql-client pwgen  
  
COPY create-database-user.sh /create-database-user.sh  
RUN chmod +x /create-database-user.sh  
ENTRYPOINT ["/create-database-user.sh"]  

