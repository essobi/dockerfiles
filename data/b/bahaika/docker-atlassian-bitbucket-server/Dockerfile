FROM java:openjdk-8-jre  
MAINTAINER Atlassian Bitbucket Server Team  
  
# Install git, download and extract Bitbucket Server and create the required
directory layout.  
# Try to limit the number of RUN instructions to minimise the number of layers
that will need to be created.  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends git libtcnative-1 \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
#
https://confluence.atlassian.com/display/BitbucketServer/Bitbucket+Server+home+directory  
ENV BITBUCKET_HOME /var/atlassian/application-data/bitbucket  
  
# Install Atlassian Bitbucket Server to the following location  
ENV BITBUCKET_INSTALL_DIR /opt/atlassian/bitbucket  
  
ENV BITBUCKET_VERSION 4.4.1  
ENV DOWNLOAD_URL
https://downloads.atlassian.com/software/stash/downloads/atlassian-
bitbucket-${BITBUCKET_VERSION}.tar.gz  
  
RUN mkdir -p ${BITBUCKET_INSTALL_DIR} \  
&& curl -L --silent ${DOWNLOAD_URL} | tar -xz --strip=1 -C
"$BITBUCKET_INSTALL_DIR" \  
&& mkdir -p ${BITBUCKET_INSTALL_DIR}/conf/Catalina \  
&& chmod -R 700 ${BITBUCKET_INSTALL_DIR}/conf/Catalina \  
&& chmod -R 700 ${BITBUCKET_INSTALL_DIR}/logs \  
&& chmod -R 700 ${BITBUCKET_INSTALL_DIR}/temp \  
&& chmod -R 700 ${BITBUCKET_INSTALL_DIR}/work \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BITBUCKET_INSTALL_DIR}/ \  
&& ln --symbolic "/usr/lib/x86_64-linux-gnu/libtcnative-1.so"
"${BITBUCKET_INSTALL_DIR}/lib/native/libtcnative-1.so"  
  
USER ${RUN_USER}:${RUN_GROUP}  
  
VOLUME ["${BITBUCKET_HOME}"]  
  
# HTTP Port  
EXPOSE 7990  
# SSH Port  
EXPOSE 7999  
WORKDIR $BITBUCKET_INSTALL_DIR  
  
# Run in foreground  
CMD ["./bin/start-bitbucket.sh", "-fg"]  

