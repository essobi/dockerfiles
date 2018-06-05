#
-------------------------------------------------------------------------------------------------------------------------  
#  
# ATLASSIAN BITBUCKET STANDALONE SERVER  
#  
# Thanks to original project example :
https://github.com/cptactionhank/docker-atlassian-stash  
#  
# @see https://www.atlassian.com/software/bitbucket/download  
# @see https://confluence.atlassian.com/bitbucketserver/install-bitbucket-
server-from-an-archive-file-776640148.html  
# @see https://confluence.atlassian.com/bitbucketserver/connecting-bitbucket-
server-to-an-external-database-776640378.html  
# @see https://confluence.atlassian.com/bitbucketserver/connecting-bitbucket-
server-to-postgresql-776640389.html  
# @see https://jdbc.postgresql.org/download.html  
# @see https://confluence.atlassian.com/bitbucketserver/supported-
platforms-776640981.html  
# @see http://www.cyberciti.biz/faq/linux-unix-extracting-specific-files  
#  
#
-------------------------------------------------------------------------------------------------------------------------  
# Base image  
FROM airdock/oracle-jdk:1.8  
# Maintainer  
MAINTAINER alban.montaigu@gmail.com  
  
  
# Configuration variables.  
ENV DEBIAN_FRONTEND="noninteractive" \  
BITBUCKET_HOME="/var/local/atlassian/bitbucket" \  
BITBUCKET_INSTALL="/usr/local/atlassian/bitbucket" \  
BITBUCKET_VERSION="4.12.1"  
# Base system update (isolated to not reproduce each time)  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1 git-
core xmlstarlet wget \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
# Install Atlassian bitbucket and helper tools and setup initial home  
# directory structure (isolated to not reproduce each time).  
RUN set -x \  
&& mkdir -p "${BITBUCKET_HOME}" \  
&& chmod -R 700 "${BITBUCKET_HOME}" \  
&& chown -R daemon:daemon "${BITBUCKET_HOME}" \  
&& mkdir -p "${BITBUCKET_INSTALL}/conf/Catalina" \  
&& wget -P /tmp --no-check-certificate
"https://downloads.atlassian.com/software/stash/downloads/atlassian-
bitbucket-${BITBUCKET_VERSION}.tar.gz" -nv \  
&& tar xz -f "/tmp/atlassian-bitbucket-${BITBUCKET_VERSION}.tar.gz"
\--directory "${BITBUCKET_INSTALL}" \--strip-components=1 --no-same-owner \  
&& rm -rf "/tmp/atlassian-bitbucket-${BITBUCKET_VERSION}.tar.gz" \  
&& chmod -R 700 "${BITBUCKET_INSTALL}/conf" \  
&& chmod -R 700 "${BITBUCKET_INSTALL}/logs" \  
&& chmod -R 700 "${BITBUCKET_INSTALL}/temp" \  
&& chmod -R 700 "${BITBUCKET_INSTALL}/work" \  
&& chown -R daemon:daemon "${BITBUCKET_INSTALL}/conf" \  
&& chown -R daemon:daemon "${BITBUCKET_INSTALL}/logs" \  
&& chown -R daemon:daemon "${BITBUCKET_INSTALL}/temp" \  
&& chown -R daemon:daemon "${BITBUCKET_INSTALL}/work"  
  
# Custom bitbucket configuration (isolated to not reproduce each time)  
RUN set -x \  
&& ln --symbolic "/usr/lib/x86_64-linux-gnu/libtcnative-1.so"
"${BITBUCKET_INSTALL}/lib/native/libtcnative-1.so" \  
&& sed --in-place 's/^# umask 0027$/umask 0027/g'
"${BITBUCKET_INSTALL}/bin/setenv.sh" \  
&& xmlstarlet ed --inplace \  
\--delete "Server/Service/Engine/Host/@xmlValidation" \  
\--delete "Server/Service/Engine/Host/@xmlNamespaceAware" \  
"${BITBUCKET_INSTALL}/conf/server.xml"  
  
# PostgreSQL connector for bitbucket (isolated to not reproduce each time)  
RUN set -x \  
&& wget -P "${BITBUCKET_INSTALL}/lib/postgresql-9.4-1202.jdbc41.jar" \--no-
check-certificate
"https://jdbc.postgresql.org/download/postgresql-9.4-1202.jdbc41.jar" -nv  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
USER daemon:daemon  
  
  
# Expose default HTTP connector port + SSH Port  
EXPOSE 7990 7999  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["/var/local/atlassian/bitbucket"]  
  
# Set the default working directory as the installation directory.  
WORKDIR ${BITBUCKET_INSTALL}  
  
# Run Atlassian bitbucket as a foreground process by default.  
CMD ["./bin/start-bitbucket.sh", "-fg"]  

