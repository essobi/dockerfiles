FROM postgres:10-alpine  
  
ADD https://raw.githubusercontent.com/MIT-LCP/mimic-
code/master/buildmimic/postgres/postgres_create_tables.sql /docker-entrypoint-
initdb.d/psql/  
ADD https://raw.githubusercontent.com/MIT-LCP/mimic-
code/master/buildmimic/postgres/postgres_add_comments.sql /docker-entrypoint-
initdb.d/psql/  
ADD https://raw.githubusercontent.com/MIT-LCP/mimic-
code/master/buildmimic/postgres/postgres_add_indexes.sql /docker-entrypoint-
initdb.d/psql/  
ADD https://raw.githubusercontent.com/MIT-LCP/mimic-
code/master/buildmimic/postgres/postgres_add_constraints.sql /docker-
entrypoint-initdb.d/psql/  
  
RUN chmod -R a+r /docker-entrypoint-initdb.d/psql/  
  
ADD setup.sh /docker-entrypoint-initdb.d/  

