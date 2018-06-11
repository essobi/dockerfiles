FROM alpine:3.6  
  
RUN apk upgrade \--no-cache --no-progress && \  
apk add \--no-cache --no-progress dumb-init  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  

