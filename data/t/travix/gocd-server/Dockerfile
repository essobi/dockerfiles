FROM alpine:3.6  
  
MAINTAINER Travix  
  
# build time environment variables  
ENV GO_VERSION=18.5.0 \  
GO_BUILD_VERSION=18.5.0-6679  
  
# install go.cd server  
RUN apk --no-cache upgrade \  
&& apk add \--no-cache \  
openjdk8-jre-base \  
git \  
bash \  
curl \  
openssh-client \  
apache2-utils \  
&& curl --retry 5 -fSL
"https://download.gocd.org/binaries/${GO_BUILD_VERSION}/generic/go-
server-${GO_BUILD_VERSION}.zip" -o /tmp/go-server.zip \  
&& unzip /tmp/go-server.zip -d / \  
&& rm /tmp/go-server.zip \  
&& mv go-server-${GO_VERSION} /var/lib/go-server \  
&& mkdir -p /var/lib/go-server/plugins/external /var/log/go-server /var/go \  
&& sed -i -e "s_root:/root_root:/var/go_" /etc/passwd \  
&& curl --retry 5 -fSL "https://github.com/gocd-contrib/google-oauth-
authorization-plugin/releases/download/2.0.0/google-oauth-authorization-
plugin-2.0.0-7.jar" -o /var/lib/go-server/plugins/external/google-oauth-
authorization-plugin-2.0.0-7.jar \  
&& curl --retry 5 -fSL "https://github.com/gocd/kubernetes-elastic-
agents/releases/download/v1.0.0/kubernetes-elastic-agent-1.0.0-94.jar" -o
/var/lib/go-server/plugins/external/kubernetes-elastic-agent-1.0.0-94.jar  
  
COPY logback-include.xml /logback-include.xml  
  
# runtime environment variables  
ENV LANG="en_US.utf8" \  
AGENT_KEY="" \  
GC_LOG="" \  
JVM_DEBUG="" \  
SERVER_MAX_MEM=1024m \  
SERVER_MAX_PERM_GEN=256m \  
SERVER_MEM=512m \  
SERVER_MIN_PERM_GEN=128m \  
GO_SERVER_PORT=8153 \  
GO_SERVER_SSL_PORT=8154 \  
GO_SERVER_SYSTEM_PROPERTIES="-Dgo.config.repo.gc.periodic=y" \  
USER_AUTH="" \  
GO_CONFIG_DIR="/etc/go"  
# expose ports  
EXPOSE 8153 8154  
  
# copy startup script  
COPY ./docker-entrypoint.sh /  
RUN chmod 500 /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

