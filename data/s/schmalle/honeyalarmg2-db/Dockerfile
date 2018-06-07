#  
# Basic mysql database server setup for honeyalarmg2  
#  
FROM mysql  
  
RUN mkdir /data  
  
WORKDIR "/data/"  
WORKDIR "/data/db"  
  
# add config file for database  
ADD ./configdb.sh /data/configdb.sh  
  
RUN /data/configdb.sh  
  
CMD ["service mysql start"]  

