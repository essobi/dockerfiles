# Base Image  
FROM koyadume/tomcat:8.0.32  
# Maintainer  
MAINTAINER Shailendra Singh <shailendra_01@outlook.com>  
  
WORKDIR $CATALINA_HOME  
  
ENV PISTON_CORE_VERSION 2.3  
ENV TURBINE_VERSION 1.0-rc2  
  
RUN rm conf/server.xml  
  
# Misc  
ADD https://github.com/pistonportal/piston-
releases/releases/download/$PISTON_CORE_VERSION-
turbine-$TURBINE_VERSION/server.xml conf/  
ADD http://central.maven.org/maven2/org/mariadb/jdbc/mariadb-java-
client/1.2.0/mariadb-java-client-1.2.0.jar lib/  
  
# Piston core  
ADD https://github.com/pistonportal/piston-
releases/releases/download/$PISTON_CORE_VERSION-
turbine-$TURBINE_VERSION/piston-core-$PISTON_CORE_VERSION-
turbine-$TURBINE_VERSION.war webapps/piston.war  
  
# Services  
ADD https://github.com/pistonportal/piston-
core/releases/download/$PISTON_CORE_VERSION/piston-
service-$PISTON_CORE_VERSION.war webapps/piston-service.war  
ADD https://github.com/pistonportal/custom-
turbine/releases/download/$TURBINE_VERSION/turbine-
service-$TURBINE_VERSION.war webapps/turbine-service.war  
ADD https://github.com/pistonportal/admin-steam/releases/download/1.3/steam-
service-1.3.war webapps/steam-service.war  
ADD https://github.com/pistonportal/custom-
userManagement/releases/download/1.2/userMgmt-service-1.2.war
webapps/userMgmt-service.war  
  

