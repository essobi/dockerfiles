FROM gissehel/dev:latest  
MAINTAINER Gissehel <public-docker-dev-dl-maintainer@gissehel.org>  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.name=dev-dl \  
org.label-schema.version=1.09-$VCS_REF \  
org.label-schema.vendor=gissehel \  
org.label-schema.vcs-url="https://github.com/gissehel/docker-gissehel-images"
\  
org.label-schema.schema-version="1.0"  
ADD script.sh /tmp/create-image-script  
RUN /bin/bash /tmp/create-image-script && rm -f /tmp/create-image-script  

