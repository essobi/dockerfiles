FROM alpine  
  
MAINTAINER nimmis <kjell.havneskold@gmail.com>  
  
ARG IMAGE_NAME  
ARG DOCKER_REPO  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL maintainer="nimmis <kjell.havneskold@gmail.com>" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.name="jq bundled in a container" \  
org.label-schema.url="https://www.nimmis.nu" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/nimmis/docker-jq.git"  
  
RUN apk update && apk upgrade && \  
  
# Make info file about this build  
mkdir -p /etc/BUILDS && \  
printf "Build of %s, date: %s\n" $(echo $IMAGE_NAME | sed 's#^.*io/##') `date
-u +"%Y-%m-%dT%H:%M:%SZ"` > /etc/BUILDS/$(echo $DOCKER_REPO | awk -F '/'
'{print $NF}') && \  
  
apk add jq && \  
  
#clear cache  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/jq"]  

