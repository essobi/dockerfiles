FROM ubuntu:14.04  
COPY mysql-apt-config_0.3.2-1ubuntu14.04_all.deb /tmp/mysql-apt-
config_0.3.2-1ubuntu14.04_all.deb  
  
RUN dpkg -i /tmp/mysql-apt-config_0.3.2-1ubuntu14.04_all.deb  
  
RUN apt-get update && apt-get install mysql-workbench -y  
  
ENTRYPOINT ["mysql-workbench"]  

