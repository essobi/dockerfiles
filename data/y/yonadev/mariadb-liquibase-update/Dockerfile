FROM openjdk:8  
WORKDIR /opt/mariadb  
  
# Create dirs  
RUN mkdir -p /opt/liquibase &&\  
mkdir -p /opt/jdbc_drivers &&\  
mkdir -p /home/rundir &&\  
mkdir /scripts  
  
# Add liquibase  
ADD http://repo1.maven.org/maven2/org/liquibase/liquibase-
core/3.5.3/liquibase-core-3.5.3-bin.tar.gz /opt/liquibase/liquibase-core-
bin.tar.gz  
WORKDIR /opt/liquibase  
RUN tar -xzf liquibase-core-bin.tar.gz &&\  
rm liquibase-core-bin.tar.gz &&\  
chmod +x /opt/liquibase/liquibase &&\  
ln -s /opt/liquibase/liquibase /usr/local/bin/  
  
WORKDIR /  
  
# Add MariaDB JDBC driver  
ENV DRIVER_VERSION 1.5.5  
ENV DRIVER_JAR mariadb-java-client-${DRIVER_VERSION}.jar  
ADD http://central.maven.org/maven2/org/mariadb/jdbc/mariadb-java-
client/${DRIVER_VERSION}/${DRIVER_JAR} /opt/jdbc_drivers/${DRIVER_JAR}  
RUN chmod 644 /opt/jdbc_drivers/${DRIVER_JAR}  
  
# Add update script  
COPY update.sh /scripts/  
RUN chmod +x /scripts/update.sh  
  
# Prepare for running container  
WORKDIR /home/rundir  
CMD ["/scripts/update.sh"]  

