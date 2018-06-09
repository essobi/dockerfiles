#Build MySQL server  
FROM mysql  
# Build arguments  
#Update  
RUN apt-get update && apt-get install -y \  
less \  
vim  
  
#add sql skript  
ADD ./build.sql /docker-entrypoint-initdb.d/  
  
# Work here  
#RUN mkdir /build  
WORKDIR /  
  
# Environment required by build script  
ENV MYSQL_ROOT_PASSWORD=Password1  

