FROM microsoft/mssql-server-linux  
  
ARG MSSQL_DATABASE=app  
ENV MSSQL_DATABASE=$MSSQL_DATABASE  
  
ARG MSSQL_PASSWORD=yourStrong(!)Password  
ENV MSSQL_PASSWORD=$MSSQL_PASSWORD  
  
ARG MSSQL_SA_PASSWORD=yourStrong(!)Password  
ENV MSSQL_SA_PASSWORD=$MSSQL_SA_PASSWORD  
  
ARG MSSQL_USER=sa  
ENV MSSQL_USER=$MSSQL_USER  
  
ARG MSSQL_COLLATION=Latin1_General_CI_AI  
ENV MSSQL_COLLATION=$MSSQL_COLLATION  
# args from microsoft/mssql-server-linux  
ARG ACCEPT_EULA=y  
ENV ACCEPT_EULA=$ACCEPT_EULA  
  
ARG MSSQL_PID=Express  
ENV MSSQL_PID=$MSSQL_PID  
  
ENV SA_PASSWORD=$MSSQL_SA_PASSWORD  
  
ENV PATH=$PATH:/opt/mssql/bin:/opt/mssql-tools/bin  
  
WORKDIR /data  
  
COPY ./docker-entrypoint.sh /  
  
CMD ["/docker-entrypoint.sh"]  

