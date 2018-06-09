FROM sath89/oracle-12c  
  
RUN apt update  
RUN apt install -y vim  
  
EXPOSE 1521  
EXPOSE 8080  
ADD data /docker-entrypoint-initdb.d  

