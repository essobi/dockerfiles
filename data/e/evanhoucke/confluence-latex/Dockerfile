FROM debian:stretch  
  
# Setup useful environment variables  
ENV CONF_HOME /var/atlassian/confluence  
ENV CONF_INSTALL /opt/atlassian/confluence  
ENV CONF_VERSION 6.7.0  
  
ENV JAVA_CACERTS $JAVA_HOME/jre/lib/security/cacerts  
ENV CERTIFICATE $CONF_HOME/certificate  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list  
  
# Install Java.  
RUN rm -rf /var/lib/apt/lists/* && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get update && \  
apt-get -y --force-yes install oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Install Atlassian Confluence and hepler tools and setup initial home  
# directory structure.  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes \--no-install-recommends libtcnative-1
xmlstarlet curl \  
&& apt-get clean \  
&& mkdir -p "${CONF_HOME}" \  
&& chmod -R 700 "${CONF_HOME}" \  
&& chown daemon:daemon "${CONF_HOME}" \  
&& mkdir -p "${CONF_INSTALL}/conf" \  
&& curl -Ls
"https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONF_VERSION}.tar.gz" | tar -xz --directory "${CONF_INSTALL}"
\--strip-components=1 \--no-same-owner \  
&& curl -L "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.38.tar.gz" | tar -xz --directory "${CONF_INSTALL}/confluence/WEB-
INF/lib" \--strip-components=1 \--no-same-owner "mysql-connector-
java-5.1.38/mysql-connector-java-5.1.38-bin.jar" \  
&& chmod -R 700 "${CONF_INSTALL}/conf" \  
&& chmod -R 700 "${CONF_INSTALL}/temp" \  
&& chmod -R 700 "${CONF_INSTALL}/logs" \  
&& chmod -R 700 "${CONF_INSTALL}/work" \  
&& chown -R daemon:daemon "${CONF_INSTALL}/conf" \  
&& chown -R daemon:daemon "${CONF_INSTALL}/temp" \  
&& chown -R daemon:daemon "${CONF_INSTALL}/logs" \  
&& chown -R daemon:daemon "${CONF_INSTALL}/work" \  
&& echo -e "\nconfluence.home=$CONF_HOME" >> "${CONF_INSTALL}/confluence/WEB-
INF/classes/confluence-init.properties" \  
&& xmlstarlet ed --inplace \  
\--delete "Server/@debug" \  
\--delete "Server/Service/Connector/@debug" \  
\--delete "Server/Service/Connector/@useURIValidationHack" \  
\--delete "Server/Service/Connector/@minProcessors" \  
\--delete "Server/Service/Connector/@maxProcessors" \  
\--delete "Server/Service/Engine/@debug" \  
\--delete "Server/Service/Engine/Host/@debug" \  
\--delete "Server/Service/Engine/Host/Context/@debug" \  
"${CONF_INSTALL}/conf/server.xml" \  
&& touch -d "@0" "${CONF_INSTALL}/conf/server.xml"  
  
RUN apt-get update --quiet \  
&& apt-get install --yes \--no-install-recommends dvipng texlive-latex-base
texlive-extra-utils texlive-math-extra mimetex graphviz  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
USER daemon:daemon  
  
# Expose default HTTP connector port.  
EXPOSE 8090  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["/var/atlassian/confluence", "/opt/atlassian/confluence/logs"]  
  
# Set the default working directory as the Confluence home directory.  
WORKDIR /var/atlassian/confluence  
  
# Run Atlassian Confluence as a foreground process by default.  
CMD ["/opt/atlassian/confluence/bin/catalina.sh", "run"]  

