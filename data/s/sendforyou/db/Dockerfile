FROM mariadb  
MAINTAINER Allan Sun <allan.sun@bricre.com>  
  
ADD init.sh /init.sh  
RUN chmod +x /init.sh  
ADD seed-data /docker-entrypoint-initdb.d  
CMD ["/init.sh"]

