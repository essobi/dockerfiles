FROM ubuntu  
MAINTAINER obed.n.munoz@gmail.com  
  
RUN apt-get update -y  
RUN apt-get install -y mariadb-server python-mysqldb  
RUN sed -i '/bind-address/d' /etc/mysql/my.cnf  
RUN service mysql start && mysqladmin -uroot password secure  
RUN service mysql start && mysql -uroot -psecure -e "GRANT ALL ON *.* to
'root'@'%' IDENTIFIED BY 'secure' WITH GRANT OPTION"  
  
EXPOSE 3306  
CMD ["mysqld_safe"]

