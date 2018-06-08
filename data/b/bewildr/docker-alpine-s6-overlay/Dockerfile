FROM bewildr/docker-alpine-base  
ARG S6OVERLAY_VERSION=1.21.4.0  
ARG S6OVERLAY_URL=https://github.com/just-
containers/s6-overlay/releases/download/v${S6OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz  
LABEL maintainer="Aadryn <aadryn@users.noreply.github.com>"  
LABEL s6-overlay=${S6OVERLAY_VERSION}  
COPY root.fs /  
RUN curl -fsL ${S6OVERLAY_URL} -o /tmp/s6-overlay-amd64.tar.gz \  
&& tar zxf /tmp/s6-overlay-amd64.tar.gz -C /  
STOPSIGNAL SIGTERM  
CMD [ "/init" ]

