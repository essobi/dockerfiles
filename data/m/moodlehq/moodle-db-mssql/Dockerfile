FROM microsoft/mssql-server-linux:2017-GA  
  
RUN apt-get -y update && apt-get install -y netcat  
  
ADD root/ /  
  
EXPOSE 1433  
CMD ["/docker-entrypoint.sh"]  

