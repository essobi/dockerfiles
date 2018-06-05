FROM java:8  
# Setup useful environment variables  
ENV STASH_HOME /var/atlassian/stash  
ENV STASH_INSTALL /opt/atlassian/stash  
ENV STASH_VERSION 3.11.6  
# Install Atlassian Stash and helper tools and setup initial home  
# directory structure.  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1 git-
core xmlstarlet \  
&& apt-get clean \  
&& mkdir -p "${STASH_HOME}/lib" \  
&& chmod -R 700 "${STASH_HOME}" \  
&& chown -R daemon:daemon "${STASH_HOME}" \  
&& mkdir -p "${STASH_INSTALL}" \  
&& curl -Ls
"http://www.atlassian.com/software/stash/downloads/binary/atlassian-
stash-${STASH_VERSION}.tar.gz" | tar -zx --directory "${STASH_INSTALL}"
\--strip-components=1 --no-same-owner \  
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.36.tar.gz" | tar -xz --directory "${STASH_INSTALL}/lib" \--strip-
components=1 --no-same-owner "mysql-connector-java-5.1.36/mysql-connector-
java-5.1.36-bin.jar" \  
&& chmod -R 700 "${STASH_INSTALL}/conf" \  
&& chmod -R 700 "${STASH_INSTALL}/logs" \  
&& chmod -R 700 "${STASH_INSTALL}/temp" \  
&& chmod -R 700 "${STASH_INSTALL}/work" \  
&& chown -R daemon:daemon "${STASH_INSTALL}/conf" \  
&& chown -R daemon:daemon "${STASH_INSTALL}/logs" \  
&& chown -R daemon:daemon "${STASH_INSTALL}/temp" \  
&& chown -R daemon:daemon "${STASH_INSTALL}/work" \  
&& ln --symbolic "/usr/lib/x86_64-linux-gnu/libtcnative-1.so"
"${STASH_INSTALL}/lib/native/libtcnative-1.so" \  
&& sed --in-place 's/^# umask 0027$/umask 0027/g'
"${STASH_INSTALL}/bin/setenv.sh" \  
&& xmlstarlet ed --inplace \  
\--delete "Server/Service/Engine/Host/@xmlValidation" \  
\--delete "Server/Service/Engine/Host/@xmlNamespaceAware" \  
"${STASH_INSTALL}/conf/server.xml"  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
USER daemon:daemon  
  
# Expose default HTTP and SSH ports.  
EXPOSE 7990 7999  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs.  
VOLUME ["/var/atlassian/stash"]  
  
# Set the default working directory as the Stash home directory.  
WORKDIR ${STASH_HOME}  
  
# Run Atlassian Stash as a foreground process by default.  
CMD ["/opt/atlassian/stash/bin/catalina.sh", "run"]  

