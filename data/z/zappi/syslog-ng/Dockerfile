FROM alpine:3.7  
LABEL maintainer "Zappi DevOps <devops@zappistore.com>"  
  
ARG SYSLOG_NG_VERSION="3.13.2-r0"  
RUN echo '@edge-main http://dl-cdn.alpinelinux.org/alpine/edge/main/' >>
/etc/apk/repositories && \  
apk update && \  
apk upgrade && \  
apk add \  
tini \  
openssl \  
syslog-ng@edge-main=${SYSLOG_NG_VERSION}  
  
ENTRYPOINT ["tini", "--"]  
CMD ["syslog-ng", "--foreground"]  

