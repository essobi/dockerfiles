FROM jboss/wildfly  
MAINTAINER atze.devries@naturalis.nl  
  
ENV API_URL=http://localhost:5000/v0 USERNAME=stargazer PASSWORD=password
LISTEN_IP=127.0.0.1 PORT=8080 PORT_SSL=8443  
  
ADD stargazer-web.war /opt/jboss/wildfly/standalone/deployments/  
ADD bootstrap.sh /bootstrap.sh  
EXPOSE $PORT  
EXPOSE $PORT_SSL  
CMD sh /bootstrap.sh  
  

