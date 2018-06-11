#docker file for mysql db  
FROM ubuntu:latest  
#Maintainer  
MAINTAINER stephan mgaya <smgayanath@gmail.com>  
#run bash script  
ADD ./database.sh /tmp/database.sh  
RUN chmod +x /tmp/database.sh  
  
# Adding this will expose mysql on a random host port. It's recommended to
avoid this. Other containers on the same  
# host can use the service without it.  
EXPOSE 3306  
CMD ["/usr/sbin/mysqld"]  

