FROM eventuateio/eventuateio-local-mysql:0.14.0  
ENV VERSION=0.2.0  
COPY replication.cnf /etc/mysql/conf.d  
ADD https://raw.githubusercontent.com/eventuate-tram/eventuate-tram-
core/release_${VERSION}.RELEASE/mysql/schema.sql /docker-entrypoint-initdb.d  
RUN chmod +r /docker-entrypoint-initdb.d/schema.sql  

