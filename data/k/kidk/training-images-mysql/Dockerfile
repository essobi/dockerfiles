FROM mysql:5.7  
ENV MYSQL_ROOT_PASSWORD=secret  
ENV MYSQL_DATABASE=my_db  
  
COPY mysqld.cnf /etc/mysql/mysql.conf.d/  
  
MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>  
  
LABEL
com.coscale.monitoring='[{"PluginType":"MYSQL","Configuration":{"TYPE":["PERFORMANCE
SCHEMA"],"QUERY
STATS":["true"],"HOSTNAME":["localhost"],"PORT":["3306"],"USERNAME":["root"],"PASSWORD":["secret"],"DEFAULT
DATABASE":["my_db"],"QUERY CHECK":["SELECT count(*) FROM words"]}}]'  

