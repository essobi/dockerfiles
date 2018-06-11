FROM node:7  
WORKDIR /home/app  
  
# Install SQL Server  
RUN echo "mariadb-server-10.0 mysql-server/root_password password password" |
debconf-set-selections  
RUN echo "mariadb-server-10.0 mysql-server/root_password_again password
password" | debconf-set-selections  
RUN apt-get update && apt-get install -y curl mariadb-server-10.0 && apt-get
clean  
  

