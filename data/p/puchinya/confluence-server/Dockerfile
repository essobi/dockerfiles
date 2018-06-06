  
FROM java:openjdk-8-jre  
MAINTAINER puchinya  
  
# Setup useful environment variables  
ENV CONFLUENCE_HOME /var/atlassian/application-data/confluence  
ENV CONFLUENCE_INSTALL /opt/atlassian/confluence  
ENV CONF_VERSION 6.7.2  
ENV CONFLUENCE_PROXY_NAME="localhost"  
ENV CONFLUENCE_PROXY_PORT="443"  
ENV CONFLUENCE_SCHEME="https"  
ENV CONFLUENCE_SECURE="true"  
LABEL Description="This image is used to start Atlassian Confluence"
Vendor="Atlassian" Version="${CONF_VERSION}"  
  
ENV CONFLUENCE_DOWNLOAD_URL
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONF_VERSION}.tar.gz  
  
ENV MYSQL_VERSION 5.1.38  
ENV MYSQL_DRIVER_DOWNLOAD_URL
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_VERSION}.tar.gz  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
# Install Atlassian Confluence and helper tools and setup initial home  
# directory structure.  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1
xmlstarlet \  
&& apt-get clean \  
&& mkdir -p "${CONFLUENCE_HOME}" \  
&& chmod -R 700 "${CONFLUENCE_HOME}" \  
&& chown ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_HOME}" \  
&& mkdir -p "${CONFLUENCE_INSTALL}/conf" \  
&& curl -Ls "${CONFLUENCE_DOWNLOAD_URL}" | tar -xz --directory
"${CONFLUENCE_INSTALL}" \--strip-components=1 --no-same-owner \  
&& curl -Ls "${MYSQL_DRIVER_DOWNLOAD_URL}" | tar -xz --directory
"${CONFLUENCE_INSTALL}/confluence/WEB-INF/lib" \--strip-components=1 --no-
same-owner "mysql-connector-java-${MYSQL_VERSION}/mysql-connector-
java-${MYSQL_VERSION}-bin.jar" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/conf" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/temp" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/logs" \  
&& chmod -R 700 "${CONFLUENCE_INSTALL}/work" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_INSTALL}/conf" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_INSTALL}/temp" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_INSTALL}/logs" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_INSTALL}/work" \  
&& echo -e "\nconfluence.home=${CONFLUENCE_HOME}" >>
"${CONFLUENCE_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties"
\  
&& xmlstarlet ed --inplace \  
\--delete "Server/@debug" \  
\--delete "Server/Service/Connector/@debug" \  
\--delete "Server/Service/Connector/@useURIValidationHack" \  
\--delete "Server/Service/Connector/@minProcessors" \  
\--delete "Server/Service/Connector/@maxProcessors" \  
\--delete "Server/Service/Engine/@debug" \  
\--delete "Server/Service/Engine/Host/@debug" \  
\--delete "Server/Service/Engine/Host/Context/@debug" \  
"${CONFLUENCE_INSTALL}/conf/server.xml" \  
&& touch -d "@0" "${CONFLUENCE_INSTALL}/conf/server.xml"  
  
RUN apt-get install --quiet --yes graphviz  
RUN apt-get install --quiet --yes fontconfig  
  
ENV TAKAOFONT_DOWNLOAD_URL https://launchpad.net/takao-
fonts/trunk/15.03/+download/TakaoFonts_00303.01.zip  
ENV TAKAOFONT_FILE_NAME_NOEXT TakaoFonts_00303.01  
ENV TAKAOFONT_FILE_NAME ${TAKAOFONT_FILE_NAME_NOEXT}.zip  
  
ENV CATALINA_OPTS=-Dconfluence.document.conversion.fontpath=/usr/share/fonts/  
  
# Install Takao Font for Japanese  
RUN wget -O ${TAKAOFONT_FILE_NAME} ${TAKAOFONT_DOWNLOAD_URL}  
RUN unzip ${TAKAOFONT_FILE_NAME}  
RUN mv ${TAKAOFONT_FILE_NAME_NOEXT} /usr/share/fonts/truetype/  
RUN fc-cache -f -v  
  
# link to JRE fonts  
RUN mkdir -p ${JAVA_HOME}/lib/fonts/fallback  
RUN (cd ${JAVA_HOME}/lib/fonts/fallback;ln -s
/usr/share/fonts/truetype/${TAKAOFONT_FILE_NAME_NOEXT}/TakaoGothic.ttf;ln -s
/usr/share/fonts/truetype/${TAKAOFONT_FILE_NAME_NOEXT}/TakaoMincho.ttf;ln -s
/usr/share/fonts/truetype/${TAKAOFONT_FILE_NAME_NOEXT}/TakaoPGothic.ttf;ln -s
/usr/share/fonts/truetype/${TAKAOFONT_FILE_NAME_NOEXT}/TakaoPMincho.ttf)  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
USER ${RUN_USER}:${RUN_GROUP}  
  
ADD ./server.xml ${CONFLUENCE_INSTALL}/conf/server.xml.org  
ADD ./bootstrap.sh ${CONFLUENCE_INSTALL}/bin/bootstrap.sh  
  
# Expose default HTTP connector port.  
EXPOSE 8090  
EXPOSE 8091  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["${CONFLUENCE_INSTALL}", "${CONFLUENCE_HOME}"]  
  
# Set the default working directory as the Confluence installation directory.  
WORKDIR ${CONFLUENCE_INSTALL}  
  
# Run Atlassian Confluence as a foreground process by default.  
CMD ["sh", "./bin/bootstrap.sh"]  

