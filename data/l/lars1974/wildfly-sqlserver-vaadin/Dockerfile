FROM jboss/wildfly:9.0.0.Final  
  
ADD com/microsoft/sqlserver/jdbc/main/module.xml
/opt/jboss/wildfly/modules/com/microsoft/sqlserver/jdbc/main/  
ADD com/microsoft/sqlserver/jdbc/main/sqljdbc4.jar
/opt/jboss/wildfly/modules/com/microsoft/sqlserver/jdbc/main/  
  
  
ADD com/vaadin/main/module.xml /opt/jboss/wildfly/modules/com/vaadin/main/  
ADD com/vaadin/main/vaadin-client-7.5.4.jar
/opt/jboss/wildfly/modules/com/vaadin/main/  
ADD com/vaadin/main/vaadin-client-compiled-7.5.4.jar
/opt/jboss/wildfly/modules/com/vaadin/main/  
ADD com/vaadin/main/vaadin-server-7.5.4.jar
/opt/jboss/wildfly/modules/com/vaadin/main/  
ADD com/vaadin/main/vaadin-sass-compiler-0.9.12.jar
/opt/jboss/wildfly/modules/com/vaadin/main/  
ADD com/vaadin/main/vaadin-shared-7.5.4.jar
/opt/jboss/wildfly/modules/com/vaadin/main/  
ADD com/vaadin/main/vaadin-themes-7.5.4.jar
/opt/jboss/wildfly/modules/com/vaadin/main/  
  
ADD com/vaadin/main/flute-1.3.0.gg2.jar
/opt/jboss/wildfly/modules/com/vaadin/main/  
ADD com/vaadin/main/guava-16.0.1.vaadin1.jar
/opt/jboss/wildfly/modules/com/vaadin/main/  
ADD com/vaadin/main/jsoup-1.8.1.jar
/opt/jboss/wildfly/modules/com/vaadin/main/  
ADD com/vaadin/main/sac-1.3.jar /opt/jboss/wildfly/modules/com/vaadin/main/  
ADD com/vaadin/main/streamhtmlparser-jsilver-0.0.10.vaadin1.jar
/opt/jboss/wildfly/modules/com/vaadin/main/  
  
EXPOSE 8080 9990

