FROM ubuntu:latest  
  
RUN apt-get update -y  
RUN apt-get install postgresql-client-9.5 wget curl -y  
  
RUN wget
https://github.com/mattes/migrate/releases/download/v3.0.1/migrate.linux-
amd64.tar.gz  
RUN tar -xvf migrate.linux-amd64.tar.gz  
RUN mv migrate.linux-amd64 migrate  
RUN chmod a+x migrate && mv migrate /usr/bin  
  
ENTRYPOINT ["/usr/bin/migrate"]  

