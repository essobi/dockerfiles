FROM alpine:edge  
MAINTAINER Jetsada Machom <jim@imjim.im>  
  
ARG VCS_REF  
  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-
url="https://github.com/zinuzoid/dockers/tree/master/puttygen"  
  
RUN apk --no-cache add \  
putty && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /app  
VOLUME /app  
WORKDIR /app  
  
ENTRYPOINT ["puttygen"]  

