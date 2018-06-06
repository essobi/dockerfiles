FROM anapsix/alpine-java:8u162b12_jdk  
  
MAINTAINER draca <info@draca.be>  
  
ARG CONF_VERSION=6.9.0  
ARG
CONF_DOWNLOAD=https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-6.9.0.tar.gz  
  
ENV CONF_HOME=/opt/atlassian/confluence/data  
ENV CONF_INSTALL=/opt/atlassian/confluence/install  
  
ENV RUN_USER=confluence  
ENV RUN_GROUP=confluence  
  
ENV JVM_MINIMUM_MEMORY=1024m  
ENV JVM_MAXIMUM_MEMORY=1024m  
  
EXPOSE 8090  
WORKDIR $CONF_HOME  
  
RUN apk add --no-cache curl tar shadow\  
&& groupadd -r ${RUN_GROUP} \  
&& useradd -r -g ${RUN_GROUP} ${RUN_USER} \  
&& mkdir -p "${CONF_HOME}" "${CONF_INSTALL}" \  
&& curl -Ls ${CONF_DOWNLOAD} | tar -xz --directory "${CONF_INSTALL}" \--strip-
components=1 --no-same-owner \  
&& echo -e "\nconfluence.home=${CONF_HOME}" >>
"${CONF_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties" \  
&& apk del curl tar shadow  
  
COPY "entrypoint.sh" "/"  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/opt/atlassian/confluence/install/bin/start-confluence.sh", "-fg"]

