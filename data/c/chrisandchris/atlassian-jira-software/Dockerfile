FROM ahaasler/jira-base:alpine-8u102b14-server-jre  
MAINTAINER Chrisandchris <null@example.org>  
  
# Configuration  
ENV JIRA_VERSION 7.5.0  
ENV JIRA_INSTALL /opt/jira  
ENV MYSQL_VERSION 5.1.44  
ENV MYSQL_DRIVER_DOWNLOAD_URL
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_VERSION}.tar.gz  
  
# Download and install jira in /opt with proper permissions and clean
unnecessary files  
RUN \  
curl -Lks https://downloads.atlassian.com/software/jira/downloads/atlassian-
jira-core-$JIRA_VERSION.tar.gz \  
-o /tmp/jira.tar.gz \  
&& mkdir -p /opt/jira \  
&& tar -zxf /tmp/jira.tar.gz --strip=1 -C /opt/jira \  
&& chown -R root:root /opt/jira \  
&& chown -R 547:root /opt/jira/logs /opt/jira/temp /opt/jira/work \  
&& rm /tmp/jira.tar.gz  
  
RUN \  
curl -Ls "${MYSQL_DRIVER_DOWNLOAD_URL}" \  
| tar -xz --directory "/opt/jira/lib" \  
\--strip-components=1 --no-same-owner \  
"mysql-connector-java-${MYSQL_VERSION}/mysql-connector-
java-${MYSQL_VERSION}-bin.jar"  
  
RUN \  
rm -rf /data/jira \  
&& mkdir -p /data/jira \  
&& chown root:root /data/jira \  
&& chmod 0777 /data \  
&& chmod 0777 /data/jira  
  
# Remove some env variables from setup, so we can set them inplace  
RUN \  
chmod 0777 ${JIRA_INSTALL}/bin/setenv.sh \  
&& sed -i 's/JVM_MINIMUM_MEMORY=.*//g' ${JIRA_INSTALL}/bin/setenv.sh \  
&& sed -i 's/JVM_MAXIMUM_MEMORY=.*//g' ${JIRA_INSTALL}/bin/setenv.sh  
  
VOLUME ["/opt/jira"]  
  
COPY launch.sh /launch  
RUN chmod +x /launch  
  
EXPOSE 8080  
WORKDIR /opt/jira  
ENTRYPOINT ["/launch"]  

