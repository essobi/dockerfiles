FROM jboss/keycloak:2.3.0.Final  
MAINTAINER carlosthe19916@gmail.com  
  
ARG KEYCLOAK_ADMIN_USER=admin  
ARG KEYCLOAK_ADMIN_PASWORD=password  
ARG KEYCLOAK_IMPORT_REALM  
ENV KEYCLOAK_IMPORT_REALM ${KEYCLOAK_IMPORT_REALM:-openfact-realm.json}  
  
RUN /opt/jboss/keycloak/bin/add-user.sh -u ${KEYCLOAK_ADMIN_USER} -p
${KEYCLOAK_ADMIN_PASWORD}  
  
ADD ${KEYCLOAK_IMPORT_REALM} /opt/jboss/keycloak/  
  
ENTRYPOINT [ "/opt/jboss/docker-entrypoint.sh" ]  
  
CMD ["-b", "0.0.0.0",
"-Dkeycloak.import=/opt/jboss/keycloak/${KEYCLOAK_IMPORT_REALM}"]  

