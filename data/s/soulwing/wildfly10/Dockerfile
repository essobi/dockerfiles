FROM openjdk:8-jre-alpine  
  
ARG CONFIG_DIR=/etc/wildfly/config.d/  
ARG WILDFLY_VERSION=10.1.0.Final  
ARG
WILDFLY_URL=http://search.maven.org/remotecontent?filepath=org/wildfly/wildfly-
dist/${WILDFLY_VERSION}/wildfly-dist-${WILDFLY_VERSION}.zip  
ARG S6_VERSION=v1.18.1.5-soulwing  
ARG S6_REPO=https://github.com/soulwing/s6-overlay/releases/download/  
ARG S6_URL=${S6_REPO}/${S6_VERSION}/s6-overlay-amd64.tar.gz  
ARG APPS_BASE=/apps  
ENV WILDFLY_USER=wildfly \  
WILDFLY_HOME=${APPS_BASE}/wildfly \  
WILDFLY_RUNTIME_BASE_DIR=/var/run/wildfly \  
WILDFLY_BIND_INTERFACE=eth0 \  
WILDFLY_HA=false  
  
ENV
WILDFLY_BIND_ADDRESS=${WILDFLY_RUNTIME_BASE_DIR}/configuration/bind_address  
ENV
WILDFLY_MGMT_BIND_ADDRESS=${WILDFLY_RUNTIME_BASE_DIR}/configuration/mgmt_bind_address  
  
RUN \  
apk add --no-cache --virtual build-dependencies wget ca-certificates && \  
echo "fetching s6-overlay" && \  
wget -qO /tmp/s6-overlay.tar.gz ${S6_URL} && \  
echo "fetching wildfly" && \  
wget -qO /tmp/wildfly.zip ${WILDFLY_URL} && \  
tar -zxf /tmp/s6-overlay.tar.gz -C / && \  
mkdir ${APPS_BASE} && \  
unzip -qd ${APPS_BASE} /tmp/wildfly.zip && \  
ln -s ${APPS_BASE}/wildfly-${WILDFLY_VERSION} ${WILDFLY_HOME} && \  
rm /tmp/s6-overlay.tar.gz && \  
rm /tmp/wildfly.zip && \  
echo "hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4" \  
> /etc/nsswitch.conf && \  
adduser -H -h "${WILDFLY_HOME}" -g "Wildfly User" \  
-s /bin/sh -D ${WILDFLY_USER}  
  
COPY run-wildfly.sh ${WILDFLY_HOME}/bin/run-wildfly  
COPY run-jboss-cli.sh ${WILDFLY_HOME}/bin/run-jboss-cli  
COPY cont-init.d/ /etc/cont-init.d/  
  
RUN \  
mv ${WILDFLY_HOME}/standalone ${WILDFLY_HOME}/standalone.OEM && \  
ln -s ${WILDFLY_RUNTIME_BASE_DIR} ${WILDFLY_HOME}/standalone && \  
mkdir -p $CONFIG_DIR && \  
chmod 755 ${WILDFLY_HOME}/bin/run-wildfly && \  
chmod 755 ${WILDFLY_HOME}/bin/run-jboss-cli && \  
ln -s ${WILDFLY_HOME}/bin/run-jboss-cli /usr/local/bin/cli  
  
EXPOSE 8080 9990  
ENTRYPOINT ["/init"]  
CMD ["/apps/wildfly/bin/run-wildfly"]  

