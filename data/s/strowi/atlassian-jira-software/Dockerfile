FROM openjdk:8u121-alpine  
MAINTAINER Roman v. Gemmeren <strowi@hasnoname.de>  
  
ARG JIRA_VERSION=7.5.0  
ARG
JIRA_DOWNLOAD_URI=https://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-core-${JIRA_VERSION}.tar.gz  
  
ARG POSTGRES_DRIVER_VERSION=42.1.1  
ARG MYSQL_DRIVER_VERSION=5.1.38  
  
# Setup useful environment variables  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
ENV JIRA_HOME /var/atlassian/jira  
ENV JIRA_INSTALL /opt/atlassian/jira  
  
RUN apk --update --no-cache add \  
curl \  
tar \  
bash \  
fontconfig \  
ttf-dejavu \  
xmlstarlet \  
# Create home, install, and conf dirs  
&& mkdir -p "${JIRA_HOME}" \  
"${JIRA_INSTALL}/conf" \  
# Download assets and extract to appropriate locations  
&& curl -Ls "${JIRA_DOWNLOAD_URI}" \  
| tar -xz --directory "${JIRA_INSTALL}" \  
\--strip-components=1 --no-same-owner \  
# Update the Postgres library to allow non-archaic Postgres versions  
&& cd "${JIRA_INSTALL}/lib" \  
&& rm -f "./postgresql-9.*" \  
&& curl -Os
"https://jdbc.postgresql.org/download/postgresql-${POSTGRES_DRIVER_VERSION}.jar"
\  
# Add MySQL library  
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
| tar -xz --directory "${JIRA_INSTALL}/lib" \  
\--strip-components=1 --no-same-owner \  
"mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar" \  
# Setup permissions  
&& chmod -R 700 "${JIRA_HOME}" \  
"${JIRA_INSTALL}/conf" \  
"${JIRA_INSTALL}/temp" \  
"${JIRA_INSTALL}/logs" \  
"${JIRA_INSTALL}/work" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${JIRA_HOME}" \  
"${JIRA_INSTALL}/conf" \  
"${JIRA_INSTALL}/temp" \  
"${JIRA_INSTALL}/logs" \  
"${JIRA_INSTALL}/work" \  
&& sed --in-place "s/java version/openjdk version/g"
"${JIRA_INSTALL}/bin/check-java.sh" \  
# Update configs  
&& echo -e "\jira.home=${JIRA_HOME}" \  
>> "${JIRA_INSTALL}/atlassian-jira/WEB-INF/classes/jira-
application.properties" \  
&& touch -d "@0" "${JIRA_INSTALL}/conf/server.xml" \  
&& apk del tar curl \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
USER "${RUN_USER}":"${RUN_GROUP}"  
# Expose HTTP  
EXPOSE 8090  
  
# Persist some of the install dir + the home dir + JRE security folder
(cacerts)  
VOLUME ["${JIRA_INSTALL}/logs", "${JIRA_HOME}"]  
  
# Set working directory to install directory  
WORKDIR "${JIRA_INSTALL}"  
# Run in foreground  
CMD ["./bin/catalina.sh", "run"]  
  
ADD src/ /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

