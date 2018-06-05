# VERSION 0.0.6-customAF  
# AUTHOR: Will Wong  
# DESCRIPTION: Docker airflow with ECR registry and DooD (Docker outside of
Dkr)  
# BUILD: docker build --rm -t wongwill86/air-tasks .  
# SOURCE: https://github.com/wongwill86/air-tasks  
ARG BASE_DIST=alpine  
ARG BASE_TAG=0.0.6-customAF  
ARG BASE_TEST=  
  
FROM wongwill86/air-tasks:base-${BASE_DIST}-${BASE_TAG}${BASE_TEST}  
MAINTAINER wongwill86  
  
ARG BASE_DIST  
ARG BASE_TAG  
ARG AIRFLOW_HOME=/usr/local/airflow  
ENV AIRFLOW_HOME ${AIRFLOW_HOME}  
ARG AIRFLOW_USER=airflow  
ENV AIRFLOW_USER ${AIRFLOW_USER}  
  
WORKDIR ${AIRFLOW_HOME}  
  
# Move base version information directly into airflow home directory  
RUN mkdir -p ${AIRFLOW_HOME}/version  
RUN cp -r /version ${AIRFLOW_HOME}  
  
# prepare airflow user  
RUN groupadd -r ${AIRFLOW_USER} \  
&& useradd -r -d ${AIRFLOW_HOME} -g ${AIRFLOW_USER} -s /bin/bash
${AIRFLOW_USER} \  
&& chown -R ${AIRFLOW_USER}: ${AIRFLOW_HOME} \  
&& usermod -aG docker ${AIRFLOW_USER} \  
# unfortunately this is required to update the container docker gid to match
the  
# host's gid, we remove this permission from entrypoint-dood.sh script  
&& echo "${AIRFLOW_USER} ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
# Docker config (i.e. credentials helper from base image)  
RUN cp /.docker/ .docker -r  
# Copy repo contents into docker image ( see .dockerignore to see skipped
folders )  
COPY . .  
  
# Get commit hash and tags these three files need to be excluded from
.dockerignore:  
# .git/refs/heads/  
# .git/refs/tags/  
# .git/HEAD  
RUN cat .git/refs/$(cat .git/HEAD | sed -e's/ref: refs\///g') > version/COMMIT
\  
&& grep $(cat version/COMMIT) .git/refs/tags/* -l | xargs -n 1 -r basename >
version/TAGS \  
&& mv version/COMMIT version/air-tasks.COMMIT.${BASE_DIST}-${BASE_TAG} \  
&& mv version/TAGS version/air-tasks.TAGS.${BASE_DIST}-${BASE_TAG}  
  
USER ${AIRFLOW_USER}  
WORKDIR ${AIRFLOW_HOME}  
ENTRYPOINT ["scripts/entrypoint-dood.sh"]  

