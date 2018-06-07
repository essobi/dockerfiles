FROM postgres:9.5  
ARG INIT_FILE=init-scripts/jira-7-update-2018-04-20.sql  
ARG INIT_DIR=/docker-entrypoint-initdb.d  
ENV POSTGRES_INITDB_ARGS="--lc-ctype=C --lc-collate=C --encoding=UTF8"  
RUN apt-get update && apt-get install -y gettext  
  
ADD $INIT_FILE prepare/init.sql  
ADD init-scripts/zzz-update-last.sh /docker-entrypoint-initdb.d/  
  
ADD docker-entrypoint-mod.sh /  
RUN chmod a+x /docker-entrypoint-mod.sh  
ENTRYPOINT ["/docker-entrypoint-mod.sh"]  
CMD ["postgres"]  

