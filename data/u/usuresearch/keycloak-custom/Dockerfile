FROM jboss/keycloak-postgres:3.1.0.Final  
  
USER root  
  
ADD docker-entrypoint.sh /opt/jboss/  
RUN chmod a+x /opt/jboss/docker-entrypoint.sh  
  
USER jboss  

