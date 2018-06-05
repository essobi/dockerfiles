FROM openjdk:8-jdk-alpine  
MAINTAINER Dave Chevell  
  
ENV RUN_USER bamboo  
ENV RUN_GROUP bamboo  
  
#
https://confluence.atlassian.com/display/BAMBOO/Locating+important+directories+and+files  
ENV BAMBOO_HOME /var/atlassian/application-data/bamboo  
ENV BAMBOO_INSTALL_DIR /opt/atlassian/bamboo  
  
VOLUME ["${BAMBOO_HOME}"]  
  
# Expose HTTP and ActiveMQ ports  
EXPOSE 8085  
EXPOSE 54663  
WORKDIR $BAMBOO_HOME  
  
CMD ["/entrypoint.sh", "-fg"]  
ENTRYPOINT ["/sbin/tini", "--"]  
  
ARG GIT_LFS_VERSION=2.2.1  
ARG GIT_LFS_DOWNLOAD_URL=https://github.com/github/git-
lfs/releases/download/v${GIT_LFS_VERSION}/git-lfs-linux-
amd64-${GIT_LFS_VERSION}.tar.gz  
  
RUN apk update -qq \  
&& update-ca-certificates \  
&& apk add ca-certificates wget curl git openssh bash procps openssl perl ttf-
dejavu tini \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/* \  
&& curl -L --silent ${GIT_LFS_DOWNLOAD_URL} | tar -xz --strip-components=1 -C
"/usr/bin" git-lfs-${GIT_LFS_VERSION}/git-lfs \  
&& addgroup -S ${RUN_GROUP} \  
&& adduser -S -G ${RUN_GROUP} ${RUN_USER}  
  
COPY entrypoint.sh /entrypoint.sh  
  
ARG BAMBOO_VERSION=6.3.4  
ARG
DOWNLOAD_URL=https://downloads.atlassian.com/software/bamboo/downloads/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz  
  
COPY . /tmp  
  
RUN mkdir -p ${BAMBOO_INSTALL_DIR} \  
&& curl -L --silent ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C
"$BAMBOO_INSTALL_DIR" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BAMBOO_INSTALL_DIR}/ \  
&& sed -i -e 's/^JVM_SUPPORT_RECOMMENDED_ARGS=""$/:
\${JVM_SUPPORT_RECOMMENDED_ARGS:=""}/g' ${BAMBOO_INSTALL_DIR}/bin/setenv.sh \  
&& sed -i -e 's/^JVM_\\(.*\\)_MEMORY="\\(.*\\)"$/: \${JVM_\1_MEMORY:=\2}/g'
${BAMBOO_INSTALL_DIR}/bin/setenv.sh \  
&& sed -i -e 's/^JAVA_OPTS="/JAVA_OPTS="${JAVA_OPTS} /g'
${BAMBOO_INSTALL_DIR}/bin/setenv.sh \  
&& sed -i -e 's/port="8085"/port="8085" secure="${catalinaConnectorSecure}"
scheme="${catalinaConnectorScheme}" proxyName="${catalinaConnectorProxyName}"
proxyPort="${catalinaConnectorProxyPort}"/'
${BAMBOO_INSTALL_DIR}/conf/server.xml  

