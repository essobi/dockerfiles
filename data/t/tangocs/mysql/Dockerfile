FROM mysql:5.5  
MAINTAINER TANGO Controls Team <tango@esrf.fr>  
  
ENV MYSQL_DATABASE=tango  
ENV MYSQL_USER=tango  
ENV MYSQL_PASSWORD=tango  
  
ADD scripts/create_db_tables.sql \  
scripts/stored_proc.sql \  
/scripts/  
  
ADD scripts/a_print_env.sh \  
scripts/b_populate_tango_db.sql \  
/docker-entrypoint-initdb.d/  
  

