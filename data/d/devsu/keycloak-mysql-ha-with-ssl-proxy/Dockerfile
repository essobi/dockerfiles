FROM devsu/keycloak-mysql-ha:latest  
  
ADD *.xsl /tmp/  
  
RUN xsl-transform /opt/jboss/keycloak/standalone/configuration/standalone-
ha.xml /tmp/enable-ssl-proxy.xsl  

