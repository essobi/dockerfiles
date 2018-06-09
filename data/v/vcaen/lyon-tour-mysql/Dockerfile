FROM mysql:latest  
  
ENV MYSQL_ROOT_PASSWORD password  
ENV MYSQL_PASSWORD password  
ENV MYSQL_DATABASE lyon_tour  
ENV MYSQL_USER h4312  
  
CMD sed -i "s/^bind-address/#bind-address/" /etc/mysql/my.cnf  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]

