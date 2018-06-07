FROM java:openjdk-8-jre  
  
MAINTAINER Films familytoto@daum.net  
  
## ENV Directory  
ENV CONFLUENCE_DATA /home/confluence  
ENV CONFLUENCE_INSTALL /usr/local/confluence  
  
## Download URL  
ENV CONFLUENCE_URL
https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-6.2.3.tar.gz  
ENV MYSQL_JDBC_URL https://dev.mysql.com/get/Downloads/Connector-J/mysql-
connector-java-5.1.40.tar.gz  
  
## Run User  
ENV USER conflunce  
ENV GROUP conflunce  
  
RUN set -x \  
&& useradd -d "${CONFLUENCE_INSTALL}" "${USER}" \  
&& apt-get update --quiet \  
&& mkdir -p "${CONFLUENCE_DATA}" \  
&& mkdir -p "${CONFLUENCE_INSTALL}" \  
&& curl -Ls "${CONFLUENCE_URL}" | tar -xz --directory "${CONFLUENCE_INSTALL}"
\--strip-components=1 --no-same-owner \  
&& curl -Ls "${MYSQL_JDBC_URL}" | tar -xz --directory
"${CONFLUENCE_INSTALL}/lib" \--strip-components=1 --no-same-owner "mysql-
connector-java-5.1.40/mysql-connector-java-5.1.40-bin.jar" \  
&& chown -R ${USER}:${GROUP} "${CONFLUENCE_DATA}" \  
&& chown -R ${USER}:${GROUP} "${CONFLUENCE_INSTALL}" \  
&& echo "confluence.home=${CONFLUENCE_DATA}" >
"${CONFLUENCE_INSTALL}"/confluence/WEB-INF/classes/confluence-init.properties  
  
USER ${USER}:${GROUP}  
  
EXPOSE 8090 8091  
VOLUME ["/home/confluence"]  
  
WORKDIR ${CONFLUENCE_INSTALL}  
  
CMD ["./bin/start-confluence.sh", "-fg"]  

