FROM docker:17.05  
  
MAINTAINER Viktor Farcic <viktor@farcic.com>  
MAINTAINER Martin Ahrer <martin.ahrer@software-craftsmen.at>  
  
ARG "version=0.1.0-dev"  
ARG "build_date=unknown"  
ARG "commit_hash=unknown"  
ARG "vcs_url=unknown"  
ARG "vcs_branch=unknown"  
  
LABEL org.label-schema.vendor="Software Craftsmen Gmbh & Co KG" \  
org.label-schema.name="jenkins-swarm-agent" \  
org.label-schema.description="Jenkins agent based on the Swarm plugin" \  
org.label-schema.usage="${vcs_url}/blob/master/README.md" \  
org.label-schema.url="${vcs_url}/blob/master/README.md" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$vcs_ref \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$build_date  
  
ENV "SWARM_CLIENT_VERSION=3.3" \  
"DOCKER_COMPOSE_VERSION=1.13.0" \  
"COMMAND_OPTIONS=" \  
"USER_NAME_SECRET=" \  
"PASSWORD_SECRET="  
  
RUN adduser -G root -D jenkins \  
&& apk --update --no-cache add ca-certificates wget && update-ca-certificates
\  
&& apk add openjdk8-jre python py-pip git openssh bash \  
&& wget -q https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/${SWARM_CLIENT_VERSION}/swarm-client-${SWARM_CLIENT_VERSION}.jar -P
/home/jenkins/ \  
&& pip install docker-compose  
  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  

