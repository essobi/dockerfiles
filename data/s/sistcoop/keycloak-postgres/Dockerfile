FROM jboss/keycloak:1.1.0.Final  
  
ADD changeDatabase.xsl /opt/jboss/keycloak/  
RUN java -jar /usr/share/java/saxon.jar
-s:/opt/jboss/keycloak/standalone/configuration/standalone.xml
-xsl:/opt/jboss/keycloak/changeDatabase.xsl
-o:/opt/jboss/keycloak/standalone/configuration/standalone.xml  
RUN mkdir -p
/opt/jboss/keycloak/modules/system/layers/base/org/postgresql/jdbc/main; cd
/opt/jboss/keycloak/modules/system/layers/base/org/postgresql/jdbc/main; curl
-O
http://central.maven.org/maven2/org/postgresql/postgresql/9.3-1102-jdbc3/postgresql-9.3-1102-jdbc3.jar  
ADD module.xml
/opt/jboss/keycloak/modules/system/layers/base/org/postgresql/jdbc/main/  
  
#load sistcoop reaml from .json file  
RUN echo 'JAVA_OPTS="$JAVA_OPTS
-Dkeycloak.import=/opt/jboss/keycloak/sistcooprealm.json"' >>
/opt/jboss/keycloak/bin/standalone.conf  
ADD files/sistcooprealm.json /opt/jboss/keycloak/sistcooprealm.json

