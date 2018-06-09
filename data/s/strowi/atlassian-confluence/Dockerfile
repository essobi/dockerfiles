FROM openjdk:8u121-alpine  
MAINTAINER Roman v. Gemmeren <strowi@hasnoname.de>  
  
ARG CONFLUENCE_VERSION=6.4.0  
ARG
CONFLUENCE_DOWNLOAD_URI=https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz  
  
ARG POSTGRES_DRIVER_VERSION=42.1.1  
ARG MYSQL_DRIVER_VERSION=5.1.38  
  
# Setup useful environment variables  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
ENV CONFLUENCE_HOME /var/atlassian/confluence  
ENV CONFLUENCE_INSTALL /opt/atlassian/confluence  
  
RUN apk --update --no-cache add \  
curl \  
tar \  
bash \  
fontconfig \  
ttf-dejavu \  
xmlstarlet \  
# Create home, install, and conf dirs  
&& mkdir -p "${CONFLUENCE_HOME}" \  
"${CONFLUENCE_INSTALL}/conf" \  
# Download assets and extract to appropriate locations  
&& curl -Ls "${CONFLUENCE_DOWNLOAD_URI}" \  
| tar -xz --directory "${CONFLUENCE_INSTALL}" \  
\--strip-components=1 --no-same-owner \  
# Update the Postgres library to allow non-archaic Postgres versions  
&& cd "${CONFLUENCE_INSTALL}/confluence/WEB-INF/lib" \  
&& rm -f "./postgresql-9.*" \  
&& curl -Os
"https://jdbc.postgresql.org/download/postgresql-${POSTGRES_DRIVER_VERSION}.jar"
\  
# Add MySQL library  
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
| tar -xz --directory "${CONFLUENCE_INSTALL}/confluence/WEB-INF/lib" \  
\--strip-components=1 --no-same-owner \  
"mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar" \  
# Setup permissions  
&& chmod -R 700 "${CONFLUENCE_HOME}" \  
"${CONFLUENCE_INSTALL}/conf" \  
"${CONFLUENCE_INSTALL}/temp" \  
"${CONFLUENCE_INSTALL}/logs" \  
"${CONFLUENCE_INSTALL}/work" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_HOME}" \  
"${CONFLUENCE_INSTALL}/conf" \  
"${CONFLUENCE_INSTALL}/temp" \  
"${CONFLUENCE_INSTALL}/logs" \  
"${CONFLUENCE_INSTALL}/work" \  
# Update configs  
&& echo -e "\nconfluence.home=${CONFLUENCE_HOME}" \  
>> "${CONFLUENCE_INSTALL}/confluence/WEB-INF/classes/confluence-
init.properties" \  
&& touch -d "@0" "${CONFLUENCE_INSTALL}/conf/server.xml" \  
&& apk del tar curl \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
USER "${RUN_USER}":"${RUN_GROUP}"  
# Expose HTTP  
EXPOSE 8090  
  
# Persist some of the install dir + the home dir + JRE security folder
(cacerts)  
VOLUME ["${CONFLUENCE_INSTALL}/logs", "${CONFLUENCE_INSTALL}/conf",
"${CONFLUENCE_HOME}", "${JAVA_HOME}/jre/lib/security/"]  
  
# Set working directory to install directory  
WORKDIR "${CONFLUENCE_INSTALL}"  
# Run in foreground  
CMD ["./bin/catalina.sh", "run"]  
  
ADD src/ /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

