FROM mysql:5.7  
  
COPY conf.d/disable_strict_mode.cnf /etc/mysql/conf.d/disable_strict_mode.cnf  
  
RUN apt-get update && apt-get -y install curl && \  
curl -sL "https://raw.githubusercontent.com/NateV/Expungement-
Generator/master/migrations/1%20-%20eg_schema.sql" > /docker-entrypoint-
initdb.d/1_eg_schema.sql && \  
curl -sL "https://raw.githubusercontent.com/NateV/Expungement-
Generator/master/migrations/2%20-%20cpcms_aopc_summary.sql" > /docker-
entrypoint-initdb.d/2_cpcms_aopc_summary.sql && \  
curl -sL "https://raw.githubusercontent.com/NateV/Expungement-
Generator/master/migrations/3%20-%20database_initial_data.sql" > /docker-
entrypoint-initdb.d/3_database_initial_data.sql && \  
curl -sL "https://raw.githubusercontent.com/NateV/Expungement-
Generator/master/migrations/4%20-%20add_saveDatabase_to_programtable.sql" >
/docker-entrypoint-initdb.d/4_add_saveDatabase_to_programtable.sql  

