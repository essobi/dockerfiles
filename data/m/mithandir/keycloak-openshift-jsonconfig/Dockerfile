FROM jboss/keycloak-openshift  
  
ADD docker-entrypoint.sh /opt/jboss/  
  
ENTRYPOINT [ "openshift-entrypoint.sh" ]  
  
CMD ["start-keycloak.sh", "-b", "0.0.0.0"]  

