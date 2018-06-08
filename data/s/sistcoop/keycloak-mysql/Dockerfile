FROM jboss/keycloak:1.1.0.Final  
  
ADD changeDatabase.xsl /opt/jboss/keycloak/  
RUN java -jar /usr/share/java/saxon.jar
-s:/opt/jboss/keycloak/standalone/configuration/standalone.xml
-xsl:/opt/jboss/keycloak/changeDatabase.xsl
-o:/opt/jboss/keycloak/standalone/configuration/standalone.xml  
RUN mkdir -p
/opt/jboss/keycloak/modules/system/layers/base/com/mysql/jdbc/main; cd
/opt/jboss/keycloak/modules/system/layers/base/com/mysql/jdbc/main && curl -O
http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.18/mysql-
connector-java-5.1.18.jar  
ADD module.xml
/opt/jboss/keycloak/modules/system/layers/base/com/mysql/jdbc/main/  
  
#load sistcoop reaml from .json file  
RUN echo 'JAVA_OPTS="$JAVA_OPTS
-Dkeycloak.import=/opt/jboss/keycloak/sistcooprealm.json"' >>
/opt/jboss/keycloak/bin/standalone.conf  
ADD files/sistcooprealm.json /opt/jboss/keycloak/sistcooprealm.json

