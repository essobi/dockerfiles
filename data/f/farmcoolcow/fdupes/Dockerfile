FROM farmcoolcow/entrypoints  
  
ENV LABEL_MAINTAINER="Jean-Michel Ruiz (coolcow) <mail@coolcow.org>" \  
LABEL_VENDOR="coolcow.org" \  
LABEL_IMAGE_NAME="farmcoolcow/fdupes" \  
LABEL_URL="https://hub.docker.com/r/farmcoolcow/fdupes/" \  
LABEL_VCS_URL="https://github.com/farmcoolcow/docker_fdupes" \  
LABEL_DESCRIPTION="Simple fdupes Docker image based on alpine." \  
LABEL_LICENSE="GPL-3.0" \  
FDUPES_GIT=https://github.com/adrianlopezroche/fdupes.git \  
ENTRYPOINT_USER="fdupes" \  
ENTRYPOINT_GROUP="fdupes" \  
ENTRYPOINT_HOME="/data"  
RUN apk --no-cache --update add \  
alpine-sdk \  
git \  
&& git clone ${FDUPES_GIT} /tmp/fdupes \  
&& cd /tmp/fdupes \  
&& make fdupes \  
&& make install \  
&& cd \  
&& rm -rf /tmp/fdupes \  
&& apk --no-cache del \  
alpine-sdk \  
git  
  
WORKDIR $ENTRYPOINT_HOME  
  
ENTRYPOINT ["/entrypoint_su-exec.sh", "fdupes"]  
  
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

