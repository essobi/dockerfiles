FROM alpine:3.6  
ENV MATTERMOST_VERSION="4.0.4" \  
MATTERMOST_BASE_DIR="/opt/mattermost" \  
\  
MM_SERVICESETTINGS_LISTENADDRESS=":80" \  
MM_LOGSETTINGS_CONSOLE_LEVEL="INFO" \  
MM_LOGSETTINGS_ENABLEFILE="false" \  
MM_PASSWORDSETTINGS_MINIMUMLENGTH="12"  
ENV MATTERMOST_DATA_DIR="${MATTERMOST_BASE_DIR}/data" \  
MATTERMOST_CONF_DIR="${MATTERMOST_BASE_DIR}/config" \  
PATH="${PATH}:${MATTERMOST_BASE_DIR}/mattermost/bin"  
RUN apk add --no-cache \  
bash ca-certificates gettext mysql-client postgresql-client tini \  
\  
&& export GOPATH=/opt/go \  
&& MATTERMOST_BUILD_PATH=${GOPATH}/src/github.com/mattermost \  
&& apk --no-cache add --virtual .builddeps curl g++ go git mercurial make
nodejs-current-npm \  
&& go get github.com/tools/godep \  
&& npm update npm --global \  
&& mkdir -p ${GOPATH} \  
&& git clone -q -b v${MATTERMOST_VERSION} \--depth 1 \  
https://github.com/mattermost/platform.git \  
${MATTERMOST_BUILD_PATH}/platform \  
&& cd ${MATTERMOST_BUILD_PATH}/platform \  
&& sed -i.org 's/sudo //g' Makefile \  
&& make build-linux BUILD_NUMBER=${MATTERMOST_VERSION} \  
\  
&& mkdir ${MATTERMOST_BASE_DIR} && cd ${MATTERMOST_BASE_DIR} \  
&& curl -sSL https://releases.mattermost.com/${MATTERMOST_VERSION}/mattermost-
team-${MATTERMOST_VERSION}-linux-amd64.tar.gz | tar -xvz \  
&& mv ${GOPATH}/bin/platform ./mattermost/bin/platform \  
\  
&& apk del .builddeps \  
&& rm -rf ${GOPATH} /tmp/* /root/* /root/.[!.]* /usr/lib/go/pkg
/usr/lib/node_modules  
  
COPY entrypoint.sh /  
  
EXPOSE 80/tcp  
VOLUME ["${MATTERMOST_DATA_DIR}"]  
WORKDIR ${MATTERMOST_BASE_DIR}/mattermost  
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]  
CMD ["server"]  

