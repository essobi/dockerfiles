FROM postgres:10.0  
#RUN chown -R postgres:root /usr/share/postgresql/9.6/tsearch_data \  
# && chmod -R 0770 /usr/share/postgresql/9.6/tsearch_data  
RUN apt-get update \  
&& apt-get install -y curl  
  
ADD ru_ru.affix /usr/share/postgresql/10/tsearch_data/ru_ru.affix  
ADD ru_ru.dict /usr/share/postgresql/10/tsearch_data/ru_ru.dict  
RUN chown -R postgres:root /usr/share/postgresql/10/tsearch_data \  
&& chmod -R 0770 /usr/share/postgresql/10/tsearch_data  
ADD postgres-install.sh /docker-entrypoint-initdb.d/postgres-install.sh  
ADD postgres-fulltextsearch.sh /docker-entrypoint-initdb.d/postgres-
fulltextsearch.sh  
ADD postgres-fulltextsearch.sql /docker-entrypoint-initdb.d/postgres-
fulltextsearch.sql  

