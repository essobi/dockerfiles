FROM alpine:3.7  
  
MAINTAINER Lothar Wieske <lothar.wieske@gmail.com>  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="python-openstackclient" \  
org.label-schema.description="CloudFoundry CLI Client" \  
org.label-schema.url="https://hub.docker.com/r/lwieske/cloudfoundrycli/" \  
org.label-schema.vcs-url="https://github.com/lwieske/dockerfiles-
cloudfoundrycli.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vendor="Lothar Wieske" \  
org.label-schema.version=6.3.0 \  
org.label-schema.schema-version="1.0.0-rc1"  
  
ADD "https://cli.run.pivotal.io/stable?version=6.3.0&release=linux64-binary"
/tmp/  
  
RUN cat /tmp/stable | tar xfz - -C /usr/local/bin \  
&& rm /tmp/stable  

