FROM postgres:9.6  
MAINTAINER chaya  
  
COPY flyway /flyway  
RUN chmod -R 755 /flyway  
  
RUN apt-get update && apt-get install -y git-core  
  
COPY shell/install.sh /docker-entrypoint-initdb.d  
COPY shell/configure-as-master.sh /opt  
COPY shell/configure-as-slave.sh /opt  
COPY shell/configure-security.sh /opt  
COPY shell/database-install.sh /opt  
COPY shell/docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint-initdb.d/install.sh /opt/configure-as-
master.sh /opt/configure-as-slave.sh /opt/configure-security.sh /opt/database-
install.sh docker-entrypoint.sh

