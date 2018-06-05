FROM travix/base-debian-git-jre8:latest  
  
MAINTAINER Ashwanth Kumar <ashwanthkumar@googlemail.com>  
  
# build time environment variables  
ENV GO_VERSION=16.2.1-3027 \  
USER_NAME=go \  
USER_ID=999 \  
GROUP_NAME=go \  
GROUP_ID=999  
# install go agent  
RUN groupadd -r -g $GROUP_ID $GROUP_NAME \  
&& useradd -r -g $GROUP_NAME -u $USER_ID -d /var/go $USER_NAME \  
&& mkdir -p /var/lib/go-agent \  
&& mkdir -p /var/go \  
&& curl -fSL "https://download.go.cd/binaries/$GO_VERSION/deb/go-
agent-$GO_VERSION.deb " -o go-agent.deb \  
&& dpkg -i go-agent.deb \  
&& rm -rf go-agent.db \  
&& sed -i -e "s/DAEMON=Y/DAEMON=N/" /etc/default/go-agent \  
&& echo "export PATH=$PATH" | tee -a /var/go/.profile \  
&& chown -R ${USER_NAME}:${GROUP_NAME} /var/lib/go-agent \  
&& chown -R ${USER_NAME}:${GROUP_NAME} /var/go \  
&& groupmod -g 200 ssh  
  
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
CMD groupmod -g ${GROUP_ID} ${GROUP_NAME}; \  
usermod -g ${GROUP_ID} -u ${USER_ID} ${USER_NAME}; \  
if [ -n "$DOCKER_GID_ON_HOST" ]; \  
then groupadd -g $DOCKER_GID_ON_HOST docker && gpasswd -a go docker; \  
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
(/bin/su - ${USER_NAME} -c "/usr/share/go-agent/agent.sh" &); \  
while [ ! -f /var/log/go-agent/go-agent-bootstrapper.log ]; \  
do sleep 1; \  
done; \  
ps aux; \  
/bin/su - ${USER_NAME} -c "exec tail -F /var/log/go-agent/*"  

