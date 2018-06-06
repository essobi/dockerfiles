FROM jboss/keycloak-ha-postgres:3.1.0.Final  
  
MAINTAINER Dag Viggo Lokoeen <dag.viggo@lokoen.org>  
  
USER root  
#RUN mkdir /config-files  
  
ADD run.sh /opt/jboss/  
ADD vimond-transform.xsl /opt/jboss/keycloak  
  
ADD https://s3.eu-central-1.amazonaws.com/vimondops-files/vimond-keycloak-
spi/vimond-spi-1.0-SNAPSHOT.jar /opt/jboss/keycloak/standalone/deployments/  
RUN chmod a+x /opt/jboss/run.sh \  
&& chown jboss:jboss /opt/jboss/keycloak/standalone/deployments/vimond-
spi-1.0-SNAPSHOT.jar \  
&& java -jar /usr/share/java/saxon.jar
-s:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml
-xsl:/opt/jboss/keycloak/vimond-transform.xsl
-o:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml  
  
USER jboss  
ENTRYPOINT [ "/opt/jboss/run.sh" ]  
  

