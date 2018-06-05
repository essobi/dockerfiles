FROM tomcat:8-jre8  
MAINTAINER Jean Pommier <jean.pommier@pi-geosolutions.fr>  
  
ENV BUILD_DEPS='curl zip' \  
AGGREGATE_URL='http://depots.pigeosolutions.fr/WARs/odkaggregate/ODKAggregate-1.5.0.war'
\  
DBCONNECTOR_VERSION='42.0.0'  
RUN apt-get update \  
&& apt-get install -y ${BUILD_DEPS} \--no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*; exit 0  
  
RUN curl -OL
https://jdbc.postgresql.org/download/postgresql-${DBCONNECTOR_VERSION}.jar \  
&& mv postgresql-${DBCONNECTOR_VERSION}.jar ${CATALINA_HOME}/lib/  
  
RUN curl -L ${AGGREGATE_URL} \--output /ODKAggregate.war  
  
#Sets defaults env vars  
ENV DB_HOSTNAME='localhost' \  
DB_PORT=5432 \  
ODK_PORT='8080' \  
ODK_PORT_SECURE='8443' \  
ODK_HOSTNAME='localhost' \  
ODK_ADMIN_USER='' \  
ODK_ADMIN_USERNAME='jpommier' \  
ODK_AUTH_REALM='Padre ODK Aggregate' \  
ODK_CHANNELTYPE='REQUIRES_INSECURE_CHANNEL'  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE ${ODK_PORT}  
ENTRYPOINT ["/run.sh"]  

