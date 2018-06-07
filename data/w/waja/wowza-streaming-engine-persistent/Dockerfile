FROM wowzamedia/wowza-streaming-engine-linux  
  
# Dockerfile Maintainer  
MAINTAINER Jan Wagner "waja@cyconet.org"  
  
ARG "BUILD_DATE=unknown"  
ARG "BUILD_VERSION=unknown"  
ARG "VCS_URL=unknown"  
ARG "VCS_REF=unknown"  
ARG "VCS_BRANCH=unknown"  
  
# See http://label-schema.org/rc1/ and https://microbadger.com/labels  
LABEL org.label-schema.name="Wowza - Wowza Live Streaming Server" \  
org.label-schema.description="Wowza Live Streaming Server (with persistence)"
\  
org.label-schema.vendor="Cyconet" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$BUILD_VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-branch=$VCS_BRANCH  
  
ENV WSE_DATA_DIR=/var/lib/wowza  
ENV WSE_LOG_DIR=/var/log/wowza  
  
COPY install.sh persistent_config.sh /usr/local/sbin/  
RUN bash /usr/local/sbin/install.sh  

