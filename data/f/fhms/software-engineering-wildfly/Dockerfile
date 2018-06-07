# Wildfly in der finalen Version 10 verwenden  
FROM jboss/wildfly:11.0.0.Final  
  
# Erzeuge Modul-Verzeichnis für MySQL JDBC Treiber  
RUN mkdir -p /opt/jboss/wildfly/modules/system/layers/base/com/sql/mysql/main  
  
# MySQL Treiber in Modul-Verzeichnis schieben  
ADD lib/mysql-connector-java-5.1.38-bin.jar
/opt/jboss/wildfly/modules/system/layers/base/com/sql/mysql/main  
ADD lib/module.xml
/opt/jboss/wildfly/modules/system/layers/base/com/sql/mysql/main  
  
# Vorhandene standalone-full.xml durch die konfigurierte ersetzen  
ADD conf/standalone-full.xml /opt/jboss/wildfly/standalone/configuration  
  
# Hinzufügen der Shell-Skripte  
ADD bin/wildfly-configuration.sh /opt/  
ADD bin/wait-for-it.sh /opt/  
ADD bin/startup.sh /opt/  
ADD bin/deploy.sh /opt/  
  
# Festlegung des Standardwerts für die Umgebungsvariable der MySQL Datenbank  
ENV MYSQL_SERVER_URL=localhost  
  
# Anlegen des Default Administrators  
RUN /opt/jboss/wildfly/bin/add-user.sh -up mgmt-users.properties admin admin
--silent  
  
USER root  
  
# Starten des Servers mithilfe des startup.sh  
CMD ["/bin/bash", "/opt/startup.sh"]  

