FROM postgres:9.6.5  
ENV VERSION=0.15.0  
ADD https://raw.githubusercontent.com/eventuate-local/eventuate-
local/release_${VERSION}.RELEASE/postgres/initialize-database.sql /docker-
entrypoint-initdb.d  
RUN chmod +r /docker-entrypoint-initdb.d/initialize-database.sql  

