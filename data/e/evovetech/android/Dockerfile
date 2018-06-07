ARG DOCKER_REPO=evovetech/android  
ARG GRADLE_VERSION=gradle-4.1  
FROM ${DOCKER_REPO}:base.${GRADLE_VERSION}  
  
WORKDIR ${HOME}  
COPY tools/entrypoint.sh ./entrypoint.sh  
ENTRYPOINT ["./entrypoint.sh"]  
  
# microbadger - ref  
ARG GIT_REF  
ARG DOCKER_CMD  
LABEL org.label-schema.vcs-ref="${GIT_REF}" \  
org.label-schema.docker.cmd="${DOCKER_CMD}"  

