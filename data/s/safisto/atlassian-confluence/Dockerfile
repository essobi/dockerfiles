FROM cptactionhank/atlassian-confluence:6.7.0  
ARG GIT_COMMIT  
  
LABEL maintainer="timo.schaefer@safisto.de" \  
git.commit="${GIT_COMMIT}" \  
description="Atlassian Confluence in a Docker container"  
  
USER root  
  
COPY catalina-connector-opts.sh ${CONF_INSTALL}/bin/  
  
RUN set -x && \  
sed -i -e 's@^export CATALINA_OPTS@. $PRGDIR/catalina-connector-
opts.sh\nexport CATALINA_OPTS@' ${CONF_INSTALL}/bin/setenv.sh && \  
sed -i 's@Connector port="8090"@Connector port="8090"
secure="${catalinaConnectorSecure}" scheme="${catalinaConnectorScheme}"
proxyName="${catalinaConnectorProxyName}"
proxyPort="${catalinaConnectorProxyPort}"@' ${CONF_INSTALL}/conf/server.xml &&
\  
chmod 755 ${CONF_INSTALL}/bin/catalina-connector-opts.sh && \  
\  
echo "GIT COMMIT: $GIT_COMMIT" > /RELEASE  
  
USER daemon  

