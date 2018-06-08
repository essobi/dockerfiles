FROM rowanto/docker-wheezy-wildfly-java8  
MAINTAINER Rowanto "rowanto@gmail.com"  
# Download and setup mysql driver  
ENV MYSQL_FILENAME mysql-connector-java-5.1.34  
ENV MYSQL_DOWNLOAD
http://dev.mysql.com/get/Downloads/Connector-J/${MYSQL_FILENAME}.tar.gz  
ENV MYSQL_DIRECTORY /opt/wildfly/modules/com/mysql/main  
  
RUN mkdir -p $MYSQL_DIRECTORY  
RUN cd $MYSQL_DIRECTORY && wget $MYSQL_DOWNLOAD && tar -xvf
${MYSQL_FILENAME}.tar.gz && rm ${MYSQL_FILENAME}.tar.gz  
RUN cd $MYSQL_DIRECTORY && mv $MYSQL_FILENAME/* ./ && rm -rf $MYSQL_FILENAME  
  
ADD mysql-module.xml ${MYSQL_DIRECTORY}/module.xml  
  
# Download and setup postgresql driver  
ENV POSTGRESQL_DOWNLOAD
http://jdbc.postgresql.org/download/postgresql-9.3-1102.jdbc41.jar  
ENV POSTGRESQL_DIRECTORY /opt/wildfly/modules/org/postgresql/main  
  
RUN mkdir -p $POSTGRESQL_DIRECTORY  
RUN cd $POSTGRESQL_DIRECTORY && wget $POSTGRESQL_DOWNLOAD  
  
ADD postgresql-module.xml ${POSTGRESQL_DIRECTORY}/module.xml  
  
# Setup standalone.xml  
ADD customized-standalone.xml
/opt/wildfly/standalone/configuration/standalone.xml  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
# Run everything below as the wildfly user  
USER wildfly  
  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]

