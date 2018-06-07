FROM python:3-alpine3.6  
MAINTAINER Sylvain Desbureaux <sylvain@desbureaux.fr>  
  
ARG VCS_REF  
ARG BUILD_DATE  
  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/willthames/ansible-lint" \  
org.label-schema.url="https://github.com/willthames/ansible-lint" \  
org.label-schema.name="ansible lint" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.build-date=$BUILD_DATE  
  
WORKDIR /playbooks  
  
RUN apk add --no-cache build-base libffi-dev libressl-dev && \  
pip install ansible-lint && \  
rm -rf ~/.cache/pip && \  
apk del build-base  
  
CMD ["ansible-lint", "--version"]  

