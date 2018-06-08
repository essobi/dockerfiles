FROM openjdk:8-alpine  
MAINTAINER TransactCharlie  
  
ARG VCS_REF  
ARG BUILD_DATE  
ENV RIEMANN_VERSION 0.2.14  
LABEL org.label-schema.name="Riemann" \  
org.label-schema.description="Riemann monitoring system on alpine linux" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.url="http://riemann.io" \  
org.label-schema.version=$RIEMANN_VERSION \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/TransactCharlie/docker-riemann"  
  
# Install Riemann  
RUN apk update \  
&& apk add openssl \  
&& wget
https://github.com/riemann/riemann/releases/download/$RIEMANN_VERSION/riemann-$RIEMANN_VERSION.tar.bz2
\  
&& tar xvfj riemann-$RIEMANN_VERSION.tar.bz2 \  
&& mv riemann-$RIEMANN_VERSION /riemann \  
&& rm riemann-$RIEMANN_VERSION.tar.bz2  
  
# / after this will point to /riemann (chroot analogue)  
WORKDIR /riemann  
  
## hack shell wrapper to use busybox sh (we don't have bash)  
RUN sed -ie 's/env bash/env sh/' bin/riemann  
  
## Default Expose Ports  
EXPOSE 5555/tcp 5555/udp 5556  
ENTRYPOINT ["bin/riemann"]  
CMD ["/config/riemann.config"]  

