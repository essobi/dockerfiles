FROM microsoft/mssql-server-linux:2017-CU2  
  
ENV ACCEPT_EULA=y  
ENV MSSQL_PID=Express  
  
WORKDIR /tmp  
  
# Sqlserver VM  
WORKDIR /sqlserver  
  
COPY entrypoint.sh /  
RUN chmod u+x /entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
EXPOSE 1433  

