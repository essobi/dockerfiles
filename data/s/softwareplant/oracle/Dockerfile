FROM sath89/oracle-12c  
  
ADD init-empty.sql /docker-entrypoint-initdb.d/init.sql  
ADD jira7.dmp /docker-entrypoint-initdb.d/jira7.dmp  
ADD entrypoint.sh /entrypoint.sh  
  
RUN chmod a+x /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh

