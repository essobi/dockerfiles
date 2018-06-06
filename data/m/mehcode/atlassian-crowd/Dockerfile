FROM java:8  
ARG CROWD_VERSION=2.11.1  
ENV CROWD_HOME /var/atlassian/crowd  
ENV CROWD_INSTALL /opt/atlassian/crowd  
  
# Install Atlassian Crowd  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get clean \  
&& mkdir -p "${CROWD_HOME}" \  
&& chmod -R 700 "${CROWD_HOME}" \  
&& chown -R daemon:daemon "${CROWD_HOME}" \  
&& mkdir -p "${CROWD_INSTALL}" \  
&& curl -L
"https://www.atlassian.com/software/crowd/downloads/binary/atlassian-
crowd-${CROWD_VERSION}.tar.gz" \  
| tar -xz --directory "${CROWD_INSTALL}" \--strip-components=1 --no-same-owner
\  
&& chmod -R 700 "${CROWD_INSTALL}" \  
&& chown -R daemon:daemon "${CROWD_INSTALL}" \  
&& echo -e "\ncrowd.home=$CROWD_HOME" >> "${CROWD_INSTALL}/crowd-webapp/WEB-
INF/classes/crowd-init.properties"  
  
# Install Plugin Manager  
#
https://marketplace.atlassian.com/plugins/com.zenofx.crowd.upm/server/overview  
RUN set -x \  
&& mkdir -p "${CROWD_HOME}/plugins" \  
&& curl -L
"https://marketplace.atlassian.com/download/plugins/com.zenofx.crowd.upm" >
"${CROWD_HOME}/plugins/upm.jar" \  
&& chmod -R 700 "${CROWD_HOME}" \  
&& chown -R daemon:daemon "${CROWD_HOME}"  
  
# Disable: demo, openidclient, and openidsever  
RUN set -x \  
&& rm "${CROWD_INSTALL}/apache-tomcat/conf/Catalina/localhost/demo.xml" \  
&& rm "${CROWD_INSTALL}/apache-
tomcat/conf/Catalina/localhost/openidclient.xml" \  
&& rm "${CROWD_INSTALL}/apache-
tomcat/conf/Catalina/localhost/openidserver.xml"  
  
# Move /crowd to /  
RUN set -x \  
&& mv "${CROWD_INSTALL}/apache-tomcat/conf/Catalina/localhost/crowd.xml"
"${CROWD_INSTALL}/apache-tomcat/conf/Catalina/localhost/ROOT.xml"  
  
# Use the default unprivileged account.  
USER daemon:daemon  
  
# Expose default HTTP connector port.  
EXPOSE 8095  
# Set volume mount points for the home directory.  
VOLUME ["/var/atlassian/crowd"]  
  
# Set the default working directory as the installation directory.  
WORKDIR /var/atlassian/crowd  
  
COPY "docker-entrypoint.sh" "/"  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Run Atlassian Crowd as a foreground process by default.  
CMD ["/opt/atlassian/crowd/apache-tomcat/bin/catalina.sh", "run"]  

