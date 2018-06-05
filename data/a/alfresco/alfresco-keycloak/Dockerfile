FROM jboss/keycloak:3.4.0.Final  
MAINTAINER https://gitter.im/Alfresco/platform-services  
  
RUN /opt/jboss/keycloak/bin/add-user.sh -u admin -p admin  
RUN /opt/jboss/keycloak/bin/add-user-keycloak.sh -r master -u admin -p admin  
  
ADD springboot-realm.json /opt/jboss/keycloak/  
  
ENTRYPOINT [ "/opt/jboss/docker-entrypoint.sh" ]  
  
ENV PORT_OFFSET 100  
EXPOSE 8180 30081  
CMD ["-b", "0.0.0.0", "-Dkeycloak.import=/opt/jboss/keycloak/springboot-
realm.json -Djboss.socket.binding.port-offset=${env.PORT_OFFSET}"]  

