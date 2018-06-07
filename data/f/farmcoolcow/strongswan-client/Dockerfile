FROM alpine  
  
ENV LABEL_MAINTAINER="Jean-Michel Ruiz (coolcow) <mail@coolcow.org>" \  
LABEL_VENDOR="coolcow.org" \  
LABEL_IMAGE_NAME="farmcoolcow/strongswan-client" \  
LABEL_URL="https://hub.docker.com/r/farmcoolcow/strongswan-client/" \  
LABEL_VCS_URL="https://github.com/farmcoolcow/docker_strongswan-client" \  
LABEL_DESCRIPTION="Very simple strongswan-client Docker image based on
alpine." \  
LABEL_LICENSE="GPL-3.0" \  
PROFILE_NAME="default" \  
LOCAL_IP="127.0.0.1" \  
WAIT_AFTER_START="10" \  
RECONNECT_IF_NOT="" \  
RECONNECT_IF_NOT_INTERVAL="10"  
RUN apk add \--no-cache --update strongswan  
  
COPY charon-logging.conf /etc/strongswan.d/charon-logging.conf  
COPY cmd.sh /cmd.sh  
  
RUN chmod +x /cmd.sh  
  
CMD /cmd.sh  
  
#  
  
ARG LABEL_VERSION="latest"  
ARG LABEL_BUILD_DATE  
ARG LABEL_VCS_REF  
  
# Build-time metadata as defined at http://label-schema.org  
LABEL maintainer=$LABEL_MAINTAINER \  
org.label-schema.build-date=$LABEL_BUILD_DATE \  
org.label-schema.description=$LABEL_DESCRIPTION \  
org.label-schema.name=$LABEL_IMAGE_NAME \  
org.label-schema.schema-version="1.0" \  
org.label-schema.url=$LABEL_URL \  
org.label-schema.license=$LABEL_LICENSE \  
org.label-schema.vcs-ref=$LABEL_VCS_REF \  
org.label-schema.vcs-url=$LABEL_VCS_URL \  
org.label-schema.vendor=$LABEL_VENDOR \  
org.label-schema.version=$LABEL_VERSION  

