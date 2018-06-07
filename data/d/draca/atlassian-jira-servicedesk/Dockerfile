FROM anapsix/alpine-java:8u162b12_jdk  
  
MAINTAINER draca <info@draca.be>  
  
ARG JIRA_VERSION=3.13.0  
ARG
JIRA_DOWNLOAD=https://www.atlassian.com/software/jira/downloads/binary/atlassian-
servicedesk-3.13.0.tar.gz  
  
ENV JIRA_HOME=/opt/atlassian/jira/data  
ENV JIRA_INSTALL=/opt/atlassian/jira/install  
  
ENV RUN_USER=jira  
ENV RUN_GROUP=jira  
  
EXPOSE 8080  
WORKDIR $JIRA_HOME  
  
RUN apk add --no-cache curl tar shadow\  
&& groupadd -r ${RUN_GROUP} \  
&& useradd -r -g ${RUN_GROUP} ${RUN_USER} \  
&& mkdir -p "${JIRA_HOME}" "${JIRA_INSTALL}" \  
&& curl -Ls ${JIRA_DOWNLOAD} | tar -xz --directory "${JIRA_INSTALL}" \--strip-
components=1 --no-same-owner \  
&& echo -e "\njira.home=${JIRA_HOME}" >> "${JIRA_INSTALL}/atlassian-jira/WEB-
INF/classes/jira-application.properties" \  
&& apk del curl tar shadow  
  
COPY "entrypoint.sh" "/"  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/opt/atlassian/jira/install/bin/start-jira.sh", "-fg"]

