FROM mysql  
MAINTAINER Gabrie van Zanten <thegabeman@gmail.com>  
  
#  
# The nest-init.sql file creates an empty 'nest' database with table 'raw'.  
# By placing it in the /docker-entrypoint-initdb.d this will be executed when
the container is initialized  
ADD nest-init.sql /docker-entrypoint-initdb.d  
RUN chmod 775 /docker-entrypoint-initdb.d/nest-init.sql  
ENV MYSQL_ROOT_PASSWORD=L@mpMyG@B  

