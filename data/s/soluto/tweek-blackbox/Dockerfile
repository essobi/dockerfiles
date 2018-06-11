FROM docker/compose:1.16.1  
  
RUN apk update && apk add git openssh-client wget  
COPY ./blackbox /blackbox  
COPY ./scripts /scripts  
COPY ./keys/ssh /root/.ssh  
  
ENV GIT_PORT=4001 \  
API_PORT=4003 \  
AUTHORING_PORT=4005 \  
EDITOR_PORT=4004 \  
PUBLISHING_SSH_PORT=4009 \  
MINIO_PORT=4007 \  
PUBLISHING_VERSION=latest \  
API_VERSION=latest \  
AUTHORING_VERSION=latest \  
EDITOR_VERSION=latest \  
PROJECT_NAME=blackbox  
  
RUN chmod 600 /root/.ssh/id_rsa  
  
WORKDIR /blackbox  
  
HEALTHCHECK \--interval=5s \--timeout=1s \--retries=10 CMD ls /tmp/ready  
  
ENTRYPOINT [ "/bin/sh", "/scripts/entrypoint.sh" ]  

