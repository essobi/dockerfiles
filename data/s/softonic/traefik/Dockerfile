FROM traefik:1.3-alpine  
  
ARG "version=0.1.0-dev"  
ARG "build_date=unknown"  
ARG "commit_hash=unknown"  
ARG "vcs_url=unknown"  
ARG "vcs_branch=unknown"  
  
LABEL org.label-schema.vendor="Softonic" \  
org.label-schema.name="traefik" \  
org.label-schema.description="Traefik instance with self-healing based on
HEALTHCHECK command" \  
org.label-schema.usage="/src/README.md" \  
org.label-schema.url="https://github.com/softonic/docker-
traefik/blob/master/README.md" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$commit_hash \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.docker.cmd.devel="" \  
org.label-schema.build-date=$build_date  
  
RUN apk add --no-cache curl  
  
HEALTHCHECK --interval=10s \--timeout=2s \--retries=3 \  
CMD curl -I -k --:connect-timeout 2 \--resolve foo-bar.com:443:127.0.0.1
https://foo-bar.com/ || exit 1  

