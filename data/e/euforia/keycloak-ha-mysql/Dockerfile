#  
# Keyclaok HA setup using MySQL and TCP for clustering.  
#  
  
FROM jboss/keycloak-mysql  
  
COPY ./standalone-ha.xml /opt/jboss/keycloak/standalone/configuration/docker-
standalone-ha.xml  
  
# 7600 - TCP cluster port  
# 8080 - Web service  
# 57600 - Failure detection  
# 57601 - Failure detection client  
EXPOSE 7600 8080 57600 57601  
# When supplying extra args, these must be specified as well  
CMD [ "-b", "0.0.0.0", "--server-config", "docker-standalone-ha.xml" ]

