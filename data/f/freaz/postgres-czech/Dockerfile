FROM postgres:latest  
  
RUN localedef -i cs_CZ -c -f UTF-8 -A /usr/share/locale/locale.alias
cs_CZ.UTF-8  
ENV LANG cs_CZ.utf8  
  
ADD http://www.pgsql.cz/data/czech.tar.gz /root/  
RUN cd /root && tar xvzf czech.tar.gz && \  
cp fulltext_dicts/* $(find / -iname "tsearch_data") && \  
rm -rf fulltext_dicts czech.tar.gz  
  
COPY ./init-scripts/* /docker-entrypoint-initdb.d/  

