FROM jenkins/jenkins:2.108-alpine  
  
MAINTAINER Basilio Vera <basilio.vera@softonic.com>  
  
ARG version="0.1.0-dev"  
ARG build_date="unknown"  
ARG commit_hash="unknown"  
ARG vcs_url="unknown"  
ARG vcs_branch="unknown"  
LABEL org.label-schema.vendor="basi" \  
org.label-schema.name="Jenkins" \  
org.label-schema.description="Jenkins with restore from backup dir option" \  
org.label-schema.usage="/README.md" \  
org.label-schema.url="https://github.com/bvis/docker-
jenkins/blob/master/README.md" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$commit_hash \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.docker.cmd.devel="" \  
org.label-schema.docker.params="DOCKER_COMPOSE_VERSION=Docker compose version
to use,\  
JENKINS_HOME_BACKUP_DIR=Where to find the backup of the jenkins data" \  
org.label-schema.build-date=$build_date  
  
ENV DOCKER_COMPOSE_VERSION="1.19.0" \  
JENKINS_HOME_BACKUP_DIR="/backup/jenkins_home"  
# if we want to install via apt  
USER root  
  
# Install dependencies  
RUN apk add --no-cache sudo \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers # Jenkins user can execute
Docker  
  
USER jenkins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
COPY jenkins-restore-backup.sh /usr/local/bin/jenkins-restore-backup.sh  
RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/plugins.txt |
tr '\n' ' ')  
#RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt \  
# && echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state  
# Auto-health check to the root page. We add such high values because of a bug
when Docker is starting the service, for Jenkins these could be acceptable.  
#HEALTHCHECK --interval=60s --timeout=5s --retries=3 \  
# CMD curl -f -A "Docker-HealthCheck/v.x
(https://docs.docker.com/engine/reference/builder/#healthcheck)"
http://localhost:8080/ || exit 1  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/jenkins-restore-backup.sh"]  

