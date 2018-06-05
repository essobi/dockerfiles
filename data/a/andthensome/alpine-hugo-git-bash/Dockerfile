FROM alpine:3.6  
MAINTAINER Ryan Kes <ryan@andthensome.nl>  
ADD VERSION .  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VCS_URL  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0-rc1"  
  
ENV HUGO_VERSION 0.31.1  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux-64bit  
  
# Install pygments (for syntax highlighting)  
RUN apk update && apk add py-pygments && apk add git && apk add bash && rm -rf
/var/cache/apk/*  
  
# Download and Install hugo  
ADD
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
/usr/local/  
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/bin/ \  
&& rm /usr/local/${HUGO_BINARY}.tar.gz  

