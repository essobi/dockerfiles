#Dockerfile untuk membuat Image MySQL server  
FROM ubuntu  
  
RUN apt-get update && apt-get -y install mysql-client mysql-server  
RUN sed -i 's/^bind-address/#bind-adress/g' /etc/mysql/my.cnf  
RUN /etc/init.d/mysql start && echo "GRANT ALL ON *.* TO admin@'%' IDENTIFIED
BY 'admin123' WITH GRANT OPTION; FLUSH PRIVILEGES" | mysql -u root  
  
EXPOSE 3306  
CMD ["/usr/bin/mysqld_safe"]  

