# Inspired by computersciencehouse/keycloak  
FROM jboss/keycloak-mysql:latest  
MAINTAINER Ajeeth Samuel (ajeeth.samuel@gmail.com)  
  
# Copy XSL patches into container  
ADD changeProxy.xsl /opt/jboss/keycloak/  
# Patch configuration for reverse proxy support  
RUN java -jar /usr/share/java/saxon.jar
-s:/opt/jboss/keycloak/standalone/configuration/standalone.xml \  
-xsl:/opt/jboss/keycloak/changeProxy.xsl -o:/opt/jboss/keycloak/standalone/configuration/standalone.xml && \  
java -jar /usr/share/java/saxon.jar
-s:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml \  
-xsl:/opt/jboss/keycloak/changeProxy.xsl -o:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml && \  
rm /opt/jboss/keycloak/changeProxy.xsl  
  
# Set permissions on the Wildfly standalone directory for OpenShift
deployments  
#RUN chmod -R og+rwx /opt/jboss/keycloak/standalone  

