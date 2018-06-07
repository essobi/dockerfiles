FROM mysql:5.7.19  
# ENV MYSQL_RANDOM_ROOT_PASSWORD=yes  
# ENV MYSQL_ONETIME_PASSWORD=yes  
ENV MYSQL_ROOT_PASSWORD=password  
# ENV MYSQL_USER=admincdb  
# ENV MYSQL_PASSWORD=qwerty1234  
COPY db/file/* /docker-entrypoint-initdb.d/  
  
ADD db/my.cnf /etc/mysql/my.cnf  
# RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
EXPOSE 3306  

