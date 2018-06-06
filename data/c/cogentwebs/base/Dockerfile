FROM frolvlad/alpine-glibc  
  
MAINTAINER Pichate Ins <cogent@cogentwebsworks.com>  
  
LABEL com.base.cogentwebworks.version=v0.5.1  
  
ENV S6_VERSION=v1.21.2.2  
ENV SOCKLOG_VERSION=v2.1.0-1  
ENV LANG=C.UTF-8  
ENV TIMEZONE="/Etc/UTC"  
# root filesystem  
COPY rootfs /  
  
RUN apk-install bash  
  
# Install s6-overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz
/tmp/  
ADD https://github.com/just-containers/socklog-
overlay/releases/download/${SOCKLOG_VERSION}/socklog-overlay-amd64.tar.gz
/tmp/  
  
RUN tar xzf /tmp/socklog-overlay-amd64.tar.gz -C / && tar xzf /tmp/s6-overlay-
amd64.tar.gz -C / && apk-clean  
  
EXPOSE 8514  
# S6 INIT  
ENTRYPOINT [ "/init" ]

