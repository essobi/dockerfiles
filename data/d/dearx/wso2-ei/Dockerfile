FROM dearx/env-java8:latest  
  
ARG VERSION=${VERSION:-6.1.1}  
ARG BUILD=${BUILD:-1497353116245}  
#RUN wget -P /opt https://storage.googleapis.com/esitolo-
apps/wso2/wso2ei-${VERSION}.${BUILD}.zip && \  
# apt-get update && \  
# apt-get install -y zip && \  
# apt-get clean && \  
# unzip /opt/wso2ei-${VERSION}.${BUILD}.zip -d /opt && \  
# rm /opt/wso2ei-${VERSION}.${BUILD}.zip  
#ADD carbon.xml /opt/wso2is-${VERSION}/repository/conf/  
#ADD web.xml /opt/wso2is-${VERSION}/repository/conf/tomcat/carbon/WEB-INF/  
  
#RUN sed -i
'17s|<url>jdbc:h2:./repository/database/WSO2CARBON_DB;DB_CLOSE_ON_EXIT=FALSE;LOCK_TIMEOUT=60000</url>|<url>${DBHOST}:${DBPORT}/${DBNAME}</url>|g'
./master-datasources.xml  
#RUN sed -i '18s|<username>wso2carbon</username>|<username>root</username>|g'
./master-datasources.xml  
#RUN sed -i
'19s|<password>wso2carbon</password>|<password>dearx123#</password>|g'
./master-datasources.xml  
#RUN sed -i
'20s|<driverClassName>org.h2.Driver</driverClassName>|<driverClassName>com.mysql.jdbc.Driver</driverClassName>|g'
./master-datasources.xml  
  
EXPOSE 9443 8243 9763 8280  
WORKDIR /opt/wso2ei-${VERSION}  
ENTRYPOINT ["bin/integrator.sh"]

