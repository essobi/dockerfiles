FROM alpine:3.5  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL maintainer niclas@mietz.io  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.name="docker-cloudflare" \  
org.label-schema.url="https://github.com/solidnerd/docker-cloudflare/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/solidnerd/docker-cloudflare.git"
\  
org.label-schema.vcs-type="Git"  
  
RUN apk add --no-cache ca-certificates  
  
COPY flarectl /flarectl  
  
RUN chmod +x /flarectl  
  
ENTRYPOINT ["/flarectl"]  

