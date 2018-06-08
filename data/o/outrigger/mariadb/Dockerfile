FROM outrigger/servicebase  
  
VOLUME ["/var/lib/mysql"]  
  
COPY root /  
  
RUN yum -y install MariaDB-server MariaDB-client  
  
# Set the default admin password  
ENV MYSQL_PASS admin  
  
# Set various default configuration  
ENV MYSQL_EXPIRE_LOGS_DAYS 10  
ENV MYSQL_MAX_ALLOWED_PACKET 16M  
ENV MYSQL_MAX_CONNECTIONS 10  
ENV MYSQL_QUERY_CACHE_LIMIT 1M  
ENV MYSQL_QUERY_CACHE_SIZE 16M  
  
# Slow query log settings  
# Set MYSQL_SLOW_QUERY_LOG to 1 to turn on slow query logging  
ENV MYSQL_SLOW_QUERY_LOG 0  
ENV MYSQL_LONG_QUERY_TIME 10  
ENV MYSQL_LOG_QUERY_NO_INDEX 0  
EXPOSE 3306  

