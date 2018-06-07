FROM jboss/keycloak-adapter-wildfly:1.1.0.Final  
  
#Agregando module mysql  
RUN mkdir -p
/opt/jboss/wildfly/modules/system/layers/base/com/mysql/jdbc/main; cd
/opt/jboss/wildfly/modules/system/layers/base/com/mysql/jdbc/main && curl -O
http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.18/mysql-
connector-java-5.1.18.jar  
ADD module.xml
/opt/jboss/wildfly/modules/system/layers/base/com/mysql/jdbc/main/  
#Copiando scripts  
ADD customization /opt/jboss/wildfly/customization/  
  
#Cambiando de usuario  
USER root  
  
# Run customization scripts as root  
RUN chmod +x /opt/jboss/wildfly/customization/execute.sh  
RUN /opt/jboss/wildfly/customization/execute.sh  
  
#Modificando datasource  
ADD changeDatabase.xsl /opt/jboss/wildfly/  
RUN java -jar /usr/share/java/saxon.jar
-s:/opt/jboss/wildfly/standalone/configuration/standalone.xml
-xsl:/opt/jboss/wildfly/changeDatabase.xsl
-o:/opt/jboss/wildfly/standalone/configuration/standalone.xml  
  
#Agregando war  
ADD files/wars/ /opt/jboss/wildfly/standalone/deployments/  
#Creando usuario  
RUN chown -R jboss:jboss /opt/jboss/wildfly/  
USER jboss

