FROM mysql:5.7.13  
ENV VERSION=0.15.0  
ADD https://raw.githubusercontent.com/eventuate-local/eventuate-
local/release_${VERSION}.RELEASE/mysql/replication.cnf /etc/mysql/conf.d  
ADD https://raw.githubusercontent.com/eventuate-local/eventuate-
local/release_${VERSION}.RELEASE/mysql/initialize-database.sql /docker-
entrypoint-initdb.d  
RUN chmod +r /etc/mysql/conf.d/replication.cnf /docker-entrypoint-
initdb.d/initialize-database.sql  

