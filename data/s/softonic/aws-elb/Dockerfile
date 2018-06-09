FROM python:2.7-alpine3.6  
  
ARG "version=0.1.0-dev"  
ARG "build_date=unknown"  
ARG "commit_hash=unknown"  
ARG "vcs_url=unknown"  
ARG "vcs_branch=unknown"  
  
ENV DOCKER_API_VERSION="v1.30" \  
AWS_ELB_NAMES=""  
  
LABEL org.label-schema.vendor="Softonic" \  
org.label-schema.name="aws-elb-autoconfigure" \  
org.label-schema.description="Autoregisters the nodes in a swarm cluster in a
predefined set of ELBs" \  
org.label-schema.usage="/src/README.md" \  
org.label-schema.url="https://github.com/softonic/docker-aws-
cli/blob/master/README.md" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$commit_hash \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.docker.cmd.devel="" \  
org.label-schema.docker.params="AWS_ELB_NAMES=ELB names to
configure,DOCKER_API_VERSION=API version to use" \  
org.label-schema.build-date=$build_date  
  
COPY rootfs /  
  
RUN pip install awscli && apk add --no-cache curl jq  
  
CMD ["/autoregister.sh"]  

