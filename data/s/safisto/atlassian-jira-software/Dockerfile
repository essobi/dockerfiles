FROM cptactionhank/atlassian-jira-software:7.7.1  
ARG GIT_COMMIT  
  
LABEL maintainer="timo.schaefer@safisto.de" \  
git.commit="${GIT_COMMIT}" \  
description="Atlassian JIRA Software in a Docker container"  
  
USER root  
  
COPY catalina-connector-opts.sh ${JIRA_INSTALL}/bin/  
  
RUN set -x && \  
sed -i -e '/^export JAVA_OPTS$/a\\\n. $PRGDIR/catalina-connector-
opts.sh\nexport CATALINA_OPTS' ${JIRA_INSTALL}/bin/setenv.sh && \  
sed -i 's@Connector port="8080"@Connector port="8080"
secure="${catalinaConnectorSecure}" scheme="${catalinaConnectorScheme}"
proxyName="${catalinaConnectorProxyName}"
proxyPort="${catalinaConnectorProxyPort}"@' ${JIRA_INSTALL}/conf/server.xml &&
\  
chmod 755 ${JIRA_INSTALL}/bin/catalina-connector-opts.sh && \  
\  
echo "GIT COMMIT: $GIT_COMMIT" > /RELEASE  
  
USER daemon  

