FROM redis:3.2-alpine  
  
  
  
# Build arguments  
ARG BUILD_DATE  
ARG VCS_REF  
ARG NAME  
  
# Basic build-time metadata as defined at http://label-schema.org  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.name=$NAME \  
org.label-schema.url="https://github.com/egobude/docker" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/egobude/docker.git" \  
org.label-schema.vcs-type="Git"  

