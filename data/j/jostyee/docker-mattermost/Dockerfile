FROM frolvlad/alpine-glibc:alpine-3.7  
LABEL maintainer="jostyee <hi@josta.me>"  
  
ENV MATTERMOST_VERSION=4.10.0 \  
MATTERMOST_HOME="/opt/mattermost"  
ENV MATTERMOST_DATA_DIR="${MATTERMOST_HOME}/data" \  
MATTERMOST_BUILD_DIR="${MATTERMOST_HOME}/build" \  
MATTERMOST_RUNTIME_DIR="${MATTERMOST_HOME}/runtime" \  
MATTERMOST_CONF_DIR="${MATTERMOST_HOME}/config"  
COPY assets/runtime/ ${MATTERMOST_RUNTIME_DIR}/  
COPY entrypoint.sh /sbin/entrypoint.sh  
  
RUN apk --no-cache add bash gettext curl \  
mysql-client postgresql-client \  
ca-certificates \  
&& cd /opt \  
&& curl
https://releases.mattermost.com/${MATTERMOST_VERSION}/mattermost-${MATTERMOST_VERSION}-linux-
amd64.tar.gz | tar -xz \  
&& chmod 755 /sbin/entrypoint.sh \  
&& apk del curl  
  
EXPOSE 80/tcp  
  
VOLUME ["${MATTERMOST_DATA_DIR}"]  
WORKDIR ${MATTERMOST_HOME}  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["app:start"]  

