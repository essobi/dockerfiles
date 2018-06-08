#be sure to use the tomcat version with JRE 8  
#also use the alpine version, which is much smaller than most distribution
base images  
FROM tomcat:8.5.9-jre8-alpine  
MAINTAINER Oliver Schwab  
  
# parameters for using jmx  
ENV CATALINA_OPTS "-Dcom.sun.management.jmxremote \  
-Dcom.sun.management.jmxremote.port=1099 \  
-Dcom.sun.management.jmxremote.authenticate=false \  
-Dcom.sun.management.jmxremote.ssl=false"  
# port for remote debugging  
ENV JPDA_ADDRESS 8000  
# add application properties to classpath  
COPY application_local.properties /usr/local/tomcat/lib/  
  
#override users config to add new user (deployer:deployer)  
COPY tomcat-users.xml /usr/local/tomcat/conf/  
COPY manager.xml /usr/local/tomcat/conf/Catalina/localhost/  
  
# start tomcat with remote debugging  
ENTRYPOINT ["catalina.sh", "jpda", "run"]

