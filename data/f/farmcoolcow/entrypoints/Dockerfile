FROM alpine  
  
ENV LABEL_MAINTAINER="Jean-Michel Ruiz (coolcow) <mail@coolcow.org>" \  
LABEL_VENDOR="coolcow.org" \  
LABEL_IMAGE_NAME="farmcoolcow/entrypoints" \  
LABEL_URL="https://hub.docker.com/r/farmcoolcow/entrypoints/" \  
LABEL_VCS_URL="https://github.com/farmcoolcow/docker_entrypoints" \  
LABEL_DESCRIPTION="Docker base image with su-exec and crond entrypoint
scripts, based on alpine." \  
LABEL_LICENSE="GPL-3.0"  
# Install shadow (for usermod and groupmod) and su-exec  
RUN apk --no-cache --update add \  
shadow \  
su-exec  
  
COPY create_user_group_home.sh \  
entrypoint_su-exec.sh \  
entrypoint_crond.sh \  
/  
  
RUN chmod +x \  
/create_user_group_home.sh \  
/entrypoint_su-exec.sh \  
/entrypoint_crond.sh  
  
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

