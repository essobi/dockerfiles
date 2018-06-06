FROM mimacom/centos7-java:oraclejdk-8u151-b12  
MAINTAINER sysadmin@mimacom.com  
  
# Setup useful environment variables  
ENV CONFLUENCE_HOME /var/atlassian/application-data/confluence  
ENV CONFLUENCE_INSTALL /opt/atlassian/confluence  
ENV CONF_VERSION 6.8.1  
LABEL Description="This image is used to start Atlassian Confluence"
Vendor="Atlassian" Version="${CONF_VERSION}"  
ENV CONFLUENCE_DOWNLOAD_URL
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONF_VERSION}.tar.gz  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
# Reverse proxy environment variables  
ENV CATALINA_CONNECTOR_PROXYNAME=  
ENV CATALINA_CONNECTOR_PROXYPORT=  
ENV CATALINA_CONNECTOR_SCHEME http  
  
# install the entrypoint  
COPY entrypoint /entrypoint  
RUN chmod 755 /entrypoint  
  
# download oracle jre8  
RUN yum update -y && \  
yum install -y epel-release && \  
  
# graphviz is needed for PlantUML plugin  
yum install -y xmlstarlet graphviz && \  
  
# dependency for installing windows fonts  
yum install -y curl cabextract xorg-x11-font-utils fontconfig && \  
rm -rf /var/cache/yum/*  
  
# install windows fonts  
RUN rpm -i
https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-
installer-2.6-1.noarch.rpm  
  
# download confluence  
RUN mkdir -p "${CONFLUENCE_HOME}" && \  
chmod -R 700 "${CONFLUENCE_HOME}" &&\  
chown ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_HOME}" && \  
  
mkdir -p "${CONFLUENCE_INSTALL}/WEB-INF/classes/" && \  
curl -Ls "${CONFLUENCE_DOWNLOAD_URL}" | tar -xz --directory
"${CONFLUENCE_INSTALL}" \--strip-components=1 \--no-same-owner && \  
  
chmod -R 700 "${CONFLUENCE_INSTALL}" && \  
chown -R ${RUN_USER}:${RUN_GROUP} "${CONFLUENCE_INSTALL}" && \  
echo -e "\nconfluence.home=${CONFLUENCE_HOME}" >>
"${CONFLUENCE_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties"
&& \  
mv "${CONFLUENCE_INSTALL}/conf/server.xml"
"${CONFLUENCE_INSTALL}/conf/server.xml.orig"  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
USER ${RUN_USER}:${RUN_GROUP}  
  
# Expose default HTTP connector port.  
EXPOSE 8090  
EXPOSE 8091  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["${CONFLUENCE_INSTALL}", "${CONFLUENCE_HOME}"]  
  
# Set the default working directory as the Confluence installation directory.  
WORKDIR ${CONFLUENCE_INSTALL}  
  
# start  
ENTRYPOINT ["/entrypoint"]  
  

