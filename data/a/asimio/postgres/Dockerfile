FROM postgres:9.5  
MAINTAINER Orlando L Otero ootero@asimio.net,
https://bitbucket.org/asimio/postgres  
# Manually build using command: docker build -t asimio/postgres:latest .  
# Update Ubuntu  
RUN \  
bash -c 'apt-mark hold postgresql-common' && \  
bash -c 'apt-get -qq update && apt-get -y upgrade && apt-get -y autoclean &&
apt-get -y autoremove' && \  
bash -c 'DEBIAN_FRONTEND=noninteractive apt-get install -y curl wget tar'  
  
ENV DB_NAME dbName  
ENV DB_USER dbUser  
ENV DB_PASSWD dbPassword  
  
RUN mkdir -p /docker-entrypoint-initdb.d  
ADD scripts/db-init.sh /docker-entrypoint-initdb.d/  
RUN chmod 755 /docker-entrypoint-initdb.d/db-init.sh  
  
# Run as:  
# docker run -d -e DB_NAME=db_dvdrental -e DB_USER=user_dvdrental -e
DB_PASSWD=changeit asimio/postgres:latest  

