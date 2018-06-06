FROM jboss/keycloak-postgres:latest  
MAINTAINER Clint Eastwool <clint.eastwool@gmail.com>  
  
# slightly modified from https://github.com/jboss-
dockerfiles/keycloak/tree/master/server-ha-postgres  
# Because keycloak is now already prepared for using infinispan etc, we just
adjust the settings  
# for using a (haproxy) reverse proxy:  
# http://keycloak.github.io/docs/userguide/keycloak-server/html/server-
installation.html#ssl_modes  
ADD update-standalone-ha.xsl /opt/jboss/keycloak/  
RUN java -jar /usr/share/java/saxon.jar
-s:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml
-xsl:/opt/jboss/keycloak/update-standalone-ha.xsl
-o:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml; rm
/opt/jboss/keycloak/update-standalone-ha.xsl  
  
ADD start.sh /opt/jboss/keycloak/bin/  
ADD start_with_export.sh /opt/jboss/keycloak/bin/  
ADD start_with_import.sh /opt/jboss/keycloak/bin/  
  
# use import.json, previously obtained from a keycloak server, for initial
realm(s)  
ADD import.json /opt/jboss/keycloak/  
  
USER root  
RUN chmod 755 /opt/jboss/keycloak/bin/start*.sh; chown jboss:jboss
/opt/jboss/keycloak/bin/start*.sh  
USER jboss  
  
CMD ["/opt/jboss/keycloak/bin/start.sh"]

