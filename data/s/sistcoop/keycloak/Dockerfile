FROM jboss/keycloak:1.1.0.Final  
#load sistcoop reaml from .json file  
RUN echo 'JAVA_OPTS="$JAVA_OPTS
-Dkeycloak.import=/opt/jboss/keycloak/sistcooprealm.json"' >>
/opt/jboss/keycloak/bin/standalone.conf  
ADD files/sistcooprealm.json /opt/jboss/keycloak/sistcooprealm.json

