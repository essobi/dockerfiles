FROM openjdk:8-jdk-alpine  
  
ENV BAMBOO_AGENT_HOME=/var/atlassian/application-data/bamboo-agent  
ENV BAMBOO_AGENT_INSTALL_DIR=/opt/atlassian/bamboo-agent  
  
ENV RUN_USER=daemon  
ENV RUN_GROUP=daemon  
  
# support set timezone, default GMT timezone  
ENV TZ=  
  
VOLUME ["${BAMBOO_AGENT_HOME}"]  
WORKDIR $BAMBOO_AGENT_INSTALL_DIR  
  
COPY ./bamboo-capabilities.properties ${BAMBOO_AGENT_INSTALL_DIR}/  
COPY ./bamboo-capabilities.shared.properties ${BAMBOO_AGENT_INSTALL_DIR}/  
COPY ./entrypoint.sh /entrypoint.sh  
  
ONBUILD COPY ./bamboo-capabilities.properties ${BAMBOO_AGENT_INSTALL_DIR}/  
  
ARG GLIBC_VERSION=2.27-r0  
ARG GLIBC_APK=glibc-${GLIBC_VERSION}.apk  
ARG GLIBC_DOWNLOAD_URL=https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/${GLIBC_APK}  
  
ARG BAMBOO_VERSION=6.5.0  
ARG
BAMBOO_AGENT_DOWNLOAD_URL=https://downloads.atlassian.com/software/bamboo/downloads/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz  
ENV BAMBOO_AGENT_JAR=atlassian-bamboo-agent-installer-${BAMBOO_VERSION}.jar  
ARG BAMBOO_AGENT_JAR_TARGZ_PATH=atlassian-bamboo-${BAMBOO_VERSION}/atlassian-
bamboo/admin/agent/${BAMBOO_AGENT_JAR}  
  
RUN apk update -qq \  
&& apk add --no-cache ca-certificates openssl wget curl git openssh bash ttf-
dejavu tini tzdata \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget ${GLIBC_DOWNLOAD_URL} \  
&& apk add ${GLIBC_APK} \  
&& rm ${GLIBC_APK} \  
&& mkdir -p ${BAMBOO_AGENT_INSTALL_DIR} \  
&& curl -L --silent ${BAMBOO_AGENT_DOWNLOAD_URL} | tar -xz -C
${BAMBOO_AGENT_INSTALL_DIR} \--strip-components=4
${BAMBOO_AGENT_JAR_TARGZ_PATH} \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BAMBOO_AGENT_INSTALL_DIR}  
  
CMD ["/entrypoint.sh", "console"]  
ENTRYPOINT ["/sbin/tini", "--"]

