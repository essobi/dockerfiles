FROM anapsix/alpine-java:jdk8  
  
MAINTAINER Ashwanth Kumar  
  
ENV GOCD_VERSION=16.1.0-2855 \  
USER_NAME=go \  
USER_ID=999 \  
GROUP_NAME=go \  
GROUP_ID=999 \  
JAVA_HOME=/opt/jdk  
  
RUN apk --update add unzip git openssh-client \  
&& curl -fSL https://download.go.cd/binaries/${GOCD_VERSION}/generic/go-
agent-${GOCD_VERSION}.zip -o /tmp/go-agent-${GOCD_VERSION}.zip \  
&& unzip /tmp/go-agent-${GOCD_VERSION}.zip -d /var/lib/ \  
&& mv /var/lib/go-agent* /var/lib/go-agent \  
&& ls -lah /var/lib/go-agent \  
&& mkdir -p /etc/default /var/log/go-agent \  
&& cp /var/lib/go-agent/default.cruise-agent /etc/default/go-agent \  
&& addgroup -g $GROUP_ID $GROUP_NAME \  
&& adduser -D -G $GROUP_NAME -u $USER_ID -s /bin/sh -h /var/go $USER_NAME \  
&& mkdir -p /var/go \  
&& sed -i -e "s/DAEMON=Y/DAEMON=N/" /etc/default/go-agent \  
&& chown -R ${USER_NAME}:${GROUP_NAME} /var/go \  
&& chmod +x /var/lib/go-agent/agent.sh \  
&& chown -R ${USER_NAME}:${GROUP_NAME} /var/lib/go-agent/ \  
# && echo "export JAVA_HOME=${JAVA_HOME}" | tee -a /etc/default/go-agent \  
# Add JAVA_HOME environment variable to go and root user profiles  
&& echo "export JAVA_HOME=${JAVA_HOME}" | tee -a /root/.profile \  
&& echo "export JAVA_HOME=${JAVA_HOME}" | tee -a /root/.bash_profile \  
&& echo "export JAVA_HOME=${JAVA_HOME}" | tee -a /var/go/.profile \  
&& echo "export JAVA_HOME=${JAVA_HOME}" | tee -a /var/go/.bash_profile \  
&& ln -s ${JAVA_HOME}/bin/java /usr/bin/java \  
&& ln -s ${JAVA_HOME}/bin/javac /usr/bin/javac \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
# runtime environment variables  
ENV GO_SERVER=localhost \  
GO_SERVER_PORT=8153 \  
AGENT_MEM=128m \  
AGENT_MAX_MEM=256m \  
AGENT_KEY="" \  
AGENT_RESOURCES="" \  
AGENT_GUID="" \  
AGENT_ENVIRONMENTS="" \  
AGENT_HOSTNAME="" \  
DOCKER_GID_ON_HOST=""  
# define default command  
CMD if [ -n "$DOCKER_GID_ON_HOST" ]; \  
then addgroup -g $DOCKER_GID_ON_HOST docker && addgroup go docker; \  
fi; \  
chown -R ${USER_NAME}:${GROUP_NAME} /var/lib/go-agent /var/go /var/log/go-
agent; \  
sed -i -e "s/GO_SERVER=127.0.0.1/GO_SERVER=${GO_SERVER}/" /etc/default/go-
agent; \  
sed -i -e "s/GO_SERVER_PORT=8153/GO_SERVER_PORT=${GO_SERVER_PORT}/"
/etc/default/go-agent; \  
if [ -n "$AGENT_KEY" ]; \  
then echo "agent.auto.register.key=$AGENT_KEY" > /var/lib/go-
agent/config/autoregister.properties; \  
fi; \  
if [ -n "$AGENT_RESOURCES" ]; \  
then echo "agent.auto.register.resources=$AGENT_RESOURCES" >> /var/lib/go-
agent/config/autoregister.properties; \  
fi; \  
if [ -n "$AGENT_ENVIRONMENTS" ]; \  
then echo "agent.auto.register.environments=$AGENT_ENVIRONMENTS" >>
/var/lib/go-agent/config/autoregister.properties; \  
fi; \  
if [ -n "$AGENT_HOSTNAME" ]; \  
then echo "agent.auto.register.hostname=$AGENT_HOSTNAME" >> /var/lib/go-
agent/config/autoregister.properties; \  
fi; \  
if [ -n "$AGENT_GUID" ]; \  
then echo "$AGENT_GUID" > /var/lib/go-agent/config/guid.txt; \  
fi; \  
until curl -s -o /dev/null "http://${GO_SERVER}:${GO_SERVER_PORT}"; \  
do sleep 5; \  
echo "Waiting for http://${GO_SERVER}:${GO_SERVER_PORT}"; \  
done; \  
(/bin/su -m - ${USER_NAME} -c "/var/lib/go-agent/agent.sh" &); \  
while [ ! -f /var/log/go-agent/go-agent-bootstrapper.log ]; \  
do sleep 1; \  
done; \  
ps aux; \  
/bin/su - ${USER_NAME} -c "exec tail -F /var/log/go-agent/*"  

