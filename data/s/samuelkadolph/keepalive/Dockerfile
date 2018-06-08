FROM alpine:latest  
MAINTAINER samuel@kadolph.com  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.name="keepalive"  
LABEL org.label-schema.schema-version="1.0"  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/samuelkadolph/docker-
keepalive"  
  
RUN apk add --update curl && rm -rf /var/cache/apk/*  
  
COPY script /  
  
CMD /script  

