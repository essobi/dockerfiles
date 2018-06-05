FROM jboss/base-jdk:8  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 8.2.0.Final  
  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME && curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx && mv $HOME/wildfly-$WILDFLY_VERSION $HOME/wildfly  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]  
  
### -- Instalação do modulo do postgres no wildfly -- ###  
ENV POSTGRES_JDBC_VESION 9.3-1102-jdbc41  
  
RUN cd ${JBOSS_HOME}/modules/system/layers/base/org \  
&& mkdir -p postgresql/main && cd postgresql/main \  
&& curl -O
http://central.maven.org/maven2/org/postgresql/postgresql/${POSTGRES_JDBC_VESION}/postgresql-${POSTGRES_JDBC_VESION}.jar  
  
ADD module.xml ${JBOSS_HOME}/modules/system/layers/base/org/postgresql/main/  
  
### -- Preparação do build da plataform -- ###  
ADD standalone.conf ${JBOSS_HOME}/bin/  
ADD standalone.xml ${JBOSS_HOME}/standalone/configuration/  
ADD dist/plataforma-ear.ear ${JBOSS_HOME}/standalone/deployments/  
  
### -- Restaurar autoridade de todos arquivos do wildfly para o usuário jboss
-- ###  
USER root  
RUN chown jboss:jboss -R ${JBOSS_HOME}  
USER jboss  

