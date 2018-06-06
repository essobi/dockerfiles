FROM jetty:9.4  
MAINTAINER Ronny Trommer <ronny@opennms.org>  
  
ENV OCA_CHECK_VERSION 1.1  
ENV OCA_CHECK_WAR_URL https://github.com/opennms-forge/opennms-oca-github-
plugin/releases/download/v${OCA_CHECK_VERSION}/oca-github-
plugin-${OCA_CHECK_VERSION}.war  
ENV OCA_CHECK_DEPLOY_DIR /var/lib/jetty/webapps  
ENV OCA_PLUGIN_CONFIG_DIR /etc/oca-github-plugin  
ENV OCA_PLUGIN_CONFIG ${OCA_PLUGIN_CONFIG_DIR}/oca-github-plugin.properties  
ENV OCA_PLUGIN_MAPPING ${OCA_PLUGIN_CONFIG_DIR}/oca-mapping.properties  
ENV GITHUB_API_TOKEN myToken  
ENV GITHUB_USER myUser  
ENV GITHUB_REPOSITORY myRepo  
ENV GITHUB_WEBHOOK_SECRET myWebhookSecret  
ENV OCA_REGEXP_REDO myRegexpRedo  
ENV MAPPING_FILE_LOCATION myMappingFileLocation  
  
USER root  
  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
curl -L ${OCA_CHECK_WAR_URL} -o ${OCA_CHECK_DEPLOY_DIR}/oca-check.war && \  
mkdir ${OCA_PLUGIN_CONFIG_DIR} && \  
chown -R jetty:jetty ${OCA_CHECK_DEPLOY_DIR} ${OCA_PLUGIN_CONFIG_DIR} && \  
apt -y purge curl && \  
apt-get -y autoremove && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY assets/* ${OCA_PLUGIN_CONFIG_DIR}/  
COPY ./docker-entrypoint.sh /  
  
LABEL license="GPLv3" \  
org.opennms.ocacheck.version="${OCA_CHECK_VERSION}" \  
vendor="OpenNMS Community" \  
name="OCA Check GitHub Plugin"  
  
USER jetty  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  
CMD [ "-h" ]  
  
EXPOSE 8080  

