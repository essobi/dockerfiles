FROM alpine:latest  
ARG BUILD_DATE  
ARG VCS_REF  
ARG S6_OVERLAY_VERSION  
ARG S6_OVERLAY_ARCH  
ENV S6_OVERLAY_VERSION ${S6_OVERLAY_VERSION:-v1.21.2.2}  
ENV S6_OVERLAY_ARCH ${S6_OVERLAY_ARCH:-amd64}  
  
COPY rootfs /  
  
RUN apk update && \  
apk add \--no-cache \  
bash \  
curl \  
shadow  
  
RUN echo -e "alpine:latest\n$S6_OVERLAY_VERSION $S6_OVERLAY_ARCH" >
/s6_version.txt  
RUN curl -L --max-redirs 10 -o /tmp/s6-overlay-${S6_OVERLAY_ARCH}.tar.gz
https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-${S6_OVERLAY_ARCH}.tar.gz
\  
&& tar xzvf /tmp/s6-overlay-${S6_OVERLAY_ARCH}.tar.gz -C / \  
&& rm -rf /tmp/s6-overlay-${S6_OVERLAY_ARCH}.tar.gz  
  
VOLUME /data  
ENTRYPOINT ["/init"]  
  
# Build-time metadata as defined at http://label-schema.org  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="baseimage-s6" \  
org.label-schema.description="A docker base image using s6 overlay" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/fsimplice/docker-baseimage-s6" \  
org.label-schema.vendor="fsimplice" \  
org.label-schema.version=$S6_OVERLAY_VERSION \  
org.label-schema.schema-version="1.0" \  
org.label-schema.docker.params="PUID=user id (default 1000), PGID=user group
id (default 1000), USERNAME=username (default app)" \  
org.label-schema.docker.debug="docker exec -it $CONTAINER /bin/bash"

