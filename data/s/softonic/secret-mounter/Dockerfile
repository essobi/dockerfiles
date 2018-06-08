FROM alpine:3.5  
  
ARG "version=0.1.0-dev"  
ARG "build_date=unknown"  
ARG "commit_hash=unknown"  
ARG "vcs_url=unknown"  
ARG "vcs_branch=unknown"  
  
LABEL org.label-schema.vendor="Softonic" \  
org.label-schema.name="Secret Mounter" \  
org.label-schema.description="Mounts the specified secrets in a predefined
folder that should be mounted as a volume" \  
org.label-schema.usage="/src/README.md" \  
org.label-schema.url="https://github.com/bvis/docker-secret-
mounter/blob/master/README.md" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$commit_hash \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.docker.cmd.devel="" \  
org.label-schema.docker.params="PROJECT=Project Name,\  
ENVIRONMENT=Environment name (staging, production, etc)" \  
org.label-schema.build-date=$build_date  
  
RUN apk add --no-cache git openssh  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  
#ENTRYPOINT socat -d -d TCP-L:$OUT,fork TCP:$IN  

