FROM alpine:3.5  
  
ARG "version=0.1.0-dev"  
ARG "build_date=unknown"  
ARG "commit_hash=unknown"  
ARG "vcs_url=unknown"  
ARG "vcs_branch=unknown"  
  
LABEL org.label-schema.vendor="Basi" \  
org.label-schema.name="Docker-Events" \  
org.label-schema.description="Exposes in STDOUT the /events endpoint of the
docker API" \  
org.label-schema.usage="/src/README.md" \  
org.label-schema.url="https://github.com/bvis/docker-
events/blob/master/README.md" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$commit_hash \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.docker.cmd.devel="" \  
org.label-schema.docker.params="DOCKER_API_VERSION=Docker API version to use"
\  
org.label-schema.build-date=$build_date  
  
ENV "DOCKER_API_VERSION=v1.29"  
  
RUN apk add --no-cache curl  
  
ENTRYPOINT curl -sf --unix-socket /var/run/docker.sock -H "Content-Type:
application/json" -X GET http:/${DOCKER_API_VERSION}/events  

