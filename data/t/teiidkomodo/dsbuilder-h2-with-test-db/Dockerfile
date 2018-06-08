#  
# Docker image configuration for dsbuilder configured with a locally available  
# mysql database and driver added to wildfly.  
#  
FROM teiidkomodo/dsbuilder:vanilla-1.0  
MAINTAINER Teiid-Komodo Community <http://teiiddesigner.jboss.org>  
  
#  
# Env variables  
#  
ENV BIN_DIR /usr/local/bin  
ENV JBOSS_HOME /opt/jboss/wildfly  
ENV H2_DB_VERSION 2014-04-05  
ENV H2_DATA /opt/h2-data  
ENV DB_NAME customers  
  
#  
# Change to root user  
#  
USER root  
  
# set-up h2  
ADD http://www.h2database.com/h2-${H2_DB_VERSION}.zip .  
RUN unzip h2-${H2_DB_VERSION}.zip -d ./  
RUN mkdir -p ${H2_DATA}  
RUN rm h2-${H2_DB_VERSION}.zip  
  
#  
# Add the h2 database scripts and import  
#  
ADD schema/customer-schema.sql ./  
RUN java -cp h2/bin/h2*.jar \  
org.h2.tools.RunScript \  
-url jdbc:h2:${H2_DATA}/${DB_NAME} \  
-user sa \  
-script customer-schema.sql  
  
EXPOSE 8081 1521  
#  
# Copy wildfly exec script and set permissions  
#  
COPY wildfly-exec.sh ${BIN_DIR}/  
RUN chmod +x ${BIN_DIR}/wildfly-exec.sh  
  
#  
# Add datasource configuration files  
#  
ADD datasources/* ./  
  
#  
# Start wildfly and configure the data sources  
#  
RUN chmod +x ./configure-wildfly-datasources.sh && ./configure-wildfly-
datasources.sh  
  
#  
# Copy h2 exec script and set permissions  
#  
COPY h2-exec.sh ${BIN_DIR}/  
RUN chmod +x ${BIN_DIR}/h2-exec.sh  
  
##  
## The default cmd for this container  
##  
CMD ["/bin/sh", "-c", "${BIN_DIR}/h2-exec.sh ${H2_DATA} && ${BIN_DIR}/wildfly-
exec.sh"]  

