FROM microsoft/mssql-server-linux:2017-GA  
MAINTAINER Shane Genschaw  
  
ENV ENVIRONMENT_REFRESH 2017-10-09  
EXPOSE 1433  
RUN ln -s /opt/mssql-tools/bin/sqlcmd /usr/local/bin/sqlcmd \  
&& ln -s /opt/mssql-tools/bin/bcp /usr/local/bin/bcp \  
&& mkdir -p /docker-entrypoint-initdb.d  
  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY docker-entrypoint-initdb.sh /usr/local/bin/  
COPY initdb.d /initdb.d  
  
WORKDIR /initdb.d  
RUN ls -1 *.sql | sort | while read fn ; do cat "$fn" >> /docker-entrypoint-
initdb.d/initdb.sql; done  
ENTRYPOINT ["docker-entrypoint.sh"]

