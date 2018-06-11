FROM alpine:3.7  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://bitbucket.org/yusufhm/reins" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="0.1.0"  
RUN addgroup -g 1000 user && \  
adduser -u 1000 -G user -D user && \  
apk add \--no-cache \  
ansible curl openssh-client python  
  
USER user  

