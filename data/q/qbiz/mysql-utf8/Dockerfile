  
FROM mysql:latest  
  
COPY mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf  
  
RUN apt-get update && apt-get install -y \  
pv \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV MYSQL_ROOT_PASSWORD 123456  
ENV LANG C.UTF-8

