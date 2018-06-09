FROM ubuntu:16.04  
ENV MSSQL_SERVER_HOST mssql  
ENV MSSQL_USERNAME SA  
ENV MSSQL_PASSWORD ""  
ENV MSSQL_PORT 1433  
ENV MSSQL_DATABASE_NAME testdb  
RUN apt-get update && apt-get install -y \  
nodejs-legacy \  
npm  
RUN npm install -g sql-cli  
CMD mssql -u $MSSQL_USERNAME -p $MSSQL_PASSWORD -s $MSSQL_SERVER_HOST -o
$MSSQL_PORT -q "create database $MSSQL_DATABASE_NAME"

