FROM farmcoolcow/rclone  
  
ENV LABEL_MAINTAINER="Jean-Michel Ruiz (coolcow) <mail@coolcow.org>" \  
LABEL_VENDOR="coolcow.org" \  
LABEL_IMAGE_NAME="farmcoolcow/rclone-cron" \  
LABEL_URL="https://hub.docker.com/r/farmcoolcow/rclone-cron/" \  
LABEL_VCS_URL="https://github.com/farmcoolcow/docker_rclone-cron" \  
LABEL_DESCRIPTION="Docker farmcoolcow/rclone image using crond as default
entrypoint." \  
LABEL_LICENSE="GPL-3.0" \  
ENTRYPOINT_USER=rclone \  
ENTRYPOINT_GROUP=rclone \  
ENTRYPOINT_HOME=/home \  
CROND_CRONTAB=/crontab  
  
# creating empty crontab  
RUN touch $CROND_CRONTAB  
  
ENTRYPOINT ["/entrypoint_crond.sh"]  
  
CMD ["-f"]  
  
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

