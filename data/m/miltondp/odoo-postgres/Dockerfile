FROM postgres:9.4  
  
RUN localedef -i es_AR -c -f UTF-8 -A /usr/share/locale/locale.alias
es_AR.UTF-8  
ENV LANG es_AR.utf8  
  
COPY init-database.sql /docker-entrypoint-initdb.d/  
  

