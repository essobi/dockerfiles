FROM jboss/base-jdk:8  
ENV KEYCLOAK_VERSION 2.5.4.Final  
# Enables signals getting passed from startup script to JVM  
# ensuring clean shutdown when container is stopped.  
ENV LAUNCH_JBOSS_IN_BACKGROUND 1  
USER root  
  
RUN yum install -y epel-release && yum install -y jq && yum clean all  
  
RUN cd /opt/jboss/ && curl -L
https://downloads.jboss.org/keycloak/$KEYCLOAK_VERSION/keycloak-$KEYCLOAK_VERSION.tar.gz
| tar zx && mv /opt/jboss/keycloak-$KEYCLOAK_VERSION /opt/jboss/keycloak  
  
ADD docker-entrypoint.sh /opt/jboss/  
  
ADD setLogLevel.xsl /opt/jboss/keycloak/  
RUN java -jar /usr/share/java/saxon.jar
-s:/opt/jboss/keycloak/standalone/configuration/standalone.xml
-xsl:/opt/jboss/keycloak/setLogLevel.xsl
-o:/opt/jboss/keycloak/standalone/configuration/standalone.xml  
RUN sed -i 's/\\(logger.handlers=CONSOLE\\),FILE/\1/'
keycloak/standalone/configuration/logging.properties  
  
ENV JBOSS_HOME /opt/jboss/keycloak  
  
ADD https://circleci.com/api/v1/project/redhat-ipaas/keycloak-
customizations/latest/artifacts/0/\$CIRCLE_ARTIFACTS/openshift-provider.jar
/opt/jboss/keycloak/providers/  
ADD https://circleci.com/api/v1/project/redhat-ipaas/keycloak-
customizations/latest/artifacts/0/\$CIRCLE_ARTIFACTS/ipaas-theme.jar
/opt/jboss/keycloak/providers/  
ADD https://circleci.com/api/v1/project/redhat-ipaas/keycloak-
customizations/latest/artifacts/0/\$CIRCLE_ARTIFACTS/autolink-idp.jar
/opt/jboss/keycloak/providers/  
#ADD openshift-provider.jar /opt/jboss/keycloak/providers/  
#ADD ipaas-theme.jar /opt/jboss/keycloak/providers/  
#ADD autolink-idp.jar /opt/jboss/keycloak/providers/  
RUN mkdir -p /opt/jboss/keycloak/themes/keycloak/admin/resources/partials/ &&
\  
cd /opt/jboss/keycloak/themes/keycloak/admin/resources/partials/ && \  
unzip -j /opt/jboss/keycloak/providers/ipaas-theme.jar
theme/ipaas/admin/resources/partials/realm-identity-provider-openshift.html
theme/ipaas/admin/resources/partials/realm-identity-provider-openshift-
ext.html && \  
mkdir -p /opt/jboss/keycloak/themes/keycloak/admin/messages/ && \  
cd /opt/jboss/keycloak/themes/keycloak/admin/messages/ && \  
unzip -j /opt/jboss/keycloak/providers/ipaas-theme.jar
theme/ipaas/admin/messages/admin-messages_en.properties && \  
chmod g+rwX /opt/jboss/keycloak/providers/*.jar  
RUN cd /opt/jboss/keycloak/themes/ && \  
unzip /opt/jboss/keycloak/providers/ipaas-theme.jar && \  
mv theme/ipaas . && \  
rm -rf theme META-INF  
  
RUN mkdir $JBOSS_HOME/standalone/{data,log} && \  
chown -R jboss:root $JBOSS_HOME && \  
find $JBOSS_HOME -type d -exec chmod 770 {} \; && \  
find $JBOSS_HOME/standalone/configuration -type f -exec chmod 660 {} \;  
  
USER jboss  
  
EXPOSE 8080  
ENTRYPOINT [ "/opt/jboss/docker-entrypoint.sh" ]  
  
CMD ["-b", "0.0.0.0"]  

