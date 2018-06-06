FROM openjdk:8u121-alpine  
  
ARG CONFLUENCE_VERSION=6.7.0  
ARG POSTGRES_DRIVER_VERSION=42.1.4  
ARG MYSQL_DRIVER_VERSION=5.1.45  
  
ARG CONFLUENCE_HOME=/var/atlassian/confluence  
ARG CONFLUENCE_INSTALL=/opt/atlassian/confluence  
  
ARG
CONFLUENCE_DOWNLOAD_URI=https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz  
  
ARG RUN_USER=confluence  
ARG RUN_GROUP=confluence  
  
ENV LC_ALL=C \  
CONFLUENCE_HOME=$CONFLUENCE_HOME \  
CONFLUENCE_INSTALL=$CONFLUENCE_INSTALL  
# Setup Confluence User & Group + directories  
RUN addgroup -S "${RUN_GROUP}" \  
&& adduser -S -s /bin/false -G "${RUN_GROUP}" "${RUN_USER}" \  
&& mkdir -p "${CONFLUENCE_HOME}" \  
"${CONFLUENCE_INSTALL}/conf"  
# Install build deps & required binaries  
RUN apk add \--no-cache --virtual .build-deps \  
curl \  
tar \  
&& apk add \--no-cache \  
bash \  
fontconfig \  
ttf-dejavu  
# Confluence install/setup. Order of operations:  
# 1. Confluence assets + install  
# 2. Postgres Driver  
# 3. MySQL Driver  
# 4. Permissions  
# 5. Update configurations  
RUN curl -Ls "${CONFLUENCE_DOWNLOAD_URI}" \  
| tar -xz --directory "${CONFLUENCE_INSTALL}" \  
\--strip-components=1 --no-same-owner \  
&& cd "${CONFLUENCE_INSTALL}/confluence/WEB-INF/lib" \  
&& rm -f "./postgresql-9.*" \  
&& curl -Os
"https://jdbc.postgresql.org/download/postgresql-${POSTGRES_DRIVER_VERSION}.jar"
\  
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
| tar -xz --directory "${CONFLUENCE_INSTALL}/confluence/WEB-INF/lib" \  
\--strip-components=1 --no-same-owner \  
"mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar" \  
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
&& echo -e "\nconfluence.home=${CONFLUENCE_HOME}" \  
>> "${CONFLUENCE_INSTALL}/confluence/WEB-INF/classes/confluence-
init.properties" \  
&& touch -d "@0" "${CONFLUENCE_INSTALL}/conf/server.xml"  
# Remove build dependencies  
RUN apk del .build-deps  
  
# Switch from root  
USER "${RUN_USER}":"${RUN_GROUP}"  
# Expose ports  
EXPOSE 8090  
  
# Persist some of the install dir + the home dir + JRE security folder
(cacerts)  
VOLUME ["${CONFLUENCE_INSTALL}/logs", "${CONFLUENCE_INSTALL}/conf",
"${CONFLUENCE_HOME}", "${JAVA_HOME}/jre/lib/security/"]  
  
# Set working directory to install directory  
WORKDIR "${CONFLUENCE_INSTALL}"  
# Run in foreground  
CMD ["./bin/catalina.sh", "run"]  
  
# Copy & set entrypoint for manual access  
COPY ./docker-entrypoint.sh /  
COPY ./entrypoint.d/ /entrypoint.d/  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Metadata  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL maintainer="LasLabs Inc <support@laslabs.com>" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Confluence - Alpine" \  
org.label-schema.description="Provides a Docker image for Confluence on Alpine
Linux." \  
org.label-schema.url="https://laslabs.com/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/LasLabs/docker-alpine-confluence"
\  
org.label-schema.vendor="LasLabs Inc." \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  

