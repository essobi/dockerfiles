FROM phusion/baseimage:latest  
# Initially was based on work of Alessandro Viganò AND Andreas Löffler
<andy@x86dev.com>  
# Almost entierly rewrote by Abdelrani Djelaili <strator.adj@gmail.com>  
MAINTAINER Gissehel <public-dev-github-docker-seafile@gissehel.org>  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Seafile server" \  
org.label-schema.description="A simple to use seafile server" \  
org.label-schema.license="MIT" \  
org.label-schema.vendor="strator-dev" \  
org.label-schema.url="https://github.com/strator-dev/docker-seafile" \  
org.label-schema.vcs-url="https://github.com/strator-dev/docker-seafile" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0-rc.1"  
  
RUN apt-get update  
ADD files /tmp/files  
RUN chmod 755 /tmp/files/build-script.sh  
RUN /tmp/files/build-script.sh  
  
expose 8080  

