FROM alpine:3.5  
MAINTAINER wolfy959@tuta.io  
  
ENV TINI_VERSION v0.14.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-
static-amd64 /tini  
RUN chmod +x /tini  
  
ENTRYPOINT ["/tini", "--"]  

