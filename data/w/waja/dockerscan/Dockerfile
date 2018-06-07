FROM alpine:3.7  
# Dockerfile Maintainer  
MAINTAINER Jan Wagner "waja@cyconet.org"  
ARG "BUILD_DATE=unknown"  
ARG "BUILD_VERSION=unknown"  
ARG "VCS_URL=unknown"  
ARG "VCS_REF=unknown"  
ARG "VCS_BRANCH=unknown"  
# See http://label-schema.org/rc1/ and https://microbadger.com/labels  
LABEL org.label-schema.name="dockerscan - security analysis & hacking tools" \  
org.label-schema.description="Docker security analysis & hacking tools on
Alpine Linux based container" \  
org.label-schema.vendor="Cyconet" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$BUILD_VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-branch=$VCS_BRANCH  
  
ENV DOCKERSCAN_VERSION 1.0.0a3  
  
RUN apk --no-cache update && apk --no-cache upgrade && \  
apk --no-cache add python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
pip install dockerscan==$DOCKERSCAN_VERSION && \  
rm -r /root/.cache  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["dockerscan"]  

