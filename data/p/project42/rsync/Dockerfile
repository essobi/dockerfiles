FROM alpine:3.6  
MAINTAINER Jordan Clark jordan.clark@esu10.org  
  
RUN apk add \--no-cache rsync && \  
apk --no-cache --update upgrade  
  
ENTRYPOINT ["/usr/bin/rsync"]  

