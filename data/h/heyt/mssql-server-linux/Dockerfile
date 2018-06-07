FROM microsoft/mssql-server-linux:latest  
  
# Default SQL Server TCP/Port.  
EXPOSE 1433  
  
# Environment variables  
ENV ACCEPT_EULA=Y  
ENV MSSQL_SA_PASSWORD=  
ENV MSSQL_PID=Express  
ENV MSSQL_LCID=1033  
ENV MSSQL_COLLATION=Turkish_CI_AS  
ENV MSSQL_MEMORY_LIMIT_MB=1024  
ENV MSSQL_BACKUP_DIR=/var/opt/mssql/backup  
ENV MSSQL_DATA_DIR=/var/opt/mssql/data  
ENV MSSQL_LOG_DIR=/var/opt/mssql/data  
ENV MSSQL_DUMP_DIR=/var/opt/mssql/dump  
  
# Data Volume  
VOLUME [ "/var/opt/mssql" ]  
  
# Run SQL Server process.  
CMD /opt/mssql/bin/sqlservr

