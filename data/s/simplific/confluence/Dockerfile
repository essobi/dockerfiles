FROM anapsix/alpine-java:8  
# Configuration variables  
ENV CONFLUENCE_HOME /var/atlassian/confluence  
ENV CONFLUENCE_INSTALL /opt/atlassian/confluence  
ENV CONFLUENCE_VERSION 6.4.2  
# Install Atlassian JIRA and helper tools  
RUN apk --update add curl tar \  
&& mkdir -p ${CONFLUENCE_HOME} \  
&& mkdir -p ${CONFLUENCE_INSTALL} \  
&& curl -Ls
"https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz" | tar -xz --directory
"${CONFLUENCE_INSTALL}" \--strip-components=1 --no-same-owner \  
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.36.tar.gz" | tar -xz --directory "${CONFLUENCE_INSTALL}/lib"
\--strip-components=1 --no-same-owner "mysql-connector-java-5.1.36/mysql-
connector-java-5.1.36-bin.jar" \  
&& echo -e "\nconfluence.home=$CONFLUENCE_HOME" >>
"${CONFLUENCE_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties"
\  
&& chown -R daemon:daemon ${CONFLUENCE_INSTALL} \  
&& chown -R daemon:daemon ${CONFLUENCE_HOME}  
  
EXPOSE 8090  
USER daemon:daemon  
  
VOLUME ${CONFLUENCE_HOME}  
  
WORKDIR ${CONFLUENCE_HOME}  
  
CMD ["sh", "-c", "${CONFLUENCE_INSTALL}/bin/start-confluence.sh -fg"]  

