FROM monogramm/docker-axelor-development-kit:4.1  
LABEL maintainer="Mathieu BRUNOT <mathieu.brunot@monogramm.io>"  
  
ENV AXELOR_HOME /opt/adk  
ENV ABS_VERSION 4.2.3  
# Test axelor-development-kit  
RUN set -o errexit -o nounset; \  
echo "Testing Axelor Development Kit installation"; \  
echo "$AXELOR_HOME"; \  
axelor --version  
  
# Switch to root  
USER root  
  
# Second stage: Get axelor-business-suite  
RUN set -o errexit -o nounset ; \  
echo "Downloading Axelor Business Suite"; \  
wget -O abs.tar.gz https://github.com/axelor/axelor-business-
suite/archive/v${ABS_VERSION}.tar.gz; \  
wget -O abs-webapp.tar.gz https://github.com/axelor/abs-
webapp/archive/v${ABS_VERSION}.tar.gz; \  
\  
echo "Building Axelor Business Suite"; \  
tar -xzf abs-webapp.tar.gz; \  
rm abs-webapp.tar.gz; \  
mv "abs-webapp-${ABS_VERSION}" "/usr/src/abs-webapp"; \  
tar -xzf abs.tar.gz; \  
rm abs.tar.gz; \  
rm -rf /usr/src/abs-webapp/modules/abs; \  
mv "axelor-business-suite-${ABS_VERSION}" "/usr/src/abs-webapp/modules/abs"; \  
rm -rf "axelor-business-suite-${ABS_VERSION}"; \  
cd "/usr/src/abs-webapp"; \  
axelor build; \  
\  
echo "Preparing Axelor Business Suite"; \  
mv "/usr/src/abs-webapp/build/libs/abs-webapp-${ABS_VERSION}.war"
"/tmp/abs.war"; \  
./gradlew clean  
  
# Third stage: Deploy and configure the WAR for tomcat  
FROM tomcat:8-jre8  
  
COPY \--from=0 /tmp/abs.war /tmp/abs.war  
  
# Database settings  
ENV DB_DIALECT 'org.hibernate.dialect.PostgreSQLDialect'  
ENV DB_DRIVER 'org.postgresql.Driver'  
ENV DB_URL=postgresql://localhost:5432/axelor-business-suite  
ENV DB_USER ''  
ENV DB_PASSWORD ''  
# link to be used with header logo  
ENV HOME 'http://localhost:8080'  
# Set default language  
ENV LOCALE 'en'  
# Set default CSS theme, for example `blue`  
ENV THEME 'theme-default'  
# Application Mode: Set to 'dev' for development mode else 'prod'  
ENV MODE 'prod'  
# Application Demo: whether to import demo data for the application  
ENV DEMO 'false'  
# Date Format  
ENV DATE_FORMAT 'yyyy-MM-dd'  
# Timezone  
ENV TIMEZONE 'UTC'  
# TODO CORS configuration?  
# LDAP Configuration  
ENV LDAP_URL ''  
ENV LDAP_AUTH_TYPE 'simple'  
ENV LDAP_ADMIN_LOGIN ''  
ENV LDAP_ADMIN_PASS ''  
ENV LDAP_USER_BASE ''  
ENV LDAP_USER_FILTER '(uid={0})'  
ENV LDAP_GROUP_BASE ''  
ENV LDAP_GROUP_FILTER '(uniqueMember=uid={0})'  
ENV LDAP_GROUP_CLASS ''  
# SMTP/IMAP Configuration  
ENV SMTP_HOST ''  
ENV SMTP_PORT ''  
ENV SMTP_CHANNEL ''  
ENV SMTP_USER_NAME ''  
ENV SMTP_PASSWORD ''  
ENV IMAP_HOST ''  
ENV IMAP_PORT ''  
ENV IMAP_CHANNEL ''  
ENV IMAP_USER_NAME ''  
ENV IMAP_PASSWORD ''  
RUN set -ex; \  
echo "Installing needed packages"; \  
# install the packages we need  
apt-get update -q; apt-get install -y --no-install-recommends \  
unzip xmlstarlet \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
echo "Deploying Axelor Business Suite"; \  
unzip /tmp/abs.war -d $CATALINA_HOME/webapps/abs; \  
mv "$CATALINA_HOME/webapps/abs/WEB-INF/classes/application.properties"
"$CATALINA_HOME/webapps/abs/WEB-INF/classes/application.properties.template";
\  
xmlstarlet ed \  
-P -S -L \  
-i '/Server/Service/Engine/Host/Valve' -t 'elem' -n 'Context' \  
-i '/Server/Service/Engine/Host/Context' -t 'attr' -n 'path' -v '/' \  
-i '/Server/Service/Engine/Host/Context[@path="/"]' -t 'attr' -n 'docBase' -v 'abs' \  
-s '/Server/Service/Engine/Host/Context[@path="/"]' -t 'elem' -n 'WatchedResource' -v 'WEB-INF/web.xml' \  
-i '/Server/Service/Engine/Host/Valve' -t 'elem' -n 'Context' \  
-i '/Server/Service/Engine/Host/Context[not(@path="/")]' -t 'attr' -n 'path' -v '/ROOT' \  
-s '/Server/Service/Engine/Host/Context[@path="/ROOT"]' -t 'attr' -n 'docBase' -v 'ROOT' \  
-s '/Server/Service/Engine/Host/Context[@path="/ROOT"]' -t 'elem' -n 'WatchedResource' -v 'WEB-INF/web.xml' \  
$CATALINA_HOME/conf/server.xml; \  
\  
echo "Cleaning Axelor Business Suite"; \  
rm -f /tmp/abs.war  
  
  
VOLUME /srv/axelor/config  
VOLUME /srv/axelor/upload  
VOLUME /srv/axelor/reports  
VOLUME /srv/axelor/reports-gen  
VOLUME /srv/axelor/templates  
VOLUME /srv/axelor/data-export  
VOLUME /srv/axelor/logs  
  
EXPOSE 8080 8443  
WORKDIR $CATALINA_HOME  
  
# Copy entrypoint  
COPY entrypoint.sh /  
RUN set -ex; \  
chmod 755 /entrypoint.sh;  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["catalina.sh", "run"]  
  

