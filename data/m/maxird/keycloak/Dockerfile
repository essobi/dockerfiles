FROM maxird/java:7-8  
RUN export VERSION=3.4.3.Final && \  
cd /opt && \  
wget -q
"http://downloads.jboss.org/keycloak/${VERSION}/keycloak-${VERSION}.tar.gz" -O
- | tar -xvz && \  
ln -s keycloak-${VERSION} keycloak && \  
echo 'export PATH=$PATH:/opt/keycloak/bin' > /etc/profile.d/keycloak.sh && \  
echo '[ { \  
"realm" : "master", \  
"users" : [ {"username" : "admin", "enabled" : true, \  
"credentials" : [ {"type" : "password", "value" : "admin"} ], \  
"realmRoles" : [ "admin" ]} ]} ]' >
/opt/keycloak/standalone/configuration/keycloak-add-user.json && \  
mkdir -p /opt/keycloak/standalone/data && \  
mkdir -p /opt/keycloak/standalone/log && \  
mkdir -p /opt/keycloak/standalone/tmp && \  
echo 'done'  
  
EXPOSE 8080  
VOLUME /opt/keycloak/standalone/data  
VOLUME /opt/keycloak/standalone/log  
VOLUME /opt/keycloak/standalone/tmp  
  
CMD ["/opt/keycloak/bin/standalone.sh", "-Djboss.bind.address=0.0.0.0"]  

