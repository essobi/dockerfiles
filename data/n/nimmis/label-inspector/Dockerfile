FROM alpine  
  
MAINTAINER nimmis <kjell.havneskold@gmail.com>  
  
ARG IMAGE_NAME  
ARG DOCKER_REPO  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL maintainer="nimmis <kjell.havneskold@gmail.com>" \  
org.label-schema.schema-version="build #11" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.name="docker label inspector in a container" \  
org.label-schema.url="https://www.nimmis.nu" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/nimmis/docker-label-
inspector.git"  
  
COPY /root/* /  
  
RUN apk update && apk upgrade && \  
  
# Make info file about this build  
mkdir -p /etc/BUILDS && \  
printf "Build of %s, date: %s\n" $(echo $IMAGE_NAME | sed 's#^.*io/##') `date
-u +"%Y-%m-%dT%H:%M:%SZ"` > /etc/BUILDS/$(echo $DOCKER_REPO | awk -F '/'
'{print $NF}') && \  
  
apk add python py2-pip && \  
# create /dli directory  
mkdir -p /dli && \  
  
apk add \--virtual .build-dependencies git py-pip && \  
  
# get and install dli  
git clone https://github.com/nimmis/docker-label-inspector.git && \  
cd docker-label-inspector && \  
pip install . && \  
cp example/schema.json /dli && \  
cd / && \  
rm -Rf /root/docker-label-inspector.git && \  
  
apk del .build-dependencies && \  
  
#clear cache  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

