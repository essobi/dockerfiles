FROM python:alpine  
  
LABEL org.label-schema.vcs-url="https://github.com/kfsq/gitlab-ci-docker" \  
org.label-schema.vendor="Docker images for use with GitLab CI" \  
maintainer="Kristoffer Winther Balling <kfsq@novonordisk.com>"  
RUN apk update \  
&& apk add \--no-cache make \  
&& pip install sphinx sphinx_rtd_theme  

