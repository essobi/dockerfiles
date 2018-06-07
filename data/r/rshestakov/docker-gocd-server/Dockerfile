FROM phusion/baseimage:0.9.18  
#FROM travix/base-debian-git-jre8:latest  
#FROM kr3ssh/debian-pam  
# install dependencies  
RUN apt-get update \  
&& apt-get install -y \  
git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& git config --global core.preloadindex true \  
&& git config --global gc.auto 256  
  
# install dependencies  
#RUN echo "deb http://http.debian.net/debian jessie-backports main" | tee
/etc/apt/sources.list.d/jessie-backports.list \  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y openjdk-7-jre-headless acl  
  
# build time environment variables  
ENV GO_VERSION=16.5.0-3305 \  
USER_NAME=go \  
USER_ID=999 \  
GROUP_NAME=go \  
GROUP_ID=999  
# install go server  
RUN groupadd -r -g $GROUP_ID $GROUP_NAME \  
&& useradd -r -g $GROUP_NAME -u $USER_ID -d /var/go $USER_NAME \  
&& curl -fSL "https://download.go.cd/binaries/$GO_VERSION/deb/go-
server-$GO_VERSION.deb" -o go-server.deb \  
&& dpkg -i go-server.deb \  
&& rm -rf go-server.db \  
&& sed -i -e "s/DAEMON=Y/DAEMON=N/" /etc/default/go-server \  
&& mkdir -p /var/lib/go-server/plugins/external \  
&& curl -fSL "https://github.com/srinivasupadhya/gocd-oauth-
login/releases/download/v1.2/google-oauth-login-1.2.jar" -o /var/lib/go-
server/plugins/external/google-oauth-login-1.2.jar  
  
# runtime environment variables  
ENV AGENT_KEY="" \  
GC_LOG="" \  
JVM_DEBUG="" \  
SERVER_MAX_MEM=1024m \  
SERVER_MAX_PERM_GEN=256m \  
SERVER_MEM=512m \  
SERVER_MIN_PERM_GEN=128m  
  
# expose ports  
EXPOSE 8153 8154  
COPY ./docker-entrypoint.sh /  
  
RUN chmod 500 /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

