FROM codenvy/debian_jdk8_node  
  
# install docker in addition to existing stuff  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.11.0  
RUN set -x \  
&& sudo bash -c "wget -qO-
https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz | tar
xvz -C /opt/" && sudo mv /opt/docker/* /usr/bin/  

