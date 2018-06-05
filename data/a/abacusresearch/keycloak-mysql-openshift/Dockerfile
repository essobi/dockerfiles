FROM jboss/keycloak-mysql  
  
COPY changeProxy.xsl /opt/jboss/keycloak/  
COPY changeLogger.xsl /opt/jboss/keycloak/  
COPY removeHeaders.xsl /opt/jboss/keycloak/  
COPY changeWelcomeTheme.xsl /opt/jboss/keycloak/  
  
# import themes  
COPY themes /opt/jboss/keycloak/themes/  
  
# required for chown operations  
USER root  
RUN java -jar /usr/share/java/saxon.jar \  
-s:/opt/jboss/keycloak/standalone/configuration/standalone.xml \  
-xsl:/opt/jboss/keycloak/changeProxy.xsl \  
-o:/opt/jboss/keycloak/standalone/configuration/standalone.xml && \  
java -jar /usr/share/java/saxon.jar \  
-s:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml \  
-xsl:/opt/jboss/keycloak/changeProxy.xsl \  
-o:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml && \  
rm /opt/jboss/keycloak/changeProxy.xsl && \  
java -jar /usr/share/java/saxon.jar \  
-s:/opt/jboss/keycloak/standalone/configuration/standalone.xml \  
-xsl:/opt/jboss/keycloak/changeLogger.xsl \  
-o:/opt/jboss/keycloak/standalone/configuration/standalone.xml && \  
java -jar /usr/share/java/saxon.jar \  
-s:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml \  
-xsl:/opt/jboss/keycloak/changeLogger.xsl \  
-o:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml && \  
rm /opt/jboss/keycloak/changeLogger.xsl && \  
java -jar /usr/share/java/saxon.jar \  
-s:/opt/jboss/keycloak/standalone/configuration/standalone.xml \  
-xsl:/opt/jboss/keycloak/removeHeaders.xsl \  
-o:/opt/jboss/keycloak/standalone/configuration/standalone.xml && \  
java -jar /usr/share/java/saxon.jar \  
-s:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml \  
-xsl:/opt/jboss/keycloak/removeHeaders.xsl \  
-o:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml && \  
rm /opt/jboss/keycloak/removeHeaders.xsl && \  
java -jar /usr/share/java/saxon.jar \  
-s:/opt/jboss/keycloak/standalone/configuration/standalone.xml \  
-xsl:/opt/jboss/keycloak/changeWelcomeTheme.xsl \  
-o:/opt/jboss/keycloak/standalone/configuration/standalone.xml && \  
java -jar /usr/share/java/saxon.jar \  
-s:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml \  
-xsl:/opt/jboss/keycloak/changeWelcomeTheme.xsl \  
-o:/opt/jboss/keycloak/standalone/configuration/standalone-ha.xml && \  
rm /opt/jboss/keycloak/changeWelcomeTheme.xsl && \  
chown -R jboss:root /opt/jboss/keycloak/standalone && \  
chmod -R g+rw /opt/jboss/keycloak/standalone && \  
find /opt/jboss/keycloak/standalone -type d -exec chmod g+x "{}" \;  
  
RUN \  
echo 'JAVA_OPTS="$JAVA_OPTS -Dfile.encoding=UTF8"' >>
/opt/jboss/keycloak/bin/standalone.conf  
USER jboss  

