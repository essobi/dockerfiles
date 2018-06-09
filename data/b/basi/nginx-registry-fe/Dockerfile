FROM nginx:1.13-alpine  
  
ARG "version=0.1.0-dev"  
ARG "build_date=unknown"  
ARG "commit_hash=unknown"  
ARG "vcs_url=unknown"  
ARG "vcs_branch=unknown"  
  
ENV "REGISTRY_ENDPOINT=registry:5000" \  
"SERVER_NAME=registry.local" \  
"HTPASSWD_FILE=/run/secrets/nginx.htpasswd"  
  
LABEL org.label-schema.vendor="Softonic" \  
org.label-schema.name="nginx-registry" \  
org.label-schema.description="Protects the registry with basic auth. It
should'n be used as this, it's designed to work behind a router proxy which
does the TLS strip." \  
org.label-schema.usage="/src/README.md" \  
org.label-schema.url="https://github.com/bvis/docker-nginx-registry-
fe/blob/master/README.md" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$commit_hash \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.docker.cmd.devel="" \  
org.label-schema.docker.params="REGISTRY_ENDPOINT=Registry service address,\  
SERVER_NAME=Server name used when a TLS certificate is provided,\  
HTPASSWD_FILE=Path of the htpasswd file used for provide basic auth,\  
TLS_CERT=TLS certificate file,\  
TLS_KEY=TLS Key file" \  
org.label-schema.build-date=$build_date  
  
COPY /rootfs /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

