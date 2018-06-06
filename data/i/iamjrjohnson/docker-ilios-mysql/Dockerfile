FROM mysql:5.6  
# customized to install ilios demo database  
MAINTAINER Jonathan Johnson <jon.johnson@ucsf.edu>  
ENV MYSQL_RANDOM_ROOT_PASSWORD yes  
  
COPY ilios-mysql.cnf /etc/mysql/conf.d/ilios.cnf  
  
EXPOSE 3306  
CMD ["mysqld"]  

