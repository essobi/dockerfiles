FROM alpine:3.7  
# Dockerfile Maintainer  
MAINTAINER Jan Wagner "waja@cyconet.org"  
ARG "BUILD_DATE=unknown"  
ARG "BUILD_VERSION=unknown"  
ARG "VCS_URL=unknown"  
ARG "VCS_REF=unknown"  
ARG "VCS_BRANCH=unknown"  
# See http://label-schema.org/rc1/ and https://microbadger.com/labels  
LABEL org.label-schema.name="nscan - fast internet-wide scanner" \  
org.label-schema.description="Fast Network scanner optimized for internet-wide
scanning purposes on Alpine Linux based container" \  
org.label-schema.vendor="Cyconet" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$BUILD_VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-branch=$VCS_BRANCH  
  
RUN apk --no-cache update && apk --no-cache upgrade && \  
apk --no-cache add python && \  
apk --no-cache add --virtual build-dependencies git && \  
git clone https://github.com/OffensivePython/Nscan /usr/local/nscan && \  
chmod +x /usr/local/nscan/latest/nscan.py && \  
ln -s /usr/local/nscan/latest/nscan.py /usr/local/bin/nscan && \  
apk del build-dependencies  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/local/bin/nscan"]  

