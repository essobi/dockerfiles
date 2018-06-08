FROM jboss/keycloak:latest  
  
# Temporarily elevate permissions  
USER root  
  
# Copy customizations into container  
ADD customization /opt/jboss/keycloak/customization  
  
ENV TRUSTSTORE_DISABLED true  
ENV TRUSTSTORE trust.jks  
ENV TRUSTSTORE_PASSWORD changeit  
ENV HOSTNAME_VERIFICATION_POLICY WILDCARD  
  
# Execute customization script  
RUN cd /opt/jboss/keycloak && \  
/opt/jboss/keycloak/customization/execute.sh && \  
chown -R jboss: /opt/jboss  
  
USER jboss  
  

