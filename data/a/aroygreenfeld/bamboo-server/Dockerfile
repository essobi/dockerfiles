FROM java:8  
MAINTAINER Audrey Roy Greenfeld (@audreyr)  
  
# Config vars  
ENV BAMBOO_HOME /var/atlassian/bamboo  
ENV BAMBOO_INSTALL /opt/atlassian/bamboo  
ENV BAMBOO_VERSION 5.9.7  
# Install Atlassian Bamboo and helper tools and setup initial home  
# directory structure.  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1
xmlstarlet \  
&& apt-get clean \  
&& mkdir -p "${BAMBOO_HOME}" \  
&& mkdir -p "${BAMBOO_HOME}/caches/indexes" \  
&& chmod -R 700 "${BAMBOO_HOME}" \  
&& chown -R daemon:daemon "${BAMBOO_HOME}" \  
&& mkdir -p "${BAMBOO_INSTALL}/conf/Catalina" \  
&& curl -SL
https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-$BAMBOO_VERSION.tar.gz -o /tmp/atlassian-bamboo-$BAMBOO_VERSION.tar.gz
\  
&& tar zxvf /tmp/atlassian-bamboo-$BAMBOO_VERSION.tar.gz -C $BAMBOO_INSTALL
\--strip=1 --no-same-owner \  
&& rm /tmp/atlassian-bamboo-$BAMBOO_VERSION.tar.gz \  
&& chmod -R 700 "${BAMBOO_INSTALL}" \  
&& chown -R daemon:daemon "${BAMBOO_INSTALL}"  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
USER daemon:daemon  
  
# Expose web and agent ports  
EXPOSE 8085  
EXPOSE 54663  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["/var/atlassian/bamboo"]  
  
# Set the default working directory as the installation directory.  
WORKDIR ${BAMBOO_HOME}  
  
# Run Atlassian JIRA as a foreground process by default.  
CMD ["/opt/atlassian/bamboo/bin/start-bamboo.sh", "-fg"]  

