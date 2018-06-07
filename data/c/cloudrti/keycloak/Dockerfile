FROM jboss/keycloak:2.4.0.Final  
  
ADD keycloak-entrypoint.sh keycloak-entrypoint.sh  
ADD mongo-configure.cli /opt/jboss/keycloak/  
ENV JAVA_OPTS $JAVA_OPTS -javaagent:/opt/jboss/newrelic/newrelic.jar  
  
RUN curl -O https://download.newrelic.com/newrelic/java-agent/newrelic-
agent/3.34.0/newrelic-java.zip &&\  
unzip newrelic-java.zip && rm newrelic-java.zip &&\  
/opt/jboss/keycloak/bin/jboss-cli.sh \--file=/opt/jboss/keycloak/mongo-
configure.cli &&\  
rm -rf /opt/jboss/keycloak/standalone/configuration/standalone_xml_history  
  
ENTRYPOINT [ "/opt/jboss/keycloak-entrypoint.sh" ]  
  
CMD ["-b", "0.0.0.0"]

