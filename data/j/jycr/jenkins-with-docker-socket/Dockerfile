FROM jenkins/jenkins:lts-alpine  
  
ARG USER_JENKINS=jenkins  
ARG USER_ROOT=root  
ARG GROUP_DOCKER=docker  
ARG GROUP_DOCKER_GID=1001  
  
# Switch to root  
USER ${USER_ROOT}  
# Create docker group and add user jenkins to the group  
RUN addgroup -g ${GROUP_DOCKER_GID} ${GROUP_DOCKER} \  
&& addgroup ${USER_JENKINS} ${GROUP_DOCKER}  
  
ENV DOCKER_CHANNEL stable  
ENV DOCKER_VERSION 17.06.2-ce  
ENV DOCKER_ARCH x86_64  
ENV DOCKER_SHA256
a15f62533e773c40029a61784a5a1c5bc7dd21e0beb5402fda109f80e1f2994d  
  
ENV DOCKER_BUCKET download.docker.com  
  
# Install docker  
# From https://github.com/docker-
library/docker/blob/91d454d113abfb2328c88bbd48b81e495605e809/17.03/Dockerfile  
RUN set -ex; \  
apk add \--no-cache --virtual .fetch-deps \  
curl \  
tar \  
&& curl -fSL
"https://${DOCKER_BUCKET}/linux/static/${DOCKER_CHANNEL}/${DOCKER_ARCH}/docker-${DOCKER_VERSION}.tgz"
-o docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar --extract \  
\--file docker.tgz \  
\--strip-components 1 \  
\--directory /usr/local/bin/ \  
&& rm docker.tgz \  
&& apk del .fetch-deps \  
&& dockerd -v \  
&& docker -v  
  
# Add user jenkins to list of sudoers  
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Switch to user jenkins  
USER ${USER_JENKINS}  
  
COPY docker-socket.sh /  
  
ENTRYPOINT ["/docker-socket.sh"]  

