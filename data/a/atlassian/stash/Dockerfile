FROM java:openjdk-7-jre  
MAINTAINER Atlassian Stash Team  
  
ENV DOWNLOAD_URL
https://downloads.atlassian.com/software/stash/downloads/atlassian-stash-  
  
# https://confluence.atlassian.com/display/STASH/Stash+home+directory  
ENV STASH_HOME /var/atlassian/application-data/stash  
  
# Install git, download and extract Stash and create the required directory
layout.  
# Try to limit the number of RUN instructions to minimise the number of layers
that will need to be created.  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends git \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
# Install Atlassian Stash to the following location  
ENV STASH_INSTALL_DIR /opt/atlassian/stash  
  
ENV STASH_VERSION 3.11.4  
RUN mkdir -p ${STASH_INSTALL_DIR} \  
&& curl -L --silent ${DOWNLOAD_URL}${STASH_VERSION}.tar.gz | tar -xz --strip=1
-C "$STASH_INSTALL_DIR" \  
&& mkdir -p ${STASH_INSTALL_DIR}/conf/Catalina \  
&& chmod -R 700 ${STASH_INSTALL_DIR}/conf/Catalina \  
&& chmod -R 700 ${STASH_INSTALL_DIR}/logs \  
&& chmod -R 700 ${STASH_INSTALL_DIR}/temp \  
&& chmod -R 700 ${STASH_INSTALL_DIR}/work \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${STASH_INSTALL_DIR}/logs \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${STASH_INSTALL_DIR}/temp \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${STASH_INSTALL_DIR}/work \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${STASH_INSTALL_DIR}/conf  
  
USER ${RUN_USER}:${RUN_GROUP}  
  
VOLUME ["${STASH_INSTALL_DIR}"]  
  
# HTTP Port  
EXPOSE 7990  
# SSH Port  
EXPOSE 7999  
WORKDIR $STASH_INSTALL_DIR  
  
# Run in foreground  
CMD ["./bin/start-stash.sh", "-fg"]  

