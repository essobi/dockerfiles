FROM ubuntu:14.04  
WORKDIR /tmp  
  
RUN apt-get install -y wget  
RUN wget -qO - https://packages.irods.org/irods-signing-key.asc | sudo apt-key
add -  
RUN echo "deb [arch=amd64] https://packages.irods.org/apt/ $(lsb_release -sc)
main" | sudo tee /etc/apt/sources.list.d/renci-irods.list  
RUN apt-get update  
RUN apt-get install -y libc6 sudo libssl1.0.0 libfuse2 libjson-perl perl
python openssl python-psutil python-requests lsof python-jsonschema  
RUN apt-get install -y unixodbc odbc-postgresql postgresql-client super libc6
perl  
RUN apt-get install -y irods-server irods-database-plugin-postgres  
  

