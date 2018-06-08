FROM adenix/oracle-java:8-jre  
  
ARG CONFLUENCE_VERSION=6.7.0  
ARG
DOWNLOAD_URL=http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz  
  
ENV \  
RUN_USER=daemon \  
RUN_GROUP=daemon \  
CONFLUENCE_HOME=/var/atlassian/application-data/confluence \  
CONFLUENCE_INSTALL=/opt/atlassian/confluence  
  
WORKDIR $CONFLUENCE_INSTALL  
  
# Expose HTTP, HTTPS, and Synchrony ports  
EXPOSE 8090  
EXPOSE 8443  
EXPOSE 8091  
VOLUME ["${CONFLUENCE_HOME}"]  
  
CMD ["/docker-entrypoint.sh", "-fg"]  
  
RUN \  
mkdir -p ${CONFLUENCE_INSTALL} && \  
curl -L --silent ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C
"$CONFLUENCE_INSTALL" && \  
chown -R ${RUN_USER}:${RUN_GROUP} ${CONFLUENCE_INSTALL}/ && \  
sed -i -e 's/-Xms\\([0-9]\\+[kmg]\\)
-Xmx\\([0-9]\\+[kmg]\\)/-Xms\${JVM_MINIMUM_MEMORY:=\1}
-Xmx\${JVM_MAXIMUM_MEMORY:=\2} \${JVM_SUPPORT_RECOMMENDED_ARGS}
-Dconfluence.home=\${CONFLUENCE_HOME}/g' ${CONFLUENCE_INSTALL}/bin/setenv.sh  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY server.xml ${CONFLUENCE_INSTALL}/conf/server.xml  

