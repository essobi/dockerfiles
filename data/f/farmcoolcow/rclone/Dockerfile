FROM farmcoolcow/entrypoints  
  
ENV LABEL_MAINTAINER="Jean-Michel Ruiz (coolcow) <mail@coolcow.org>" \  
LABEL_VENDOR="coolcow.org" \  
LABEL_IMAGE_NAME="farmcoolcow/rclone" \  
LABEL_URL="https://hub.docker.com/r/farmcoolcow/rclone/" \  
LABEL_VCS_URL="https://github.com/farmcoolcow/docker_rclone" \  
LABEL_DESCRIPTION="Simple rclone Docker image based on alpine." \  
LABEL_LICENSE="GPL-3.0" \  
ARCH=amd64 \  
RCLONE_VERSION=current \  
RCLONE_DOWNLOAD=http://downloads.rclone.org \  
ENTRYPOINT_USER=rclone \  
ENTRYPOINT_GROUP=rclone \  
ENTRYPOINT_HOME=/home  
  
# install rclone  
RUN apk --no-cache --update add \  
ca-certificates \  
fuse \  
openssl \  
&& cd /tmp \  
&& wget -q ${RCLONE_DOWNLOAD}/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip \  
&& unzip /tmp/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip \  
&& mv /tmp/rclone-*-linux-${ARCH}/rclone /usr/bin \  
&& rm -r /tmp/rclone-*-linux-${ARCH}/  
  
  
VOLUME $ENTRYPOINT_HOME  
  
WORKDIR $ENTRYPOINT_HOME  
  
ENTRYPOINT ["/entrypoint_su-exec.sh", "rclone"]  
  
CMD ["--help"]  
  
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

