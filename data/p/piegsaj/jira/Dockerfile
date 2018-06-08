FROM piegsaj/oracle-jre:latest  
  
MAINTAINER Jens Piegsa (piegsa@gmail.com)  
  
ENV MYSQL_CONNECTOR_VERSION 5.1.38  
ENV CUSTOMFIELD_EDITOR_PLUGIN_BUILD 117  
ENV REST_API_BROWSER_PLUGIN_BUILD 30210  
  
ENV JIRA_HOME /var/atlassian/jira  
ENV JIRA_INSTALL /opt/atlassian/jira  
ENV BUILD_PACKAGES xmlstarlet curl jq  
ENV RUNTIME_PACKAGES libtcnative-1 augeas-tools  
  
ADD dbconfig-template.xml /tmp/  
ADD adjust-log4j-properties.aug /tmp/  
ADD adjust-server-xml.aug /opt/  
ADD adjust-server-xml-proxy-settings.aug /opt/  
ADD run-jira.sh /opt/  
  
RUN apt-get update -qq && \  
apt-get install -qq -y \--no-install-recommends ${RUNTIME_PACKAGES}
${BUILD_PACKAGES} && \  
apt-get clean -qq && \  
  
# Prepare unattended setup  
echo "launch.application$Boolean=false" > /unattended.varfile && \  
echo "rmiPort$Long=8005" >> /unattended.varfile && \  
echo "app.jiraHome=${JIRA_HOME}" >> /unattended.varfile && \  
echo "app.install.service$Boolean=false" >> /unattended.varfile && \  
echo "existingInstallationDir=/opt/JIRA Core" >> /unattended.varfile && \  
echo "sys.confirmedUpdateInstallationString=false" >> /unattended.varfile && \  
echo "sys.languageId=en" >> /unattended.varfile && \  
echo "sys.installationDir=${JIRA_INSTALL}" >> /unattended.varfile && \  
echo "executeLauncherAction$Boolean=true" >> /unattended.varfile && \  
echo "httpPort$Long=8080" >> /unattended.varfile && \  
echo "portChoice=default" >> /unattended.varfile && \  
  
# Calculate download targets  
  
JSON_FEED=https://my.atlassian.com/download/feeds/current/jira-core.json && \  
JSON=$(curl $JSON_FEED -Ls | cut -b 11- | rev | cut -c 2- | rev) && \  
JSON_SELECTOR='.[] | select(.zipUrl | contains("jira-core")) | select(.zipUrl
| contains("-x64.bin"))' && \  
JIRA_VERSION=$(echo "$JSON" | jq -r "$JSON_SELECTOR | .version") && \  
JIRA_DOWNLOAD_URL=$(echo "$JSON" | jq -r "$JSON_SELECTOR | .zipUrl") && \  
MYSQL_CONNECTOR="mysql-connector-java-${MYSQL_CONNECTOR_VERSION}" && \  
  
# Download and install JIRA  
  
curl -Ls ${JIRA_DOWNLOAD_URL} -o /tmp/jira.bin && \  
chmod +x /tmp/jira.bin && \  
./tmp/jira.bin -q -varfile /unattended.varfile && \  
  
# Add MYSQL database connector  
  
curl -Ls
http://dev.mysql.com/get/Downloads/Connector-J/${MYSQL_CONNECTOR}.tar.gz | tar
xz \--directory=/tmp \--no-same-owner && \  
cp /tmp/${MYSQL_CONNECTOR}/${MYSQL_CONNECTOR}-bin.jar ${JIRA_INSTALL}/lib/ &&
\  
  
mkdir -p ${JIRA_HOME}/plugins/installed-plugins/ && \  
  
# Add plugins  
  
curl -Ls
https://marketplace.atlassian.com/download/plugins/jiracustomfieldeditorplugin/version/${CUSTOMFIELD_EDITOR_PLUGIN_BUILD}
\  
-o ${JIRA_HOME}/plugins/installed-plugins/customfield-editor-plugin-${CUSTOMFIELD_EDITOR_PLUGIN_BUILD}.jar && \  
  
curl -Ls
https://marketplace.atlassian.com/download/plugins/com.atlassian.labs.rest-
api-browser/version/${REST_API_BROWSER_PLUGIN_BUILD} \  
-o ${JIRA_HOME}/plugins/installed-plugins/rest-api-browser-plugin-${REST_API_BROWSER_PLUGIN_BUILD}.jar && \  
  
# Adjust configuration files  
  
cp /tmp/dbconfig-template.xml ${JIRA_HOME}/dbconfig-template.xml && \  
augtool -LeAf /tmp/adjust-log4j-properties.aug -r ${JIRA_INSTALL}/ && \  
sed -i "/^jira.home =.*/c\jira.home = ${JIRA_HOME}" ${JIRA_INSTALL}/atlassian-
jira/WEB-INF/classes/jira-application.properties && \  
echo "${JIRA_VERSION}" > ${JIRA_INSTALL}/jira.version && \  
  
  
# Adjust file permissions  
  
chmod -R 700 ${JIRA_INSTALL}/conf && \  
chmod -R 700 ${JIRA_INSTALL}/logs && \  
chmod -R 700 ${JIRA_INSTALL}/temp && \  
chmod -R 700 ${JIRA_INSTALL}/work && \  
chown -R jira:jira ${JIRA_INSTALL}/conf && \  
chown -R jira:jira ${JIRA_INSTALL}/logs && \  
chown -R jira:jira ${JIRA_INSTALL}/temp && \  
chown -R jira:jira ${JIRA_INSTALL}/work && \  
chmod +x /opt/run-jira.sh && \  
chown jira:jira $JAVA_HOME/jre/lib/security/cacerts && \  
chmod -R 700 ${JIRA_HOME} && \  
chown -R jira:jira ${JIRA_HOME} && \  
  
# Clean up  
  
apt-get remove -qq \--purge -y ${BUILD_PACKAGES} $(apt-mark showauto) && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
USER jira:jira  
  
EXPOSE 8005 8080 8443  
  
VOLUME ${JIRA_HOME}  
VOLUME ${JIRA_INSTALL}/conf  
VOLUME /etc/jira  
  
WORKDIR ${JIRA_HOME}  
  
CMD ["/opt/run-jira.sh"]  

