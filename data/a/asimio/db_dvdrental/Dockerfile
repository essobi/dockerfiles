FROM asimio/postgres:latest  
MAINTAINER Orlando L Otero ootero@asimio.net,
https://bitbucket.org/asimio/postgres  
# Manually build using command: docker build -t asimio/db_dvdrental:latest .  
VOLUME /tmp  
RUN mkdir -p /tmp/data/db_dvdrental  
  
ENV DB_NAME db_dvdrental  
ENV DB_USER user_dvdrental  
ENV DB_PASSWD changeit  
  
COPY sql/dvdrental.tar /tmp/data/db_dvdrental/dvdrental.tar  
# Seems scripts will get executed in alphabetical-sorted order, db-init.sh
needs to be executed first  
ADD scripts/db-restore.sh /docker-entrypoint-initdb.d/  
RUN chmod 755 /docker-entrypoint-initdb.d/db-restore.sh  
  
# Run as:  
# docker run -d asimio/db_dvdrental:latest  
# docker run -d -e DB_PASSWD=changeit asimio/db_dvdrental  
# docker run -d -p 5432:5432 -e DB_NAME=db_dvdrental -e DB_USER=user_dvdrental
-e DB_PASSWD=changeit asimio/db_dvdrental:latest  

