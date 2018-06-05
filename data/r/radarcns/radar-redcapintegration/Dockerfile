  
FROM tomcat:8.5.20-jre8  
  
# Create a radar configuration directory  
RUN mkdir $CATALINA_HOME/conf/radar  
  
# Add the configuration file  
# COPY ./radar.yml $CATALINA_HOME/conf/radar/radar.yml  
# ADD ./radar.yml $CATALINA_HOME/conf/radar/radar.yml  
RUN rm -rf /usr/local/tomcat/webapps/*  
  
# Copy the WAR file to tomcat webapps for deployment  
ADD https://github.com/RADAR-CNS/RADAR-
RedcapIntegration/releases/download/v0.1-beta.2/redcap-2.0-SNAPSHOT.war
$CATALINA_HOME/webapps/redcap.war  
#ADD ./build/libs/redcap-1.0-SNAPSHOT.war $CATALINA_HOME/webapps/redcap.war  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

