# restSQL service image  
FROM tomcat:7-jre7  
  
MAINTAINER Mark Sawers <mark.sawers@restsql.org>  
  
ENV RESTSQL_VERSION=0.8.12  
ENV RESTSQL_SERVICE_WEBAPP_DIR=/usr/local/tomcat/webapps/restsql  
ENV RESTSQL_CONF_DIR=/etc/opt/restsql  
ENV RESTSQL_PROPERTIES=${RESTSQL_CONF_DIR}/restsql.properties  
ENV RESTSQL_SQLRESOURCES_DIR=${RESTSQL_CONF_DIR}/sqlresources  
ENV RESTSQL_LOG_DIR=/var/log/restsql  
  
# Install JDK - we need the jar tool  
RUN apt-get update && apt-get install -y --no-install-recommends \  
openjdk-7-jdk \  
&& rm -rf /var/lib/apt/lists/*  
  
# Create base dirs  
RUN mkdir -vp ${RESTSQL_LOG_DIR}  
RUN mkdir -vp ${RESTSQL_SQLRESOURCES_DIR}  
RUN mkdir -vp ${RESTSQL_SERVICE_WEBAPP_DIR}  
  
# Download and unpack the service webapp  
WORKDIR ${RESTSQL_SERVICE_WEBAPP_DIR}  
RUN curl https://raw.githubusercontent.com/restsql/dist-
archive/master/restsql-${RESTSQL_VERSION}.war > service.war  
RUN jar -xvf service.war  
RUN rm service.war  
  
# Customize default restsql.properties, setting db password, hostname and
sqlresources dir  
RUN sed 's/localhost:3306/mysql:3306/' WEB-
INF/classes/resources/properties/default-restsql.properties >
${RESTSQL_PROPERTIES}  
RUN sed -i'' 's/database.password=root/database.password=sakila/'
${RESTSQL_PROPERTIES}  
RUN sed -i'' 's/sqlresources.dir=\/opt\/restsql\/code\/restsql-
test\/src\/resources\/xml\/sqlresources/sqlresources.dir=\/etc\/opt\/restsql\/sqlresources/'
${RESTSQL_PROPERTIES}  
  
VOLUME "${RESTSQL_LOG_DIR}"  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

