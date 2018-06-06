FROM openjdk:8-jdk-alpine  
MAINTAINER Dave Chevell  
  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
# https://confluence.atlassian.com/crowd/important-directories-and-
files-78676537.html  
ENV CROWD_HOME /var/atlassian/application-data/crowd  
ENV CROWD_INSTALL_DIR /opt/atlassian/crowd  
  
VOLUME ["${CROWD_HOME}"]  
  
# Expose HTTP port  
EXPOSE 8095  
WORKDIR $CROWD_HOME  
  
CMD ["/entrypoint.sh", "-fg"]  
ENTRYPOINT ["/sbin/tini", "--"]  
  
RUN apk update -qq \  
&& update-ca-certificates \  
&& apk add ca-certificates wget curl openssh bash procps openssl perl ttf-
dejavu tini \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
ARG CROWD_VERSION=3.2.1  
ARG
DOWNLOAD_URL=https://www.atlassian.com/software/crowd/downloads/binary/atlassian-
crowd-${CROWD_VERSION}.tar.gz  
  
COPY . /tmp  
  
RUN mkdir -p ${CROWD_INSTALL_DIR} \  
&& curl -L --silent ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C
"$CROWD_INSTALL_DIR" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${CROWD_INSTALL_DIR}/ \  
&& sed -i -e 's/-Xms\\([0-9]\\+[kmg]\\)
-Xmx\\([0-9]\\+[kmg]\\)/-Xms\${JVM_MINIMUM_MEMORY:=\1}
-Xmx\${JVM_MAXIMUM_MEMORY:=\2} \${JVM_SUPPORT_RECOMMENDED_ARGS}
-Dcrowd.home=\${CROWD_HOME}/g' ${CROWD_INSTALL_DIR}/apache-
tomcat/bin/setenv.sh \  
&& sed -i -e 's/port="8095"/port="8095" secure="${catalinaConnectorSecure}"
scheme="${catalinaConnectorScheme}" proxyName="${catalinaConnectorProxyName}"
proxyPort="${catalinaConnectorProxyPort}"/' ${CROWD_INSTALL_DIR}/apache-
tomcat/conf/server.xml  

