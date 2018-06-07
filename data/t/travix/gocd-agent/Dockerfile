FROM docker:17.09.1-ce-dind  
  
MAINTAINER Travix  
  
# build time environment variables  
ENV GO_VERSION=18.5.0 \  
GO_BUILD_VERSION=18.5.0-6679  
# install go.cd agent  
RUN apk --update-cache upgrade \  
&& apk add --update-cache \  
openjdk8-jre-base \  
git \  
bash \  
curl \  
openssh-client \  
coreutils \  
&& rm /var/cache/apk/* \  
&& curl -fSL
"https://download.gocd.io/binaries/${GO_BUILD_VERSION}/generic/go-
agent-${GO_BUILD_VERSION}.zip" -o /tmp/go-agent.zip \  
&& unzip /tmp/go-agent.zip -d / \  
&& rm /tmp/go-agent.zip \  
&& mv go-agent-${GO_VERSION} /var/lib/go-agent \  
&& mkdir -p /var/log/go-agent /var/go \  
&& sed -i -e "s_root:/root_root:/var/go_" /etc/passwd  
  
# runtime environment variables  
ENV LANG="en_US.utf8" \  
AGENT_BOOTSTRAPPER_ARGS="-sslVerificationMode NONE" \  
AGENT_ENVIRONMENTS="" \  
AGENT_HOSTNAME="" \  
AGENT_KEY="" \  
AGENT_MAX_MEM=256m \  
AGENT_MEM=128m \  
AGENT_RESOURCES="" \  
GO_SERVER_URL="https://localhost:8154/go" \  
STORAGE_DRIVER="overlay2" \  
HOME="/var/go" \  
RUN_DOCKER_DAEMON="true"  
# copy startup script  
COPY ./docker-entrypoint.sh /  
RUN chmod 500 /docker-entrypoint.sh  
  
CMD ["/docker-entrypoint.sh"]  

