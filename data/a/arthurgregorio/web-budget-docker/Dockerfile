FROM jboss/wildfly:10.1.0.Final  
  
LABEL application=webBudget-v2.3.1  
LABEL maintainer=arthurshakal@gmail.com  
  
USER root  
  
RUN \  
yum update -y && \  
yum install -y epel-release mariadb-server hostname net-tools pwgen wget && \  
yum clean all && \  
rm -rf /var/lib/mysql/*  
  
RUN mkdir -p /opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main  
RUN wget https://downloads.mariadb.com/Connectors/java/connector-
java-2.2.3/mariadb-java-client-2.2.3.jar -O
/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/mariadb-java-
client-2.2.3.jar  
  
COPY container-files/wildfly/standalone.xml
/opt/jboss/wildfly/standalone/configuration/standalone.xml  
COPY container-files/wildfly/module.xml
/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/  
  
RUN /opt/jboss/wildfly/bin/add-user.sh admin admin --silent  
  
COPY container-files/mariadb /  
COPY container-files/wildfly/run-wildfly.sh /  
COPY container-files/wildfly/wb-v2.3.1.war
/opt/jboss/wildfly/standalone/deployments/  
  
EXPOSE 3306 8443 9993  
WORKDIR "/"  
  
ENV MARIADB_PASS 'sa_webbudget'  
RUN chmod +x /run-maria.sh  
RUN chmod +x /run-wildfly.sh  
  
ENTRYPOINT ./run-maria.sh && ./run-wildfly.sh  

