FROM mariadb:10  
MAINTAINER Nikolay Didenko "nd@info74.ru"  
# Copy build script  
COPY build-me.sh /opt/  
  
# Copy preconfigure script  
COPY 10-pinba-db-init.sh /docker-entrypoint-initdb.d/  
  
# RUN build script (build and install pinba-server)  
RUN cd /opt && ./build-me.sh  
  
# expose extraport for pinba  
EXPOSE 30002  

