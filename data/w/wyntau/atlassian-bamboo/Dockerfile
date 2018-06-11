FROM openjdk:8-jdk-alpine  
  
ENV RUN_USER=daemon  
ENV RUN_GROUP=daemon  
  
ENV BAMBOO_HOME=/var/atlassian/application-data/bamboo  
ENV BAMBOO_INSTALL_DIR=/opt/atlassian/bamboo  
# support set timezone  
ENV TZ=  
  
ARG BAMBOO_VERSION=6.5.0  
ARG
BAMBOO_DOWNLOAD_URL=https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz  
  
VOLUME ["${BAMBOO_HOME}"]  
WORKDIR $BAMBOO_HOME  
  
# Expose default HTTP and SSH ports.  
EXPOSE 8085 54663  
COPY entrypoint.sh /entrypoint.sh  
  
RUN apk add --no-cache curl git openssh bash ttf-dejavu tini libc6-compat
tzdata \  
&& mkdir -p ${BAMBOO_INSTALL_DIR} \  
&& curl -L --silent ${BAMBOO_DOWNLOAD_URL} | tar -xz --strip-components=1 -C
"$BAMBOO_INSTALL_DIR" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BAMBOO_INSTALL_DIR}/ \  
&& sed -i -e 's/port="8085"/port="8085" secure="${catalinaConnectorSecure}"
scheme="${catalinaConnectorScheme}" proxyName="${catalinaConnectorProxyName}"
proxyPort="${catalinaConnectorProxyPort}"/'
${BAMBOO_INSTALL_DIR}/conf/server.xml  
  
CMD ["/entrypoint.sh", "-fg"]  
ENTRYPOINT ["/sbin/tini", "--"]

