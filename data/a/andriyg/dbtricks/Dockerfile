FROM alpine  
  
RUN \  
apk update && \  
apk add git mercurial postgresql-client postgresql mysql-client bash openssh-
client && \  
rm -rvf /var/cache/apk/* && \  
true  
  
ADD importer.py mysqldump_splitsort.py pg_dump_splitsort.py dump_databases.sh
scm.sh /backup/  
  
RUN \  
chmod -Rv guo+rx-w /backup/ && \  
true  
  
ENTRYPOINT ["/bin/bash", "/backup/dump_databases.sh"]  

